import os

def generate_svg():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080" style="background-color: #F8FAFC; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <!-- Gradients -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1B365D"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0EA5E9"/>
    </linearGradient>
    <linearGradient id="alertGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#EF4444"/>
    </linearGradient>
    <linearGradient id="successGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#F59E0B"/>
    </linearGradient>

    <!-- Drop Shadows -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <filter id="shadowHeavy" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.15"/>
    </filter>

    <!-- Markers for Flow Arrows -->
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#4F46E5"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#EF4444"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10B981"/>
    </marker>

    <!-- Dot Matrix Pattern -->
    <pattern id="dotMatrix" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.2" fill="#CBD5E1"/>
    </pattern>
  </defs>

  <!-- Background Dot Matrix -->
  <rect width="1920" height="1080" fill="#F8FAFC"/>
  <rect width="1920" height="1080" fill="url(#dotMatrix)"/>

  <!-- HEADER BAR -->
  <rect x="0" y="0" width="1920" height="75" fill="url(#headerGrad)"/>
  
  <!-- Left Badge -->
  <rect x="30" y="18" width="140" height="38" rx="19" fill="#38BDF8" fill-opacity="0.15" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="100" y="43" text-anchor="middle" font-size="16" font-weight="700" fill="#38BDF8">MineNova6</text>

  <!-- Main Title -->
  <text x="960" y="46" text-anchor="middle" font-size="26" font-weight="800" fill="#FFFFFF" letter-spacing="1">TECHNICAL APPROACH &amp; SYSTEM ARCHITECTURE</text>
  <text x="960" y="66" text-anchor="middle" font-size="12" font-weight="600" fill="#94A3B8">MineGuard AI (PS ID: SIH26025) — Real-Time Mine Subsidence Monitoring &amp; Early Warning System</text>

  <!-- Right SIH Badge -->
  <rect x="1720" y="18" width="170" height="38" rx="8" fill="#FFFFFF" fill-opacity="0.1" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="1"/>
  <text x="1805" y="42" text-anchor="middle" font-size="13" font-weight="700" fill="#F59E0B">SIH 2026 OFFICIAL</text>

  <!-- ========================================================================= -->
  <!-- LEFT COLUMN: BACKEND ARCHITECTURE & AI ENGINE (X: 30 to 600) -->
  <!-- ========================================================================= -->

  <!-- DOCKER CONTAINER CONTAINER -->
  <rect x="30" y="95" width="570" height="575" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <!-- Docker Container Header Badge -->
  <rect x="45" y="110" width="220" height="32" rx="6" fill="#0284C7"/>
  <text x="155" y="131" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">BACKEND ARCHITECTURE</text>

  <!-- Docker Label Vertical Pill -->
  <rect x="45" y="155" width="30" height="495" rx="6" fill="#0EA5E9" fill-opacity="0.1" stroke="#0EA5E9" stroke-width="1"/>
  <text x="60" y="410" text-anchor="middle" font-size="12" font-weight="700" fill="#0284C7" transform="rotate(-90 60 410)">DOCKER CONTAINER ENVIRONMENT</text>

  <!-- Local DB Section -->
  <rect x="90" y="155" width="495" height="105" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="105" y="178" font-size="13" font-weight="700" fill="#1B365D">Local &amp; Cloud Database Layer</text>
  
  <!-- DB Box 1: TimescaleDB -->
  <rect x="105" y="190" width="225" height="58" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="115" y="212" font-size="12" font-weight="700" fill="#0284C7">TimescaleDB / SQLite</text>
  <text x="115" y="232" font-size="10" font-weight="500" fill="#64748B">Stores 2.5s time-series IoT telemetry</text>

  <!-- DB Box 2: PostgreSQL -->
  <rect x="345" y="190" width="225" height="58" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="355" y="212" font-size="12" font-weight="700" fill="#4F46E5">PostgreSQL / SQLAlchemy</text>
  <text x="355" y="232" font-size="10" font-weight="500" fill="#64748B">Relational mine seam &amp; alert records</text>

  <!-- API Gateway & Middleware -->
  <rect x="90" y="275" width="425" height="150" rx="10" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <text x="105" y="298" font-size="13" font-weight="700" fill="#3730A3">Python FastAPI REST &amp; WebSocket Server</text>
  
  <!-- Fast API sub-components -->
  <rect x="105" y="310" width="190" height="45" rx="6" fill="#FFFFFF" stroke="#A5B4FC" stroke-width="1"/>
  <text x="115" y="330" font-size="11" font-weight="700" fill="#4338CA">FastAPI Event Loop</text>
  <text x="115" y="345" font-size="9" stroke="none" fill="#64748B">Async ASGI &amp; Pydantic</text>

  <rect x="310" y="310" width="190" height="45" rx="6" fill="#FFFFFF" stroke="#A5B4FC" stroke-width="1"/>
  <text x="320" y="330" font-size="11" font-weight="700" fill="#4338CA">WebSocket Broadcaster</text>
  <text x="320" y="345" font-size="9" fill="#64748B">Real-time 2.5s UI push</text>

  <rect x="105" y="365" width="395" height="45" rx="6" fill="#FFFFFF" stroke="#A5B4FC" stroke-width="1"/>
  <text x="115" y="385" font-size="11" font-weight="700" fill="#3730A3">SIH Emergency Simulator Service</text>
  <text x="115" y="400" font-size="9" fill="#64748B">One-click live stress simulation engine</text>

  <!-- Vertical API Gateway Pill -->
  <rect x="525" y="275" width="60" height="150" rx="8" fill="#4F46E5"/>
  <text x="555" y="350" text-anchor="middle" font-size="12" font-weight="800" fill="#FFFFFF" transform="rotate(-90 555 350)">API GATEWAY</text>

  <!-- Message Router & Ingestion -->
  <rect x="90" y="440" width="495" height="100" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="105" y="462" font-size="13" font-weight="700" fill="#1B365D">Kafka / Telemetry Message Ingestion Pipeline</text>
  
  <rect x="105" y="475" width="225" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="115" y="495" font-size="11" font-weight="700" fill="#0EA5E9">IoT Telemetry Gateway</text>
  <text x="115" y="512" font-size="9" fill="#64748B">HTTP POST JSON Ingestion</text>

  <rect x="345" y="475" width="225" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="355" y="495" font-size="11" font-weight="700" fill="#059669">Stream Analytics Engine</text>
  <text x="355" y="512" font-size="9" fill="#64748B">Calculates 5-min rates of change</text>

  <!-- Architecture Note -->
  <rect x="90" y="555" width="495" height="85" rx="8" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="105" y="578" font-size="12" font-weight="700" fill="#334155">⚡ Service-Oriented Architecture (SOA)</text>
  <text x="105" y="598" font-size="10" font-weight="500" fill="#475569">• Decoupled FastAPI backend &amp; React frontend ready for cloud/edge.</text>
  <text x="105" y="616" font-size="10" font-weight="500" fill="#475569">• Easily scales to 100+ mine nodes with TimescaleDB time-series indexing.</text>

  <!-- AI COMPONENTS CONTAINER -->
  <rect x="30" y="685" width="570" height="365" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="45" y="700" width="200" height="32" rx="6" fill="#4F46E5"/>
  <text x="145" y="721" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">AI PREDICTIVE ENGINE</text>

  <!-- Tech Badges -->
  <rect x="255" y="702" width="90" height="28" rx="14" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="300" y="720" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">Python 3.12</text>

  <rect x="355" y="702" width="100" height="28" rx="14" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="405" y="720" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">scikit-learn</text>

  <rect x="465" y="702" width="80" height="28" rx="14" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="505" y="720" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">joblib</text>

  <!-- Random Forest Card -->
  <rect x="45" y="745" width="540" height="120" rx="10" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
  <text x="60" y="770" font-size="14" font-weight="700" fill="#991B1B">🌲 Random Forest Regressor &amp; Classifier Ensemble</text>
  <text x="60" y="792" font-size="11" font-weight="600" fill="#B91C1C">• 10 Telemetry Parameters:</text>
  <text x="80" y="810" font-size="10" font-weight="500" fill="#475569">tilt_x, tilt_y, displacement, prop_load, temp, humidity, vibration</text>
  <text x="60" y="830" font-size="11" font-weight="700" fill="#DC2626">• Rate-of-Change Velocity Weighting (42% Weight):</text>
  <text x="80" y="848" font-size="10" font-weight="600" fill="#991B1B">Prioritizes Δdisp/Δt &amp; Δtilt/Δt to catch Stage-1 micro-sagging before collapse.</text>

  <!-- Model Metrics Box -->
  <rect x="45" y="880" width="540" height="150" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="60" y="905" font-size="13" font-weight="700" fill="#1B365D">Model Accuracy &amp; Inference Specs:</text>
  
  <rect x="60" y="920" width="245" height="95" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="182" y="948" text-anchor="middle" font-size="11" font-weight="600" fill="#64748B">Mean Absolute Error (MAE)</text>
  <text x="182" y="985" text-anchor="middle" font-size="28" font-weight="800" fill="#059669">1.27</text>

  <rect x="320" y="920" width="245" height="95" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="442" y="948" text-anchor="middle" font-size="11" font-weight="600" fill="#64748B">Coefficient of Determination (R²)</text>
  <text x="442" y="985" text-anchor="middle" font-size="28" font-weight="800" fill="#4F46E5">0.9969</text>

  <!-- ========================================================================= -->
  <!-- CENTER COLUMN: UNDERGROUND COAL MINE & HARDWARE MESH (X: 630 to 1290) -->
  <!-- ========================================================================= -->

  <!-- TOP ADMIN & COMPLIANCE BOX -->
  <rect x="630" y="95" width="660" height="185" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="645" y="110" width="180" height="32" rx="6" fill="#1B365D"/>
  <text x="735" y="131" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">ADMIN &amp; COMPLIANCE</text>

  <!-- Admin Features Grid -->
  <rect x="645" y="155" width="315" height="110" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="660" y="178" font-size="12" font-weight="700" fill="#1B365D">📋 Digital SMP Compliance</text>
  <text x="660" y="196" font-size="10" font-weight="500" fill="#475569">• Digitizes DGMS Strata Management Plans.</text>
  <text x="660" y="214" font-size="10" font-weight="500" fill="#475569">• Automated PDF compliance report generation.</text>
  <text x="660" y="232" font-size="10" font-weight="500" fill="#475569">• Eliminates manual paper logbook errors.</text>

  <rect x="975" y="155" width="300" height="110" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="990" y="178" font-size="12" font-weight="700" fill="#1B365D">🚨 Critical Issue Resolution</text>
  <text x="990" y="196" font-size="10" font-weight="500" fill="#475569">• Real-time SMS &amp; Web dashboard alerts.</text>
  <text x="990" y="214" font-size="10" font-weight="500" fill="#475569">• Centralized worker shift assignment.</text>
  <text x="990" y="232" font-size="10" font-weight="500" fill="#475569">• Verifiable audit log for safety inspectors.</text>

  <!-- MAIN COAL MINE DEPLOYMENT BOX -->
  <rect x="630" y="295" width="660" height="540" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="645" y="310" width="220" height="32" rx="6" fill="#D97706"/>
  <text x="755" y="331" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">COAL MINE DEPLOYMENT</text>

  <!-- Mine Seams Visual Illustration -->
  <rect x="645" y="355" width="630" height="250" rx="10" fill="#1E293B"/>
  
  <!-- Underground Strata Layers Graphic -->
  <path d="M 645 420 Q 960 400 1275 420 L 1275 605 L 645 605 Z" fill="#334155"/>
  <path d="M 645 480 Q 960 460 1275 480 L 1275 605 L 645 605 Z" fill="#0F172A"/>

  <text x="960" y="380" text-anchor="middle" font-size="13" font-weight="700" fill="#F8FAFC">UNDERGROUND COAL MINE SEAM &amp; ROOF STRATA</text>

  <!-- Mine Nodes Graphic representation -->
  <!-- Node N1 -->
  <circle cx="730" cy="450" r="16" fill="#10B981" stroke="#FFFFFF" stroke-width="2"/>
  <text x="730" y="455" text-anchor="middle" font-size="11" font-weight="800" fill="#FFFFFF">N1</text>

  <!-- Node N2 -->
  <circle cx="880" cy="435" r="16" fill="#10B981" stroke="#FFFFFF" stroke-width="2"/>
  <text x="880" y="440" text-anchor="middle" font-size="11" font-weight="800" fill="#FFFFFF">N2</text>

  <!-- Node N5 (Danger) -->
  <circle cx="1040" cy="460" r="18" fill="#EF4444" stroke="#FFFFFF" stroke-width="3"/>
  <circle cx="1040" cy="460" r="26" fill="none" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="1040" y="465" text-anchor="middle" font-size="12" font-weight="800" fill="#FFFFFF">N5</text>

  <!-- Node N6 -->
  <circle cx="1190" cy="445" r="16" fill="#10B981" stroke="#FFFFFF" stroke-width="2"/>
  <text x="1190" y="450" text-anchor="middle" font-size="11" font-weight="800" fill="#FFFFFF">N6</text>

  <!-- LoRa Wireless Connections -->
  <path d="M 746 450 L 864 435" stroke="#38BDF8" stroke-width="2" stroke-dasharray="6,4"/>
  <path d="M 896 435 L 1022 460" stroke="#38BDF8" stroke-width="2" stroke-dasharray="6,4"/>
  <path d="M 1058 460 L 1174 445" stroke="#38BDF8" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="960" y="430" text-anchor="middle" font-size="11" font-weight="700" fill="#38BDF8">868MHz LoRa Chirp Spread Spectrum (2km Range)</text>

  <!-- Hardware Node Detail Card Overlay -->
  <rect x="660" y="500" width="600" height="95" rx="8" fill="#FFFFFF" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="1"/>
  <text x="675" y="522" font-size="12" font-weight="700" fill="#1B365D">Wireless ESP32 Sensor Node Hardware Suite (₹1,590/node):</text>
  <text x="675" y="542" font-size="10" font-weight="600" fill="#334155">• ESP32 (32-bit MCU) + SX1276 LoRa 868MHz Transceiver</text>
  <text x="675" y="558" font-size="10" font-weight="600" fill="#334155">• MPU6050 Gyro/Accel (Tilt &amp; Vib) | Linear String Potentiometer (Sag 0-50mm)</text>
  <text x="675" y="574" font-size="10" font-weight="600" fill="#334155">• HX711 Load Cell Amp (Prop Stress 0-200kN) | DHT22 (Temp/Hum)</text>

  <!-- Edge Failover Section -->
  <rect x="645" y="620" width="630" height="200" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="660" y="643" font-size="13" font-weight="700" fill="#1B365D">🚨 Dual Edge Failover Resilience &amp; Zero-Internet Mode</text>
  
  <rect x="660" y="655" width="295" height="150" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
  <text x="675" y="678" font-size="12" font-weight="700" fill="#047857">🟢 Primary Connection (Online)</text>
  <text x="675" y="698" font-size="10" font-weight="500" fill="#065F46">• Telemetry sent directly via ESP32 LoRa Gateway.</text>
  <text x="675" y="714" font-size="10" font-weight="500" fill="#065F46">• HTTP POST JSON to FastAPI REST Backend.</text>
  <text x="675" y="730" font-size="10" font-weight="500" fill="#065F46">• Instant WebSocket broadcast to React dashboard.</text>

  <rect x="970" y="655" width="290" height="150" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="985" y="678" font-size="12" font-weight="700" fill="#B91C1C">🔴 Fallback Mode (No Internet)</text>
  <text x="985" y="698" font-size="10" font-weight="500" fill="#991B1B">• ESP32 MCU evaluates edge risk threshold locally.</text>
  <text x="985" y="714" font-size="10" font-weight="700" fill="#DC2626">• Triggers 1kHz Piezo Siren Buzzer (GPIO 12/13).</text>
  <text x="985" y="730" font-size="10" font-weight="500" fill="#991B1B">• Buffers telemetry locally to SD card to prevent loss.</text>

  <!-- DATA PRIVACY & SECURITY CONTAINER -->
  <rect x="630" y="850" width="660" height="200" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="645" y="865" width="220" height="32" rx="6" fill="#059669"/>
  <text x="755" y="886" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">DATA PRIVACY &amp; SECURITY</text>

  <rect x="645" y="910" width="195" height="125" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="655" y="933" font-size="11" font-weight="700" fill="#1B365D">🔒 Zero Trust Architecture</text>
  <text x="655" y="953" font-size="9" font-weight="500" fill="#475569">Intranet-only access blocking unauthorized external connections.</text>

  <rect x="855" y="910" width="210" height="125" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="865" y="933" font-size="11" font-weight="700" fill="#1B365D">🔑 End-to-End Encryption</text>
  <text x="865" y="953" font-size="9" font-weight="500" fill="#475569">AES-128 telemetry encryption &amp; secure SHA-256 data hashing.</text>

  <rect x="1080" y="910" width="195" height="125" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="1090" y="933" font-size="11" font-weight="700" fill="#1B365D">🛡️ Intrinsically Safe (IS)</text>
  <text x="1090" y="953" font-size="9" font-weight="500" fill="#475569">Polycarbonate flameproof IP67 enclosure for firedamp safety.</text>

  <!-- ========================================================================= -->
  <!-- RIGHT COLUMN: FRONTEND COMMAND CENTER & SIH DEMO (X: 1320 to 1890) -->
  <!-- ========================================================================= -->

  <!-- REACT COMMAND CENTER CONTAINER -->
  <rect x="1320" y="95" width="570" height="575" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="1335" y="110" width="250" height="32" rx="6" fill="#6366F1"/>
  <text x="1460" y="131" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">REACT 18 COMMAND CENTER</text>

  <text x="1870" y="131" text-anchor="end" font-size="12" font-weight="700" fill="#6366F1">Web / Desktop App</text>

  <!-- Tech Stack Pills -->
  <rect x="1335" y="155" width="80" height="26" rx="13" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1375" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#4338CA">React 18</text>

  <rect x="1425" y="155" width="60" height="26" rx="13" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1455" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#4338CA">Vite</text>

  <rect x="1495" y="155" width="90" height="26" rx="13" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1540" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#4338CA">Tailwind CSS</text>

  <rect x="1595" y="155" width="85" height="26" rx="13" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1637" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#4338CA">Leaflet Map</text>

  <rect x="1690" y="155" width="80" height="26" rx="13" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1730" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#4338CA">Recharts</text>

  <!-- Monitor UI Graphic -->
  <rect x="1335" y="195" width="540" height="280" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2" filter="url(#shadowHeavy)"/>
  
  <!-- Monitor Header -->
  <rect x="1335" y="195" width="540" height="30" rx="10" fill="#F1F5F9"/>
  <circle cx="1355" cy="210" r="5" fill="#EF4444"/>
  <circle cx="1370" cy="210" r="5" fill="#F59E0B"/>
  <circle cx="1385" cy="210" r="5" fill="#10B981"/>
  <text x="1605" y="214" text-anchor="middle" font-size="11" font-weight="600" fill="#64748B">MineGuard AI — Command Center Dashboard</text>

  <!-- Monitor Dashboard Body Preview -->
  <rect x="1345" y="235" width="520" height="230" rx="6" fill="#F8FAFC"/>
  
  <!-- SIH Demo bar in UI mockup -->
  <rect x="1355" y="245" width="500" height="28" rx="6" fill="#6366F1"/>
  <text x="1420" y="263" font-size="10" font-weight="800" fill="#FFFFFF">SIH DEMO MODE</text>
  <rect x="1680" y="250" width="50" height="18" rx="4" fill="#10B981"/><text x="1705" y="263" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">Normal</text>
  <rect x="1735" y="250" width="55" height="18" rx="4" fill="#F59E0B"/><text x="1762" y="263" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">Warning</text>
  <rect x="1795" y="250" width="50" height="18" rx="4" fill="#EF4444"/><text x="1820" y="263" text-anchor="middle" font-size="9" font-weight="700" fill="#FFFFFF">Hazard</text>

  <!-- Metric Cards in UI mockup -->
  <rect x="1355" y="280" width="90" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/><text x="1360" y="293" font-size="7" font-weight="700" fill="#64748B">OVERALL MINE RISK</text><text x="1360" y="312" font-size="14" font-weight="800" fill="#10B981">18/100</text>
  <rect x="1452" y="280" width="90" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/><text x="1457" y="293" font-size="7" font-weight="700" fill="#64748B">ACTIVE NODES</text><text x="1457" y="312" font-size="14" font-weight="800" fill="#4F46E5">6/6</text>
  <rect x="1549" y="280" width="90" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/><text x="1554" y="293" font-size="7" font-weight="700" fill="#64748B">HIGH RISK ZONES</text><text x="1554" y="312" font-size="14" font-weight="800" fill="#059669">0</text>
  <rect x="1646" y="280" width="90" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/><text x="1651" y="293" font-size="7" font-weight="700" fill="#64748B">WARNINGS</text><text x="1651" y="312" font-size="14" font-weight="800" fill="#F59E0B">1</text>
  <rect x="1743" y="280" width="112" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/><text x="1748" y="293" font-size="7" font-weight="700" fill="#64748B">LAST SYNC</text><text x="1748" y="312" font-size="11" font-weight="800" fill="#1B365D">04:03:19 PM</text>

  <!-- Map and Gauge in mockup -->
  <rect x="1355" y="328" width="310" height="127" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
  <text x="1365" y="342" font-size="9" font-weight="700" fill="#1B365D">Underground Seam Geo-spatial Map (Jharia Coalfield #4)</text>
  <path d="M 1365 370 L 1420 360 L 1480 390 L 1550 375 L 1655 410" stroke="#CBD5E1" stroke-width="2" fill="none"/>
  <circle cx="1420" cy="360" r="6" fill="#10B981"/><circle cx="1480" cy="390" r="6" fill="#10B981"/><circle cx="1550" cy="375" r="7" fill="#EF4444"/>

  <rect x="1675" y="328" width="180" height="127" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
  <text x="1685" y="342" font-size="9" font-weight="700" fill="#1B365D">AI Subsidence Predictor</text>
  <path d="M 1705 420 A 45 45 0 0 1 1825 420" fill="none" stroke="#E2E8F0" stroke-width="10"/>
  <path d="M 1705 420 A 45 45 0 0 1 1740 380" fill="none" stroke="#10B981" stroke-width="10"/>
  <text x="1765" y="440" text-anchor="middle" font-size="11" font-weight="800" fill="#10B981">18 / 100 LOW</text>

  <!-- Supervisor Role Cards -->
  <rect x="1335" y="490" width="260" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="1350" y="512" font-size="11" font-weight="700" fill="#1B365D">👨‍💼 Shift Supervisor View</text>
  <text x="1350" y="530" font-size="9" font-weight="500" fill="#475569">• Real-time round planning &amp; task allotment.</text>
  <text x="1350" y="546" font-size="9" font-weight="500" fill="#475569">• Digital shift handover approval &amp; submission.</text>

  <rect x="1615" y="490" width="260" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="1630" y="512" font-size="11" font-weight="700" fill="#1B365D">👷 Strata Control Engineer</text>
  <text x="1630" y="530" font-size="9" font-weight="500" fill="#475569">• Monitors 60 FPS rolling rate-of-change graphs.</text>
  <text x="1630" y="546" font-size="9" font-weight="500" fill="#475569">• Receives predictive pre-failure roof sag warnings.</text>

  <!-- Live Sync Feature Card -->
  <rect x="1335" y="575" width="540" height="80" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="1350" y="598" font-size="11" font-weight="700" fill="#3730A3">🔄 Cross-Device Real-Time Synchronization</text>
  <text x="1350" y="616" font-size="10" font-weight="500" fill="#4338CA">• BroadcastChannel API &amp; Epoch time seeding syncs live telemetry across devices.</text>
  <text x="1350" y="632" font-size="10" font-weight="500" fill="#4338CA">• Judges can open live Vercel URL on mobile phones to view synchronized real-time data.</text>

  <!-- MINERS & SHIFT OPERATORS MOBILE & EDGE NOTIFICATIONS CONTAINER -->
  <rect x="1320" y="685" width="570" height="365" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
  
  <rect x="1335" y="700" width="230" height="32" rx="6" fill="#10B981"/>
  <text x="1450" y="721" text-anchor="middle" font-size="14" font-weight="700" fill="#FFFFFF">SHIFT OPERATORS &amp; ALERTS</text>

  <!-- Mobile & Edge Features Grid -->
  <rect x="1335" y="745" width="260" height="140" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="1350" y="770" font-size="12" font-weight="700" fill="#1B365D">📱 Field Worker Mobile App</text>
  <text x="1350" y="792" font-size="10" font-weight="500" fill="#475569">• Quick summary of assigned shifts &amp; tasks.</text>
  <text x="1350" y="810" font-size="10" font-weight="500" fill="#475569">• Log safety issues &amp; equipment status.</text>
  <text x="1350" y="828" font-size="10" font-weight="500" fill="#475569">• Multilingual support for Indian languages.</text>
  <text x="1350" y="846" font-size="10" font-weight="500" fill="#475569">• Smart voice-assisted task logging.</text>

  <rect x="1615" y="745" width="260" height="140" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="1630" y="770" font-size="12" font-weight="700" fill="#B91C1C">🔊 Instant Evacuation Alarms</text>
  <text x="1630" y="792" font-size="10" font-weight="500" fill="#991B1B">• 1kHz Local Piezo Siren at mine face.</text>
  <text x="1630" y="810" font-size="10" font-weight="700" fill="#DC2626">• Provides vital minutes of warning.</text>
  <text x="1630" y="828" font-size="10" font-weight="500" fill="#991B1B">• Instant visual warning ring on Leaflet map.</text>
  <text x="1630" y="846" font-size="10" font-weight="500" fill="#991B1B">• Zero false alarm velocity validation.</text>

  <!-- Live Deployment & Links Box -->
  <rect x="1335" y="900" width="540" height="130" rx="10" fill="#1E293B"/>
  <text x="1350" y="925" font-size="13" font-weight="700" fill="#38BDF8">🌐 LIVE PROJECT DEPLOYMENT &amp; LINKS</text>
  
  <text x="1350" y="952" font-size="11" font-weight="600" fill="#F8FAFC">• Live Vercel Command Center:</text>
  <text x="1560" y="952" font-size="11" font-weight="700" fill="#38BDF8">https://mineguard-ai.vercel.app</text>

  <text x="1350" y="976" font-size="11" font-weight="600" fill="#F8FAFC">• Official GitHub Repository:</text>
  <text x="1560" y="976" font-size="11" font-weight="700" fill="#38BDF8">https://github.com/sharequesyed/MineGuard-AI</text>

  <text x="1350" y="1005" font-size="10" font-weight="500" fill="#94A3B8">Team MineNova6 — Smart India Hackathon (SIH 2026) Idea Submission Deck</text>

  <!-- ========================================================================= -->
  <!-- PIPELINE FLOW CONNECTING ARROWS -->
  <!-- ========================================================================= -->

  <!-- Flow 1: Coal Mine to Gateway -->
  <path d="M 645 450 Q 610 450 600 480" fill="none" stroke="#4F46E5" stroke-width="2.5" marker-end="url(#arrow)"/>
  
  <!-- Flow 2: FastAPI to React Monitor -->
  <path d="M 600 350 L 1335 245" fill="none" stroke="#4F46E5" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow)"/>

  <!-- Flow 3: AI Model to FastAPI -->
  <path d="M 300 685 L 300 425" fill="none" stroke="#4F46E5" stroke-width="2.5" marker-end="url(#arrow)"/>

</svg>'''
    
    output_svg = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\mineguard_ai_technical_approach.svg"
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG generated successfully at: {output_svg}")

if __name__ == '__main__':
    generate_svg()
