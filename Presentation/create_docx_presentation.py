import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Segoe UI'
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = RGBColor(27, 54, 93) # Deep Navy
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Segoe UI'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(44, 82, 130) # Dark Blue
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Segoe UI'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(197, 48, 48) # Crimson Accent
    return p

def add_bullet(doc, bold_prefix, text, level=0):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)
    if level > 0:
        p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
    
    if bold_prefix:
        r_bold = p.add_run(bold_prefix + " ")
        r_bold.font.name = 'Calibri'
        r_bold.font.size = Pt(11)
        r_bold.font.bold = True
        r_bold.font.color.rgb = RGBColor(45, 55, 72)
    
    r_text = p.add_run(text)
    r_text.font.name = 'Calibri'
    r_text.font.size = Pt(11)
    r_text.font.color.rgb = RGBColor(45, 55, 72)
    return p

def add_callout(doc, title, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F4F8") # Subtle blue tint
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Border styling (Left thick navy border)
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="1B365D"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    
    r_title = p.add_run(title + "\n")
    r_title.font.name = 'Segoe UI'
    r_title.font.size = Pt(11)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(27, 54, 93)
    
    r_text = p.add_run(text)
    r_text.font.name = 'Calibri'
    r_text.font.size = Pt(10.5)
    r_text.font.italic = True
    r_text.font.color.rgb = RGBColor(45, 55, 72)
    
    # Add empty paragraph after table for spacing
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(6)

def build_docx():
    doc = Document()
    
    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Document Header
    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(2)
    r_main = p_main.add_run("MINEGUARD AI")
    r_main.font.name = 'Segoe UI'
    r_main.font.size = Pt(26)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(27, 54, 93)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(18)
    r_sub = p_sub.add_run("SIH 2026 Presentation Content Document (Slide 1 to Slide 6)\nTeam MineNova6 | Problem Statement ID: SIH26025")
    r_sub.font.name = 'Segoe UI'
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # =========================================================================
    # SLIDE 1
    # =========================================================================
    add_heading_1(doc, "SLIDE 1: Title Slide (Official SIH 2026 Format)")
    add_callout(doc, "📌 Slide Header & Banner", "SMART INDIA HACKATHON 2026 — Official Idea Submission Deck")
    
    add_bullet(doc, "Problem Statement ID:", "SIH26025")
    add_bullet(doc, "Problem Statement Title:", "Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India")
    add_bullet(doc, "Theme:", "Smart Automation / Safety & Security / Disaster Management")
    add_bullet(doc, "PS Category:", "Software & Hardware (Hybrid IoT-AI System)")
    add_bullet(doc, "Team ID:", "SIH2026-MINENOVA6")
    add_bullet(doc, "Team Name (Registered on Portal):", "MineNova6")
    add_bullet(doc, "Team Members & Roles:", "Shareque (Team Lead & System Architect), Monika (Geotechnical Research & Presentation), Aditya (UI/UX Lead), Farhan (Frontend React), Atharva (Backend FastAPI), Affan (AI/ML Lead)")

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # =========================================================================
    # SLIDE 2
    # =========================================================================
    add_heading_1(doc, "SLIDE 2: Proposed Solution & \"Why We Stand Out\"")
    add_heading_2(doc, "Section A: Proposed Solution Overview")
    
    add_callout(doc, "💡 Core Executive Summary", "MineGuard AI is an ultra-low-cost, wireless IoT-AI strata monitoring system that provides real-time mine subsidence prediction and instant early warnings for underground coal mines in India.")

    add_bullet(doc, "• Wireless LoRa Sensor Mesh:", "ESP32 LoRa (868MHz) nodes monitor roof tilt, sag displacement, crack growth, and stress without fragile cabling.")
    add_bullet(doc, "• AI Subsidence Predictor:", "Random Forest engine uses 5-min rate-of-change velocity (Δdisp/Δt) to predict Stage-1 micro-sagging.")
    add_bullet(doc, "• React Web Command Center:", "Provides interactive underground seam maps, rolling 60 FPS charts, and live emergency simulation.")
    add_bullet(doc, "• Dual Edge & Cloud Sirens:", "Triggers 1kHz local sirens at mine face independently during outages, plus instant web alerts.")
    add_bullet(doc, "• Tailored for Indian Coalfields:", "Replaces reactive, static cabled monitoring with predictive early warnings for Jharia & Raniganj mines.")
    add_bullet(doc, "• 100% Functional MVP:", "Fully validated with hardware LoRa telemetry, FastAPI backend, and real-time dashboard sync.")

    add_heading_2(doc, "Section B: Why We Stand Out? (4 Key Differentiators)")
    
    # 2x2 Table for Why We Stand Out
    t_out = doc.add_table(rows=2, cols=2)
    t_out.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_out.autofit = False
    
    col_widths = [Inches(3.3), Inches(3.3)]
    
    cards_data = [
        ("🧠 Velocity-Weighted AI Engine", "Predicts roof sag in Stage 1 using 5-minute rate-of-change velocity (Δdisp/Δt, Δtilt/Δt). MAE: 1.27, R²: 0.9969."),
        ("💰 98.8% Cost Reduction vs Legacy", "₹1,590/node ($19 USD) vs ₹50,000+ cabled legacy sensors. Complete panel setup for ₹11,990 vs ₹10+ Lakhs."),
        ("📡 Non-Line-Of-Sight LoRa Telemetry", "868MHz Chirp Spread Spectrum penetrates up to 2km solid rock/coal strata without optical line of sight or cabling."),
        ("🚨 Fail-Safe Dual Edge Siren Resilience", "ESP32 MCU fires local piezo sirens on GPIO 12/13 automatically during central internet/power outages.")
    ]

    for idx, (title, desc) in enumerate(cards_data):
        r_idx = idx // 2
        c_idx = idx % 2
        cell = t_out.cell(r_idx, c_idx)
        cell.width = col_widths[c_idx]
        set_cell_background(cell, "F7FAFC")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        
        tcPr = cell._element.get_or_add_tcPr()
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/><w:left w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/><w:right w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/><w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/></w:tcBorders>')
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        r1 = p.add_run(title + "\n")
        r1.font.name = 'Segoe UI'
        r1.font.size = Pt(10.5)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(27, 54, 93)
        
        r2 = p.add_run(desc)
        r2.font.name = 'Calibri'
        r2.font.size = Pt(10)
        r2.font.color.rgb = RGBColor(74, 85, 104)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # =========================================================================
    # SLIDE 3
    # =========================================================================
    add_heading_1(doc, "SLIDE 3: Technical Approach & System Architecture")
    
    add_callout(doc, "🔄 End-to-End Data Pipeline", "[Underground Seam Sensors] ──(868MHz LoRa)──► [ESP32 Gateway Hub] ──(HTTP POST)──► [FastAPI Backend] ──► [Random Forest ML] ──► [React Dashboard & Siren Alarm]")

    add_heading_2(doc, "1. Hardware & Perception Layer")
    add_bullet(doc, "Microcontroller & Radio:", "ESP32 (32-bit dual-core 240MHz MCU) + SX1276 LoRa 868MHz Chirp Spread Spectrum transceiver (2km strata penetration).")
    add_bullet(doc, "MPU6050 Motion Sensor:", "6-axis Gyroscope & Accelerometer measuring roof tilt (θx, θy), angular rate, and vibration acceleration.")
    add_bullet(doc, "Linear String Potentiometer:", "Continuous roof sag displacement (0 - 50 mm) and crack growth width tracking.")
    add_bullet(doc, "HX711 + Load Cell:", "Hydraulic prop stress and strata compression pressure measurement (0 - 200 kN).")
    add_bullet(doc, "DHT22 Sensor:", "Ambient underground temperature and relative humidity monitoring.")

    add_heading_2(doc, "2. Backend & AI Analytics Layer")
    add_bullet(doc, "FastAPI Framework:", "Python async ASGI event loop with Pydantic schema validation and WebSocket real-time broadcast engine.")
    add_bullet(doc, "Database Architecture:", "SQLAlchemy ORM configured with SQLite for edge testing, PostgreSQL & TimescaleDB ready for cloud production.")
    add_bullet(doc, "Machine Learning Engine:", "scikit-learn Random Forest Regressor & Classifier evaluating 10 telemetric parameters.")
    add_bullet(doc, "Key AI Feature Acceleration:", "Places 42% predictive weight on 5-minute velocity rates of change (Δdisp/Δt, Δtilt/Δt) to detect pre-failure roof sagging.")
    add_bullet(doc, "Model Performance:", "Mean Absolute Error (MAE): 1.27 | R² Score: 0.9969.")

    add_heading_2(doc, "3. Frontend & Presentation Layer")
    add_bullet(doc, "Web Framework:", "React 18 + Vite with Tailwind CSS (Glassmorphism dark theme default with light mode toggle).")
    add_bullet(doc, "Visualizations:", "Recharts rolling 60 FPS line charts, Leaflet geospatial underground seam map with pulsing danger rings.")
    add_bullet(doc, "Live SIH Simulator:", "Interactive Emergency Simulator allows judges to trigger a 'Subsidence Event' live during presentation.")

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # =========================================================================
    # SLIDE 4
    # =========================================================================
    add_heading_1(doc, "SLIDE 4: Feasibility, Viability & Challenges vs Mitigations")
    
    add_heading_2(doc, "Part 1: 4-Dimensional Feasibility Analysis")
    add_bullet(doc, "Economic Feasibility:", "₹1,590 ($19 USD) per sensor node; ₹11,990 total for 6 nodes + gateway (98.8% cost saving vs ₹10+ Lakhs cabled systems). Immediate ROI (<1 month).")
    add_bullet(doc, "Technical Feasibility:", "Low-power 3.3V DC logic; 3.7V LiFePO4 battery lasts 6+ months; 868MHz LoRa penetrates solid coal/rock strata without optical line-of-sight.")
    add_bullet(doc, "Operational Feasibility:", "Simple clamp-on roof bolting installation requires zero specialized technical training for mine workers.")
    add_bullet(doc, "Regulatory Feasibility:", "Automates compliance checks for DGMS (Directorate General of Mines Safety) Strata Management Plans (SMP).")

    add_heading_2(doc, "Part 2: Technical Challenges & Mitigation Matrix")
    
    # Table for Challenges & Mitigations
    t_chal = doc.add_table(rows=5, cols=3)
    t_chal.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_chal.autofit = False
    
    headers = ["#", "Challenge in Underground Mines", "Solution & Technical Mitigation Strategy"]
    w_list = [Inches(0.5), Inches(2.6), Inches(3.5)]
    
    hdr_cells = t_chal.rows[0].cells
    for i, text in enumerate(headers):
        hdr_cells[i].width = w_list[i]
        set_cell_background(hdr_cells[i], "1B365D")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Segoe UI'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    chal_data = [
        ("1", "Explosive Methane / Coal Dust Atmosphere", "IP67 flameproof polycarbonate enclosure complying with DGMS Intrinsically Safe (IS Ex 'd') standards."),
        ("2", "Severe RF Signal Attenuation through Solid Rock", "868MHz Chirp Spread Spectrum (CSS) frequency modulation designed for non-line-of-sight penetration with multi-hop relaying."),
        ("3", "Central Internet / Server Outages", "Edge Failover Redundancy — ESP32 Gateway independently fires GPIO 12/13 piezo sirens & logs data locally over USB/SD buffer."),
        ("4", "Sensor Calibration Drift & Dust Exposure", "Auto-zero calibration routines on startup combined with protective IP65 dust-filtering membranes.")
    ]

    for row_idx, data_tuple in enumerate(chal_data, start=1):
        row_cells = t_chal.rows[row_idx].cells
        bg_color = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data_tuple):
            row_cells[col_idx].width = w_list[col_idx]
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=100, right=100)
            
            tcPr = row_cells[col_idx]._element.get_or_add_tcPr()
            borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:left w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/></w:tcBorders>')
            tcPr.append(borders)
            
            p = row_cells[col_idx].paragraphs[0]
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(45, 55, 72)
            if col_idx == 0:
                r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # =========================================================================
    # SLIDE 5
    # =========================================================================
    add_heading_1(doc, "SLIDE 5: Impacts, Stakeholder Workflow & UN SDGs")
    
    add_heading_2(doc, "1. Multi-Sector Impacts & Benefits")
    add_bullet(doc, "Economic Benefits:", "Saves coal mining companies multi-crores in damaged hydraulic supports, continuous miners, mine closure penalties, and legal compensation.")
    add_bullet(doc, "Social Benefits:", "Protects 300,000+ underground miners in India by eliminating unpredicted roof falls during depillaring, fostering a zero-casualty safety culture.")
    add_bullet(doc, "Environmental & Regulatory Benefits:", "Prevents surface land fissuring, groundwater table depletion, and environmental degradation above mined-out panels while satisfying DGMS SMP guidelines.")

    add_heading_2(doc, "2. End-to-End Stakeholder Impact Flow")
    add_bullet(doc, "Underground Miner / Worker:", "Receives instant 1kHz piezo siren alarm at the mine face, providing vital minutes for safe evacuation.")
    add_bullet(doc, "Shift Safety Officer:", "Receives real-time risk alert notification on mobile/handheld device with exact seam location coordinates.")
    add_bullet(doc, "Strata Control Engineer:", "Analyzes 10-parameter AI graphs and velocity trends to plan preventive roof bolting and prop reinforcement.")
    add_bullet(doc, "DGMS & Mine Management:", "Accesses automated, tamper-proof digital log reports for regulatory compliance and safety audits.")

    add_heading_2(doc, "3. UN Sustainable Development Goals (SDGs) & National Targets")
    add_bullet(doc, "SDG 3 (Good Health & Well-Being):", "Directly targets zero fatal casualties and injuries from underground roof collapses.")
    add_bullet(doc, "SDG 8 (Decent Work & Economic Growth):", "Ensures safer working conditions and uninterrupted underground coal production.")
    add_bullet(doc, "SDG 9 (Industry, Innovation & Infrastructure):", "Deploys state-of-the-art IoT and ML innovation in legacy mining operations.")
    add_bullet(doc, "SDG 12 (Responsible Consumption & Production):", "Prevents catastrophic structural damage to mining panels and equipment.")
    add_bullet(doc, "National Production Goal:", "Supports India's target of producing 1.5 Billion Tons of Coal by 2030 with high safety standards.")

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # =========================================================================
    # SLIDE 6
    # =========================================================================
    add_heading_1(doc, "SLIDE 6: Research, Market Economics & References")
    
    add_heading_2(doc, "1. Market Size & Addressable Market (TAM / SAM / SOM)")
    add_bullet(doc, "Total Addressable Market (TAM):", "₹15,000 Crore ($1.8 Billion USD) — Global and Indian Underground Mining Safety & Telemetry Market.")
    add_bullet(doc, "Serviceable Available Market (SAM):", "₹4,500 Crore — CIL Subsidiaries (ECL, BCCL, CCL, SECL, WCL) & SCCL Underground Coal Mines.")
    add_bullet(doc, "Serviceable Obtainable Market (SOM):", "₹450 Crore — High-risk depillaring and longwall extraction panels in Indian coal seams.")

    add_heading_2(doc, "2. Unit Economics & BOM Cost Breakdown (Per Node = ₹1,590)")
    
    # Table for BOM Cost Breakdown
    t_bom = doc.add_table(rows=7, cols=3)
    t_bom.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_bom.autofit = False
    
    bom_headers = ["Component", "Specification", "Cost (INR)"]
    bom_widths = [Inches(2.5), Inches(3.0), Inches(1.1)]
    
    bom_hdr_cells = t_bom.rows[0].cells
    for i, text in enumerate(bom_headers):
        bom_hdr_cells[i].width = bom_widths[i]
        set_cell_background(bom_hdr_cells[i], "1B365D")
        set_cell_margins(bom_hdr_cells[i], top=90, bottom=90, left=100, right=100)
        p = bom_hdr_cells[i].paragraphs[0]
        r = p.add_run(text)
        r.font.name = 'Segoe UI'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    bom_data = [
        ("ESP32 Microcontroller", "32-bit Dual-Core 240MHz MCU with Wi-Fi/BLE", "₹450"),
        ("SX1276 LoRa Module", "868MHz Chirp Spread Spectrum Transceiver", "₹350"),
        ("MPU6050 Motion Sensor", "6-Axis Gyroscope & Accelerometer", "₹150"),
        ("Linear String Potentiometer", "Roof Displacement & Sag Sensor (0-50mm)", "₹300"),
        ("HX711 + Load Cell", "200kN Prop Load Stress Amplifier & Sensor", "₹250"),
        ("Housing & Miscellaneous", "IP67 Flameproof Polycarbonate Enclosure & PCB", "₹90")
    ]

    for row_idx, data_tuple in enumerate(bom_data, start=1):
        row_cells = t_bom.rows[row_idx].cells
        bg_color = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data_tuple):
            row_cells[col_idx].width = bom_widths[col_idx]
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=100, right=100)
            
            tcPr = row_cells[col_idx]._element.get_or_add_tcPr()
            borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:left w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/></w:tcBorders>')
            tcPr.append(borders)
            
            p = row_cells[col_idx].paragraphs[0]
            r = p.add_run(text)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(45, 55, 72)
            if col_idx == 0:
                r.font.bold = True

    add_heading_2(doc, "3. References & Live Prototype Links")
    add_bullet(doc, "DGMS Technical Circulars:", "Directorate General of Mines Safety guidelines on Strata Management & Convergence Monitoring.")
    add_bullet(doc, "CSIR-CIMFR Research:", "Central Institute of Mining and Fuel Research studies on Bord-and-Pillar Depillaring Stress Dynamics.")
    add_bullet(doc, "IS/IEC 60079 Standard:", "Explosive Atmospheres & Intrinsically Safe (IS Ex 'd') Electrical Apparatus Compliance.")
    add_bullet(doc, "Hardware Datasheet:", "Semtech SX1276 LoRa 868MHz Chirp Spread Spectrum Technical Manual.")
    add_bullet(doc, "Live Web Dashboard:", "https://mineguard-ai.vercel.app")
    add_bullet(doc, "Official GitHub Repository:", "https://github.com/sharequesyed/MineGuard-AI")

    # Output path
    output_docx = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Presentation_Content.docx"
    try:
        doc.save(output_docx)
        print(f"Docx file successfully created at: {output_docx}")
    except PermissionError:
        output_docx_alt = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Presentation_Content_v2.docx"
        doc.save(output_docx_alt)
        print(f"Original file was open/locked. Docx file saved at: {output_docx_alt}")

if __name__ == '__main__':
    build_docx()
