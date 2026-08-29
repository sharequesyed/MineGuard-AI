/*
 * MineGuard AI — ESP32 LoRa Gateway Receiver (Hub Node)
 * Team MineNova6 | Problem Statement ID: SIH26025
 * 
 * Function: Receives 868MHz LoRa telemetry packets from underground ESP32 sensor nodes (N1 to N6)
 * and forwards the parsed data to the FastAPI Backend via Wi-Fi HTTP POST (or USB Serial Bridge).
 * 
 * Hardware Wiring:
 * - SX1276 LoRa: SCK -> GPIO 18, MISO -> GPIO 19, MOSI -> GPIO 23, SS -> GPIO 5, RST -> GPIO 14, DIO0 -> GPIO 2
 * - Red Siren LED: GPIO 12
 * - Warning Buzzer: GPIO 13
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <SPI.h>
#include <LoRa.h>

// Wi-Fi Credentials for Gateway Internet Connectivity
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";

// FastAPI Backend URL (Replace with your laptop IP address, e.g. http://192.168.1.10:8000/api/sensors/data)
const char* BACKEND_URL = "http://192.168.1.10:8000/api/sensors/data";

#define LORA_BAND 868E6
#define SIREN_LED 12
#define BUZZER_PIN 13

void setup() {
  Serial.begin(115200);
  pinMode(SIREN_LED, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  digitalWrite(SIREN_LED, LOW);
  digitalWrite(BUZZER_PIN, LOW);

  Serial.println("==========================================");
  Serial.println(" MineGuard AI — ESP32 LoRa Gateway Receiver");
  Serial.println("==========================================");

  // 1. Connect to Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Connecting to Wi-Fi");
  int timeout = 0;
  while (WiFi.status() != WL_CONNECTED && timeout < 20) {
    delay(500);
    Serial.print(".");
    timeout++;
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWi-Fi Connected! IP Address: " + WiFi.localIP().toString());
  } else {
    Serial.println("\nWi-Fi connection timed out. Gateway operating in Serial Bridge mode.");
  }

  // 2. Initialize SX1276 LoRa Module
  LoRa.setPins(5, 14, 2); // SS, RST, DIO0
  if (!LoRa.begin(LORA_BAND)) {
    Serial.println("CRITICAL ERROR: Starting LoRa receiver failed!");
    while (1);
  }
  Serial.println("LoRa Receiver active at 868 MHz. Waiting for node transmissions...\n");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    String incoming = "";
    while (LoRa.available()) {
      incoming += (char)LoRa.read();
    }

    int rssi = LoRa.packetRssi();
    float snr = LoRa.packetSnr();

    Serial.println("Received LoRa Packet: " + incoming + " | RSSI: " + String(rssi) + " dBm");

    // Parse Packet Payload: NODE_ID,TILT_DEG,DISP_MM,CRACK_MM,VIB_G,TEMP_C,BAT_PCT
    // Example: N5,4.82,14.50,5.10,0.825,29.4,96.5
    parseAndForwardPacket(incoming);
  }
}

void parseAndForwardPacket(String packet) {
  int commas[6];
  int count = 0;
  for (int i = 0; i < packet.length(); i++) {
    if (packet.charAt(i) == ',') {
      if (count < 6) commas[count++] = i;
    }
  }

  if (count < 6) {
    Serial.println("Invalid packet format received: " + packet);
    return;
  }

  String nodeId = packet.substring(0, commas[0]);
  float tilt = packet.substring(commas[0] + 1, commas[1]).toFloat();
  float disp = packet.substring(commas[1] + 1, commas[2]).toFloat();
  float crack = packet.substring(commas[2] + 1, commas[3]).toFloat();
  float vib = packet.substring(commas[3] + 1, commas[4]).toFloat();
  float temp = packet.substring(commas[4] + 1, commas[5]).toFloat();
  float bat = packet.substring(commas[5] + 1).toFloat();

  // Activate Hardware Siren/LED if hazard readings detected
  if (tilt > 3.5 || disp > 8.0 || crack > 4.0) {
    digitalWrite(SIREN_LED, HIGH);
    tone(BUZZER_PIN, 1000, 500); // 1kHz siren beep
  } else {
    digitalWrite(SIREN_LED, LOW);
  }

  // Construct JSON Payload for FastAPI Backend
  String jsonBody = "{"
    "\"node_id\":\"" + nodeId + "\","
    "\"tilt\":" + String(tilt, 2) + ","
    "\"displacement\":" + String(disp, 2) + ","
    "\"crack_width\":" + String(crack, 2) + ","
    "\"vibration\":" + String(vib, 3) + ","
    "\"load_change\":" + String(disp * 2.5, 1) + ","
    "\"temperature\":" + String(temp, 1) + ","
    "\"humidity\":80.0,"
    "\"battery\":" + String(bat, 1)
  "}";

  // Forward to FastAPI Backend via HTTP POST
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(BACKEND_URL);
    http.addHeader("Content-Type", "application/json");

    int httpCode = http.POST(jsonBody);
    if (httpCode == 200) {
      Serial.println("HTTP POST Success -> Backend updated (" + nodeId + ")");
    } else {
      Serial.println("HTTP POST Error Code: " + String(httpCode));
    }
    http.end();
  } else {
    // Serial Fallback for USB cable connection to laptop
    Serial.println("FORWARD_SERIAL:" + jsonBody);
  }
}
