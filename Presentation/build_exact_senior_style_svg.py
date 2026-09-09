import os

def generate_exact_senior_svg():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080" style="background-color: #FFFFFF; font-family: Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrow Markers -->
    <marker id="arrowBlack" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000"/>
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1890FF"/>
    </marker>
    
    <!-- Drop Shadow for Cards -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.1"/>
    </filter>
  </defs>

  <!-- PURE WHITE BACKGROUND -->
  <rect width="1920" height="1080" fill="#FFFFFF"/>

  <!-- ========================================================================= -->
  <!-- TOP HEADER BAR -->
  <!-- ========================================================================= -->

  <!-- Top-Left Team Name Badge (Senior Hand-Drawn Oval Style) -->
  <ellipse cx="80" cy="40" rx="55" ry="22" fill="none" stroke="#000000" stroke-width="2.5"/>
  <text x="80" y="47" text-anchor="middle" font-size="22" font-weight="bold" fill="#000000">MineNova6</text>

  <!-- Center Title -->
  <text x="960" y="52" text-anchor="middle" font-size="38" font-weight="bold" fill="#000000" letter-spacing="-0.5">Technical Approach</text>

  <!-- Top-Right SIH 2026 Logo Badge -->
  <g transform="translate(1730, 15)">
    <circle cx="25" cy="25" r="22" fill="#F59E0B"/>
    <path d="M 15 25 L 23 33 L 35 17" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
    <text x="55" y="24" font-size="12" font-weight="bold" fill="#000000">SMART INDIA</text>
    <text x="55" y="38" font-size="12" font-weight="bold" fill="#000000">HACKATHON 2026</text>
  </g>

  <!-- ========================================================================= -->
  <!-- LEFT COLUMN: BACKEND ARCHITECTURE (SECTION 4) & AI COMPONENTS (SECTION 8) -->
  <!-- ========================================================================= -->

  <!-- Section 4 Number Circle & Black Pill Header -->
  <circle cx="85" cy="105" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <text x="85" y="110" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">4</text>

  <rect x="110" y="85" width="340" height="42" rx="21" fill="#000000"/>
  <text x="280" y="112" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF" letter-spacing="1">BACKEND ARCHITECTURE</text>

  <!-- Docker Container Left Blue Vertical Pill -->
  <rect x="25" y="145" width="45" height="470" rx="22.5" fill="#3B82F6"/>
  <!-- Docker Icon Circle -->
  <circle cx="47.5" cy="175" r="15" fill="#FFFFFF"/>
  <text x="47.5" y="180" text-anchor="middle" font-size="16" font-weight="bold" fill="#3B82F6">🐳</text>
  <text x="47.5" y="390" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF" transform="rotate(-90 47.5 390)">Docker Container</text>

  <!-- Main Backend Architecture Box (Light Blue) -->
  <rect x="80" y="145" width="440" height="470" rx="10" fill="#E6F7FF" stroke="#91D5FF" stroke-width="1.5"/>

  <!-- Local DB Section -->
  <text x="390" y="165" font-size="12" font-weight="bold" fill="#1890FF">Local DB</text>
  <text x="360" y="178" font-size="10" fill="#595959">Slave    Master</text>

  <g transform="translate(95, 175)">
    <rect x="0" y="0" width="165" height="70" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
    <text x="10" y="25" font-size="12" font-weight="bold" fill="#000000">Time-series DB</text>
    <text x="10" y="42" font-size="11" fill="#595959">to store IoT data</text>
    <text x="10" y="58" font-size="9" fill="#1890FF">TimescaleDB / SQLite</text>
  </g>

  <g transform="translate(275, 175)">
    <rect x="0" y="0" width="150" height="70" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
    <text x="10" y="25" font-size="12" font-weight="bold" fill="#000000">To store Relational</text>
    <text x="10" y="42" font-size="12" font-weight="bold" fill="#000000">Data</text>
    <text x="10" y="58" font-size="9" fill="#1890FF">PostgreSQL / SQLAlchemy</text>
  </g>

  <!-- ERP Service / General Server (Light Orange Box) -->
  <g transform="translate(95, 260)">
    <rect x="0" y="0" width="330" height="55" rx="6" fill="#FFF5E6" stroke="#FFD591"/>
    <text x="165" y="33" text-anchor="middle" font-size="15" font-weight="bold" fill="#D46B08">ERP Service/General Server</text>
    <text x="25" y="33" font-size="11" fill="#8C8C8C">(ex) Express.js</text>
    <text x="290" y="33" font-size="11" font-weight="bold" fill="#52C41A">N Nginx</text>
  </g>

  <!-- IOT Service & AI Service (Light Grey & Light Orange) -->
  <g transform="translate(95, 330)">
    <rect x="0" y="0" width="155" height="45" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/>
    <text x="15" y="27" font-size="12" font-weight="bold" fill="#595959">(ex) IOT Service</text>
  </g>

  <g transform="translate(265, 330)">
    <rect x="0" y="0" width="160" height="45" rx="6" fill="#FFF5E6" stroke="#FFD591"/>
    <text x="20" y="27" font-size="13" font-weight="bold" fill="#D46B08">🐍 AI Service</text>
    <text x="105" y="27" font-size="10" fill="#8C8C8C">Python</text>
  </g>

  <!-- Text line between services -->
  <text x="260" y="392" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Produced data consumed by various services ↑</text>

  <!-- Kafka Message Bus Box (Light Blue) -->
  <g transform="translate(95, 405)">
    <rect x="0" y="0" width="330" height="70" rx="6" fill="#BAE7FF" stroke="#69C0FF"/>
    <text x="165" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#0050B3">⚙️ Kafka - Message Bus</text>
    <text x="165" y="54" text-anchor="middle" font-size="15" font-weight="bold" fill="#003A8C">Zookeeper</text>
  </g>

  <text x="260" y="492" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Data from IOT Pipelined</text>

  <!-- IOT Gateway Service (Light Green Box) -->
  <g transform="translate(95, 500)">
    <rect x="0" y="0" width="330" height="55" rx="6" fill="#F6FFED" stroke="#B7EB8F"/>
    <text x="165" y="33" text-anchor="middle" font-size="15" font-weight="bold" fill="#389E0D">IOT Gateway Service</text>
    <text x="25" y="33" font-size="11" fill="#8C8C8C">(ex) Express.js</text>
    <text x="290" y="33" font-size="11" font-weight="bold" fill="#52C41A">N Nginx</text>
  </g>

  <!-- Left Side Stack (Flink Stream & Elasticsearch Search) -->
  <g transform="translate(20, 410)">
    <rect x="0" y="0" width="55" height="90" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
    <text x="27.5" y="25" text-anchor="middle" font-size="16">🐿️</text>
    <text x="27.5" y="45" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Flink</text>
    <text x="27.5" y="60" text-anchor="middle" font-size="8" fill="#595959">Real-time stream</text>
    <text x="27.5" y="72" text-anchor="middle" font-size="8" fill="#595959">processing</text>
  </g>

  <g transform="translate(20, 510)">
    <rect x="0" y="0" width="55" height="90" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
    <text x="27.5" y="25" text-anchor="middle" font-size="16">🔍</text>
    <text x="27.5" y="45" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Elasticsearch</text>
    <text x="27.5" y="60" text-anchor="middle" font-size="8" fill="#595959">Search and</text>
    <text x="27.5" y="72" text-anchor="middle" font-size="8" fill="#595959">Analytics</text>
  </g>

  <!-- API GATEWAY Vertical Blue Bar -->
  <g transform="translate(530, 145)">
    <rect x="0" y="0" width="36" height="470" rx="18" fill="#1890FF"/>
    <text x="18" y="70" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">A</text>
    <text x="18" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">P</text>
    <text x="18" y="150" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">I</text>
    <text x="18" y="220" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">G</text>
    <text x="18" y="260" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">A</text>
    <text x="18" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">T</text>
    <text x="18" y="340" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">E</text>
    <text x="18" y="380" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">W</text>
    <text x="18" y="420" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">A</text>
    <text x="18" y="450" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">Y</text>
  </g>

  <!-- Data Privacy & Security Column -->
  <g transform="translate(575, 145)">
    <rect x="0" y="0" width="30" height="470" rx="6" fill="#F5F5F5" stroke="#D9D9D9" stroke-dasharray="4,4"/>
    <text x="15" y="240" text-anchor="middle" font-size="13" font-weight="bold" fill="#000000" transform="rotate(-90 15 240)">Data Privacy &amp; Security</text>
  </g>

  <!-- Bottom Left Text Note & File System -->
  <text x="25" y="640" font-size="13" font-weight="bold" fill="#000000">We use SOA architecture for flexible</text>
  <text x="25" y="658" font-size="13" font-weight="bold" fill="#000000">and efficient integration, making it</text>
  <text x="25" y="676" font-size="13" font-weight="bold" fill="#000000">perfect for mine operations.</text>
  <text x="25" y="694" font-size="10" font-weight="bold" fill="#595959">*Can be deployed in cloud with ease</text>

  <g transform="translate(270, 630)">
    <rect x="0" y="0" width="160" height="65" rx="6" fill="#FFE7BA" stroke="#FFC069"/>
    <text x="50" y="25" font-size="13" font-weight="bold" fill="#D46B08">File System</text>
    <text x="10" y="42" font-size="9" fill="#595959">File server to store and manage</text>
    <text x="10" y="55" font-size="9" fill="#595959">all the files securely</text>
  </g>

  <!-- AI COMPONENTS SECTION (SECTION 8) -->
  <g transform="translate(20, 715)">
    <!-- Number Circle 8 -->
    <circle cx="65" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="65" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">8</text>

    <!-- Black Pill Header -->
    <rect x="90" y="0" width="220" height="38" rx="19" fill="#000000"/>
    <text x="200" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF" letter-spacing="1">AI COMPONENTS</text>

    <!-- Python & TensorFlow Icons Stack -->
    <g transform="translate(20, 50)">
      <text x="10" y="25" font-size="20">🐍</text><text x="35" y="22" font-size="9" fill="#595959">Python</text>
      <text x="10" y="70" font-size="20">🟧</text><text x="35" y="67" font-size="9" fill="#595959">TensorFlow</text>
      <text x="10" y="115" font-size="20">📊</text><text x="35" y="112" font-size="9" fill="#595959">Scikit Learn</text>
    </g>

    <!-- AI Box 1 -->
    <g transform="translate(100, 50)">
      <rect x="0" y="0" width="340" height="60" rx="6" fill="#FFFBE6" stroke="#FFE58F"/>
      <text x="10" y="24" font-size="12" font-weight="bold" fill="#000000">AI-powered engine – Predicts coal production &amp;</text>
      <text x="10" y="42" font-size="12" font-weight="bold" fill="#000000">subsidence – Forecasts resource needs using real-time mine data.</text>
    </g>

    <!-- AI Box 2 -->
    <g transform="translate(100, 120)">
      <rect x="0" y="0" width="340" height="65" rx="6" fill="#FFFBE6" stroke="#FFE58F"/>
      <text x="10" y="24" font-size="12" font-weight="bold" fill="#000000">Decision Tree / Random Forest algorithm –</text>
      <text x="10" y="42" font-size="12" font-weight="bold" fill="#000000">Recommends workers for task assignment &amp; predicts</text>
      <text x="10" y="56" font-size="12" font-weight="bold" fill="#000000">roof sag risk.</text>
    </g>

    <!-- Vertical Blue Pill FLASK / FASTAPI -->
    <g transform="translate(450, 50)">
      <rect x="0" y="0" width="40" height="135" rx="20" fill="#69C0FF"/>
      <text x="20" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">F</text>
      <text x="20" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">L</text>
      <text x="20" y="65" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">A</text>
      <text x="20" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">S</text>
      <text x="20" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">K</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CENTER COLUMN: ADMIN (SECTION 3) & COAL MINES (SECTION 1 & 7) -->
  <!-- ========================================================================= -->

  <!-- SECTION 3: ADMIN (Top Center) -->
  <g transform="translate(630, 85)">
    <!-- Number Circle 3 -->
    <circle cx="215" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="215" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">3</text>

    <!-- ADMIN Blue Pill -->
    <rect x="240" y="5" width="90" height="30" rx="6" fill="#1890FF"/>
    <text x="285" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">ADMIN</text>

    <text x="345" y="25" font-size="14" font-weight="bold" fill="#000000">Efficient Task Handling with Web App for Admin</text>

    <!-- Admin Features Grid -->
    <g transform="translate(0, 45)">
      <rect x="0" y="0" width="80" height="50" rx="6" fill="#E6F7FF" stroke="#91D5FF"/>
      <text x="40" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">ERP</text>
      <text x="40" y="38" text-anchor="middle" font-size="8" fill="#595959">Existing ERP integrated</text>
    </g>

    <g transform="translate(90, 45)">
      <rect x="0" y="0" width="130" height="50" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Easy migration</text>
      <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">using Data Mapping</text>
    </g>

    <g transform="translate(230, 45)">
      <rect x="0" y="0" width="130" height="50" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="10" y="20" font-size="10" font-weight="bold" fill="#DC2626">⚠️ Real-Time</text>
      <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">Critical Alerts</text>
    </g>

    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="120" height="50" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Centralized Worker</text>
      <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">Management</text>
    </g>

    <g transform="translate(500, 45)">
      <rect x="0" y="0" width="130" height="50" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Verification of</text>
      <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">DGMS Report</text>
    </g>

    <!-- Zero Trust Ideology Column -->
    <g transform="translate(0, 105)">
      <rect x="0" y="0" width="80" height="110" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/>
      <text x="40" y="30" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Zero</text>
      <text x="40" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Trust</text>
      <text x="40" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Ideology</text>
      <text x="40" y="80" text-anchor="middle" font-size="7" fill="#595959">Intranet-only</text>
      <text x="40" y="92" text-anchor="middle" font-size="7" fill="#595959">access</text>
    </g>

    <!-- SMP Digitalization & Manual Logs -->
    <g transform="translate(90, 105)">
      <rect x="0" y="0" width="310" height="110" rx="6" fill="#FFF5E6" stroke="#FFD591"/>
      <text x="10" y="25" font-size="11" font-weight="bold" fill="#000000">The Safety Management ensures compliance with</text>
      <text x="10" y="40" font-size="11" font-weight="bold" fill="#000000">safety regulations.</text>
      
      <rect x="10" y="55" width="130" height="30" rx="15" fill="#FA8C16"/>
      <text x="75" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#FFFFFF">SMP Digitalization</text>

      <rect x="160" y="55" width="120" height="30" rx="6" fill="#D46B08"/>
      <text x="220" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#FFFFFF">Manual Logs</text>
    </g>

    <!-- OCR Box -->
    <g transform="translate(420, 105)">
      <rect x="0" y="0" width="120" height="110" rx="6" fill="#E6F7FF" stroke="#91D5FF"/>
      <text x="60" y="35" text-anchor="middle" font-size="18">📷 OCR</text>
      <text x="60" y="60" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Automated Text</text>
      <text x="60" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Extraction</text>
    </g>
  </g>

  <!-- SECTION 1: COAL MINES (Center) -->
  <g transform="translate(630, 320)">
    <!-- Main Coal Mines Dashed Container Box -->
    <rect x="0" y="0" width="410" height="140" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="2" stroke-dasharray="6,4"/>
    
    <!-- Circle Number 1 -->
    <circle cx="20" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="20" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">1</text>

    <text x="205" y="30" text-anchor="middle" font-size="22" font-weight="bold" fill="#000000" letter-spacing="1">COAL MINES</text>
    <text x="205" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Coal mines are split into sections consisting of a</text>
    <text x="205" y="70" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">supervisor and set of workers for smooth flow of</text>
    <text x="205" y="88" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">operation and safety</text>

    <!-- Mine Sections Illustration -->
    <g transform="translate(50, 100)">
      <rect x="0" y="0" width="80" height="28" rx="4" fill="#F5F5F5" stroke="#D9D9D9"/>
      <text x="40" y="18" text-anchor="middle" font-size="10" font-weight="bold">Section-1</text>

      <text x="100" y="18" text-anchor="middle" font-size="12" font-weight="bold">...</text>

      <rect x="120" y="0" width="80" height="28" rx="4" fill="#F5F5F5" stroke="#D9D9D9"/>
      <text x="160" y="18" text-anchor="middle" font-size="10" font-weight="bold">Section-n</text>

      <text x="230" y="18" font-size="11" font-weight="bold" fill="#1890FF">👤 Supervisor</text>
      <text x="310" y="18" font-size="11" font-weight="bold" fill="#52C41A">👥 Operators</text>
    </g>
  </g>

  <!-- DGMS Regulatory Box (Right Center) -->
  <g transform="translate(1060, 360)">
    <circle cx="35" cy="35" r="30" fill="#FFF0F6" stroke="#FFADD2" stroke-width="2"/>
    <text x="35" y="42" text-anchor="middle" font-size="20">🏛️</text>
    <text x="80" y="25" font-size="12" font-weight="bold" fill="#000000">DGMS Regulatory</text>
    <text x="80" y="40" font-size="11" fill="#595959">authority of mining sector in India</text>

    <text x="80" y="65" font-size="10" font-weight="bold" fill="#000000">DGMS Compliance Log Report Submission</text>

    <g transform="translate(240, 60)">
      <rect x="0" y="0" width="100" height="40" rx="6" fill="#FFF0F6" stroke="#FFADD2"/>
      <text x="50" y="24" text-anchor="middle" font-size="11" font-weight="bold" fill="#CF1322">Automatic PDF report</text>
    </g>
  </g>

  <!-- SECTION 7: DANGER DETECTING NODES & MINE MESH (Center Bottom) -->
  <g transform="translate(630, 480)">
    <!-- Circle Number 7 -->
    <circle cx="20" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="20" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">7</text>

    <!-- Node Deployment Graphic -->
    <g transform="translate(50, 0)">
      <rect x="0" y="0" width="140" height="120" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="70" y="20" text-anchor="middle" font-size="10" font-weight="bold">Node Deployment in Mines</text>
      <text x="70" y="38" text-anchor="middle" font-size="9" fill="#1890FF">ESP32 LoRa Mesh</text>
      <circle cx="70" cy="75" r="25" fill="#E6F7FF" stroke="#1890FF"/>
      <text x="70" y="80" text-anchor="middle" font-size="16">📡</text>
    </g>

    <!-- Danger Detecting Nodes Photo/Graphic Box -->
    <g transform="translate(210, 0)">
      <rect x="0" y="0" width="140" height="120" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
      <text x="70" y="20" text-anchor="middle" font-size="10" font-weight="bold">Danger Detecting Nodes</text>
      <rect x="20" y="30" width="100" height="75" rx="4" fill="#FEF2F2" stroke="#FCA5A5"/>
      <text x="70" y="70" text-anchor="middle" font-size="20">🚨</text>
    </g>

    <!-- Fallback & Internet Boxes -->
    <g transform="translate(370, 0)">
      <rect x="0" y="0" width="220" height="50" rx="6" fill="#FFFFFF" stroke="#1890FF"/>
      <text x="110" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#1890FF">🌐 Internet - Data sent</text>
      <text x="110" y="38" text-anchor="middle" font-size="11" font-weight="bold" fill="#1890FF">directly to the backend</text>

      <rect x="0" y="60" width="220" height="60" rx="6" fill="#E6F7FF" stroke="#91D5FF"/>
      <text x="110" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Fallback Mode</text>
      <text x="110" y="94" text-anchor="middle" font-size="10" font-weight="bold" fill="#DC2626">⚠️ No Internet - Data routed</text>
      <text x="110" y="108" text-anchor="middle" font-size="10" font-weight="bold" fill="#DC2626">via deployed nodes &amp; 1kHz siren</text>
    </g>

    <!-- E2E Encryption Banner -->
    <text x="280" y="-15" font-size="12" font-weight="bold" fill="#1890FF">E2E Encryption --------------------&gt;</text>
  </g>

  <!-- Underground & Open Cast Mine 3D Illustration Block (Center Bottom) -->
  <g transform="translate(630, 650)">
    <rect x="0" y="0" width="600" height="380" rx="10" fill="#F5F5F5" stroke="#D9D9D9"/>
    
    <!-- Mine Strata Illustration -->
    <path d="M 20 80 Q 300 40 580 80 L 580 360 L 20 360 Z" fill="#8C8C8C" opacity="0.2"/>
    <path d="M 20 180 Q 300 140 580 180 L 580 360 L 20 360 Z" fill="#434343" opacity="0.4"/>

    <text x="80" y="120" font-size="13" font-weight="bold" fill="#000000">Open Cast Mining</text>
    <text x="240" y="240" font-size="14" font-weight="bold" fill="#FFFFFF">Underground Mining</text>

    <!-- Safety Vest / Node Callout Box -->
    <g transform="translate(180, 270)">
      <rect x="0" y="0" width="240" height="90" rx="8" fill="#FFFFFF" stroke="#000000" stroke-width="1.5" filter="url(#cardShadow)"/>
      <text x="120" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Safety Vest / Sensor Node</text>
      <text x="120" y="44" text-anchor="middle" font-size="10" font-weight="bold" fill="#595959">transmit SpO2, tilt, sag and</text>
      <text x="120" y="60" text-anchor="middle" font-size="10" font-weight="bold" fill="#595959">fall detection data to the nearest</text>
      <text x="120" y="76" text-anchor="middle" font-size="10" font-weight="bold" fill="#595959">node for relay.</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- RIGHT COLUMN: SHIFT SUPERVISOR (SECTION 5) & SHIFT OPERATORS (SECTION 6) -->
  <!-- ========================================================================= -->

  <!-- SECTION 5: SHIFT SUPERVISOR (Top Right) -->
  <g transform="translate(1260, 85)">
    <!-- Number Circle 5 -->
    <circle cx="55" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="55" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">5</text>

    <!-- Black Pill Header -->
    <rect x="80" y="0" width="210" height="38" rx="19" fill="#000000"/>
    <text x="185" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF" letter-spacing="1">Shift Supervisor</text>

    <text x="310" y="22" font-size="22" font-weight="bold" fill="#000000">Web/Desktop App</text>
    <text x="310" y="38" font-size="14" font-weight="bold" fill="#595959">Cross-Platform</text>

    <!-- Desktop Monitor Graphic -->
    <g transform="translate(40, 50)">
      <rect x="0" y="0" width="280" height="170" rx="8" fill="#1F2937" stroke="#374151" stroke-width="3"/>
      <!-- Screen Inner -->
      <rect x="10" y="10" width="260" height="150" rx="4" fill="#FFFFFF"/>
      <rect x="10" y="10" width="260" height="20" fill="#F3F4F6"/>
      <circle cx="22" cy="20" r="3" fill="#EF4444"/><circle cx="32" cy="20" r="3" fill="#F59E0B"/><circle cx="42" cy="20" r="3" fill="#10B981"/>
      <text x="140" y="23" text-anchor="middle" font-size="8" font-weight="bold" fill="#4B5563">MineGuard AI Command Center</text>

      <!-- Dashboard Elements Preview -->
      <rect x="20" y="40" width="240" height="20" fill="#EEF2FF" rx="3"/>
      <rect x="20" y="70" width="115" height="80" fill="#F9FAFB" stroke="#E5E7EB" rx="3"/>
      <rect x="145" y="70" width="115" height="80" fill="#F9FAFB" stroke="#E5E7EB" rx="3"/>
      
      <!-- Monitor Stand -->
      <path d="M 120 170 L 160 170 L 170 200 L 110 200 Z" fill="#374151"/>
      <rect x="90" y="200" width="100" height="10" rx="3" fill="#1F2937"/>
    </g>

    <!-- Tech Icons Grid (Right of Monitor) -->
    <g transform="translate(340, 50)">
      <g transform="translate(0,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#E6F7FF" stroke="#91D5FF"/><text x="20" y="25" text-anchor="middle" font-size="14">⚛️</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">React</text></g>
      <g transform="translate(50,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/><text x="20" y="25" text-anchor="middle" font-size="14">🎨</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Shadcn</text></g>
      <g transform="translate(100,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#E6F7FF" stroke="#91D5FF"/><text x="20" y="25" text-anchor="middle" font-size="12" font-weight="bold" fill="#1890FF">TS</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">TypeScript</text></g>
      
      <g transform="translate(0,50)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#F3E8FF" stroke="#D8B4FE"/><text x="20" y="25" text-anchor="middle" font-size="14">🔮</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Redux</text></g>
      <g transform="translate(50,50)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/><text x="20" y="25" text-anchor="middle" font-size="14">🗺️</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Mapbox</text></g>
      <g transform="translate(100,50)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/><text x="20" y="25" text-anchor="middle" font-size="14">⚡</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Socket.io</text></g>
    </g>

    <!-- Feature Callout Boxes (Below Monitor) -->
    <g transform="translate(40, 270)">
      <g transform="translate(0,0)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Predictive Simulation</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">Engine</text>
      </g>

      <g transform="translate(140,0)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Real-time</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">IoT logs</text>
      </g>

      <g transform="translate(280,0)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Supervisors can</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">view/Edit Round Plans</text>
      </g>

      <g transform="translate(420,0)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Supervisors do</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">Shift Allotment</text>
      </g>

      <g transform="translate(280,65)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">AI powered assistant</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">to assist Supervisor</text>
      </g>

      <g transform="translate(420,65)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#D9D9D9"/>
        <text x="10" y="20" font-size="10" font-weight="bold" fill="#000000">Supervisors approve &amp;</text>
        <text x="10" y="34" font-size="10" font-weight="bold" fill="#000000">Submit Shift-Handovers</text>
      </g>
    </g>
  </g>

  <!-- SECTION 6: SHIFT OPERATORS (Bottom Right) -->
  <g transform="translate(1260, 520)">
    <!-- Number Circle 6 -->
    <circle cx="215" cy="20" r="14" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
    <text x="215" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#000000">6</text>

    <!-- Black Pill Header -->
    <rect x="240" y="0" width="240" height="38" rx="19" fill="#000000"/>
    <text x="360" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF" letter-spacing="1">SHIFT OPERATORS</text>

    <text x="50" y="70" font-size="22" font-weight="bold" fill="#000000">Mobile App</text>
    <text x="50" y="88" font-size="14" font-weight="bold" fill="#595959">Cross-Platform</text>

    <!-- Mobile Phone Graphic Mockup -->
    <g transform="translate(50, 105)">
      <rect x="0" y="0" width="170" height="320" rx="20" fill="#1F2937" stroke="#374151" stroke-width="3"/>
      <rect x="8" y="10" width="154" height="300" rx="14" fill="#FFFFFF"/>
      <!-- Mobile UI Header -->
      <rect x="8" y="10" width="154" height="40" rx="14" fill="#F3F4F6"/>
      <text x="20" y="35" font-size="10" font-weight="bold" fill="#000000">MineGuard AI</text>
      <!-- Mobile Content Lines -->
      <rect x="18" y="60" width="134" height="40" fill="#EEF2FF" rx="4"/>
      <rect x="18" y="110" width="134" height="60" fill="#FEF2F2" rx="4"/>
      <rect x="18" y="180" width="134" height="60" fill="#F9FAFB" stroke="#E5E7EB" rx="4"/>
    </g>

    <!-- Tech Icons (Right of Mobile) -->
    <g transform="translate(240, 105)">
      <g transform="translate(0,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#F5F5F5" stroke="#D9D9D9"/><text x="20" y="25" text-anchor="middle" font-size="14">🗄️</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">SQLite</text></g>
      <g transform="translate(50,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#E6F7FF" stroke="#91D5FF"/><text x="20" y="25" text-anchor="middle" font-size="14">🧊</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Bloc</text></g>
      <g transform="translate(100,0)"><rect x="0" y="0" width="40" height="40" rx="6" fill="#E6F7FF" stroke="#91D5FF"/><text x="20" y="25" text-anchor="middle" font-size="14">💙</text><text x="20" y="36" text-anchor="middle" font-size="7" font-weight="bold">Flutter</text></g>
    </g>

    <!-- Features Box (Right of Mobile) -->
    <g transform="translate(240, 160)">
      <rect x="0" y="0" width="280" height="235" rx="8" fill="#FFFFFF" stroke="#D9D9D9"/>
      
      <g transform="translate(15, 15)">
        <text x="0" y="15" font-size="16">📋</text>
        <text x="30" y="12" font-size="11" font-weight="bold" fill="#000000">Quick summary of shifts,</text>
        <text x="30" y="26" font-size="11" font-weight="bold" fill="#000000">tasks, issues, and alerts</text>
      </g>

      <g transform="translate(15, 70)">
        <text x="0" y="15" font-size="16">📝</text>
        <text x="30" y="12" font-size="11" font-weight="bold" fill="#000000">Log details about tasks,</text>
        <text x="30" y="26" font-size="11" font-weight="bold" fill="#000000">issues, alerts during rounds</text>
      </g>

      <g transform="translate(15, 125)">
        <text x="0" y="15" font-size="16">🗣️</text>
        <text x="30" y="12" font-size="11" font-weight="bold" fill="#000000">Support for major Indian</text>
        <text x="30" y="26" font-size="11" font-weight="bold" fill="#000000">languages</text>
      </g>

      <g transform="translate(15, 180)">
        <text x="0" y="15" font-size="16">🎙️</text>
        <text x="30" y="12" font-size="11" font-weight="bold" fill="#000000">Smart voice controls for</text>
        <text x="30" y="26" font-size="11" font-weight="bold" fill="#000000">assistance</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- BOTTOM FOOTER BAR -->
  <!-- ========================================================================= -->
  <rect x="0" y="1045" width="1920" height="35" fill="#1890FF"/>
  <text x="960" y="1068" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">MineGuard AI - @SIH Idea Submission</text>
  <text x="1890" y="1068" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">3</text>

</svg>'''

    output_svg = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\mineguard_ai_technical_approach.svg"
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Exact senior style SVG generated at: {output_svg}")

if __name__ == '__main__':
    generate_exact_senior_svg()
