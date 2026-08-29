/*
 * MineGuard AI — ESP32 + MPU6050 + SX1276 LoRa Telemetry Node
 * Team MineNova6 | Problem Statement ID: SIH26025
 * 
 * Hardware Wiring:
 * - MPU6050: SDA -> GPIO 21, SCL -> GPIO 22
 * - SX1276 LoRa: SCK -> GPIO 18, MISO -> GPIO 19, MOSI -> GPIO 23, SS -> GPIO 5, RST -> GPIO 14, DIO0 -> GPIO 2
 */

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <SPI.h>
#include <LoRa.h>

#define NODE_ID "N5"
#define LORA_BAND 868E6 // 868 MHz for India/EU license-free ISM band

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("Initializing MineGuard AI ESP32 LoRa Node...");

  // 1. Initialize MPU6050 Gyro & Accelerometer
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip!");
    while (1) { delay(10); }
  }
  Serial.println("MPU6050 initialized.");

  // Set MPU6050 accelerometer & gyro ranges
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  // 2. Initialize SX1276 LoRa Radio Module
  LoRa.setPins(5, 14, 2); // SS, RST, DIO0
  if (!LoRa.begin(LORA_BAND)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  Serial.println("LoRa Radio online at 868 MHz.");
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Compute tilt angle from accelerometer Z and X vectors
  float tilt_angle = atan2(a.acceleration.x, sqrt(a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z)) * 180.0 / M_PI;
  float vibration = sqrt(a.acceleration.x * a.acceleration.x + a.acceleration.y * a.acceleration.y + a.acceleration.z * a.acceleration.z) / 9.81;

  // Simulated pot displacement & crack width for demonstration
  float displacement = analogRead(34) * (50.0 / 4095.0); // 0-50mm range
  float crack_width = analogRead(35) * (20.0 / 4095.0);  // 0-20mm range
  float battery = 96.5;

  // Format telemetry payload string
  String payload = String(NODE_ID) + "," +
                   String(tilt_angle, 2) + "," +
                   String(displacement, 2) + "," +
                   String(crack_width, 2) + "," +
                   String(vibration, 3) + "," +
                   String(temp.temperature, 1) + "," +
                   String(battery, 1);

  Serial.print("Broadcasting LoRa Packet: ");
  Serial.println(payload);

  // Send packet via LoRa
  LoRa.beginPacket();
  LoRa.print(payload);
  LoRa.endPacket();

  delay(3000); // 3-second transmission interval
}
