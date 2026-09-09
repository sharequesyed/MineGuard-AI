import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

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
    p.paragraph_format.space_before = Pt(18)
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
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
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
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_image_reference(doc, image_path, caption):
    if os.path.exists(image_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        
        run_img = p_img.add_run()
        run_img.add_picture(image_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        
        run_cap = p_cap.add_run(f"Figure Reference: {caption}")
        run_cap.font.name = 'Segoe UI'
        run_cap.font.size = Pt(9.5)
        run_cap.font.italic = True
        run_cap.font.color.rgb = RGBColor(100, 116, 139)

def build_docx():
    doc = Document()
    
    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Document Title Header
    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(2)
    r_main = p_main.add_run("MINEGUARD AI — SIH 2026 PRESENTATION CONTENT")
    r_main.font.name = 'Segoe UI'
    r_main.font.size = Pt(24)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(27, 54, 93)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    r_sub = p_sub.add_run("Official Slide-by-Slide Deck Content Document for Napkin AI & Idea Submission\nTeam Name: MineNova6 | Problem Statement ID: SIH26025")
    r_sub.font.name = 'Segoe UI'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    assets_dir = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\assets"

    # =========================================================================
    # SLIDE 1
    # =========================================================================
    add_heading_1(doc, "SLIDE 1: Title Slide (Official SIH 2026 Format)")
    add_callout(doc, "📌 Slide Header", "SMART INDIA HACKATHON 2026 — Official Idea Submission Deck")
    
    add_bullet(doc, "Problem Statement ID:", "SIH26025")
    add_bullet(doc, "Problem Statement Title:", "Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India")
    add_bullet(doc, "Theme:", "Smart Automation / Safety & Security / Disaster Management")
    add_bullet(doc, "PS Category:", "Software & Hardware (Hybrid IoT-AI Strata Monitoring System)")
    add_bullet(doc, "Team ID:", "SIH2026-MINENOVA6")
    add_bullet(doc, "Team Name (Registered on Portal):", "MineNova6")
    add_bullet(doc, "Team Members & Key Roles:", "Shareque (Team Leader & System Architect), Monika (Geotechnical Research & Presentation Lead), Aditya (UI/UX Design Lead), Farhan (Frontend React Lead), Atharva (Backend FastAPI Lead), Affan (AI/ML & Data Lead)")

    img1 = os.path.join(assets_dir, "slide1_title_hero.png")
    add_image_reference(doc, img1, "Slide 1 Official SIH Title Banner & Project Credentials Graphic")

    # =========================================================================
    # SLIDE 2
    # =========================================================================
    add_heading_1(doc, "SLIDE 2: Solution, Prototype & Why We Stand Out")
    
    add_heading_2(doc, "Section 1: SOLUTION OVERVIEW")
    add_callout(doc, "💡 Core Executive Summary", "MineGuard AI is a complete mining operations & strata safety software combining Web Command Center, Cross-Platform Mobile App, and ESP32 LoRa wireless hardware for a smoother, safer, and more efficient mining process.")

    add_bullet(doc, "• Web Dashboard for Supervisors:", "Monitors real-time strata activity (tilt, displacement, stress), plans rounds, tracks task execution, and manages seamless shift handovers.")
    add_bullet(doc, "• Mobile App for Shift Workers:", "Allows miners to view shift details, receive instant early warning siren alerts, and log events like issues, structural cracks, or injuries.")
    add_bullet(doc, "• AI-Powered Assistant:", "Suggests intelligent round planning, predicts subsidence risks, and assigns the right personnel to handle detected issues.")
    add_bullet(doc, "• Admin Dashboard & DGMS Compliance:", "Provides easy integration with existing DGMS-compliant Strata Management Plans (SMP) and paper logbooks.")
    add_bullet(doc, "• OCR & Smart Voice Digitization:", "Scans paper logbooks and converts them into template-based digital forms; supports smart voice controls in 10+ Indian languages.")
    add_bullet(doc, "• Easy ERP Data Migration:", "Enables seamless data migration from existing enterprise systems using automated data mapping and REST APIs.")
    add_bullet(doc, "• Solution Status:", "MineGuard AI is 85% completed; testing and field validation are ongoing.")

    add_heading_2(doc, "Section 2: PROTOTYPE & ECOSYSTEM BREAKDOWN")
    add_bullet(doc, "• Cross-Platform Mobile App (Operator App):", "Designed for field workers in coal mines. Supports 10+ Indian languages with an easy UI/UX, hassle-free task logging, smart voice controls, and edge siren alarms.")
    add_bullet(doc, "• Safety Nodes & Hardware Vest:", "Wireless IoT devices deployed across underground coal seams and integrated into safety vests. Monitors strata tilt (MPU6050), displacement (string pot), prop load stress (load cell), and worker vitals.")
    add_bullet(doc, "• Supervisor Desktop Command Center:", "Designed for mine supervisors and admin. Features interactive Leaflet underground seam maps, real-time 60 FPS Recharts graphs, OCR log scanner, and automated PDF export.")

    add_heading_2(doc, "Section 3: WHY WE STAND OUT? (4 Core Pillars)")
    
    t_out = doc.add_table(rows=2, cols=2)
    t_out.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_out.autofit = False
    col_widths = [Inches(3.3), Inches(3.3)]
    
    cards_data = [
        ("🧠 Predictive Simulation & AI Engine", "Supervisors can simulate mine operations and estimate safety needs. Random Forest engine places 42% weight on 5-min velocity rates (Δdisp/Δt) to detect pre-collapse sagging (MAE: 1.27, R²: 0.9969)."),
        ("⚡ Optimizing Workflows & Resources", "Our AI engine predicts strata hazards, plans shift schedules, assigns tasks to qualified miners, and optimizes equipment resources for zero-downtime safety."),
        ("🐳 Cross-Platform Solution with Docker", "Docker containerization guarantees consistent performance, security, and instant deployment across cloud servers, local edge hubs, and desktop environments."),
        ("📡 Scalable IoT Deployment without Internet", "Our ESP32 SX1276 LoRa devices (868MHz) form a peer-to-peer mesh network, ensuring continuous cross-validation and safety alerts even deep underground with zero cellular network.")
    ]

    for idx, (title, desc) in enumerate(cards_data):
        r_idx = idx // 2
        c_idx = idx % 2
        cell = t_out.cell(r_idx, c_idx)
        cell.width = col_widths[c_idx]
        set_cell_background(cell, "F8FAFC")
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

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    img2 = os.path.join(assets_dir, "slide2_prototype_diagram.png")
    add_image_reference(doc, img2, "Slide 2 MineGuard AI Solution Prototype & 3-Panel Ecosystem Diagram")

    # =========================================================================
    # SLIDE 3
    # =========================================================================
    add_heading_1(doc, "SLIDE 3: Technical Approach & End-to-End Architecture")
    
    add_callout(doc, "🔄 System Data Flow Pipeline", "[Underground Coal Mine Seams] ──(868MHz LoRa Mesh)──► [LoRa Gateway / Node Relays] ──(HTTP / WS)──► [FastAPI Docker Backend] ──► [Random Forest AI Engine] ──► [React Supervisor Web App & Mobile Siren Alarms]")

    add_heading_2(doc, "1. Coal Mines & Sensor Network Deployment")
    add_bullet(doc, "• Mine Section Partitioning:", "Coal mines are split into defined sections consisting of a supervisor and set of workers for smooth operation and safety.")
    add_bullet(doc, "• Node Deployment in Mines:", "Wireless ESP32 sensor nodes equipped with MPU6050 (roof tilt & vibration), linear string potentiometers (sag displacement & crack width), and HX711 + load cells (hydraulic prop pressure).")
    add_bullet(doc, "• Fail-Safe Communication Fallback:", "Internet Available -> Data sent directly to backend; No Internet -> Data routed via deployed LoRa mesh nodes (868MHz CSS).")
    add_bullet(doc, "• Worker Safety Vest Integration:", "Transmits SpO2, body temperature, and fall/vibration detection data to the nearest node for relay.")
    add_bullet(doc, "• End-to-End Encryption:", "All telemetric data packets encrypted using AES-256 before transmission over LoRa.")

    add_heading_2(doc, "2. Manual Logs & SMP Digitalization Layer")
    add_bullet(doc, "• Manual Paper Logbooks:", "Track daily operations, strata observations, and important mine events.")
    add_bullet(doc, "• Automated OCR Text Extraction:", "Scans physical logbook pages using Tesseract / EasyOCR and maps extracted text into standardized digital forms.")
    add_bullet(doc, "• Smart Voice Multi-Language Input:", "Field operators log issues via voice in regional Indian languages (Hindi, Bengali, Odia, etc.).")
    add_bullet(doc, "• DGMS Compliance Reports:", "Generates tamper-proof digital Strata Management Plan (SMP) reports with admin verification.")

    add_heading_2(doc, "3. Admin & Web Application Layer")
    add_bullet(doc, "• Web App for Admin:", "Efficient task handling, central worker management, ERP data migration, real-time critical alerts, and DGMS report submission verification.")
    add_bullet(doc, "• Zero Trust Security Ideology:", "Intranet-only access blocking unauthorized external connections; strict role-based access controls.")

    add_heading_2(doc, "4. Backend Architecture (Docker Container)")
    add_bullet(doc, "• API Gateway & General Server:", "Nginx reverse proxy + Python FastAPI async ASGI server providing high-throughput REST API endpoints.")
    add_bullet(doc, "• Database Infrastructure:", "Time-series database (SQLite for edge / TimescaleDB for cloud) storing high-frequency sensor streams; Relational DB storing worker, shift, and audit records.")
    add_bullet(doc, "• Microservices Engine:", "Decoupled IoT Service (packet parsing), AI Service (prediction engine), and General Server (auth & business logic).")
    add_bullet(doc, "• Message Bus & Streaming:", "WebSocket Engine / Kafka message bus + stream processing for real-time telemetry broadcast.")
    add_bullet(doc, "• File System:", "Secure local file server for document, log, and PDF storage.")

    add_heading_2(doc, "5. Shift Supervisor Web/Desktop App")
    add_bullet(doc, "• Tech Stack:", "React 18, Vite, Shadcn UI, TypeScript, Tailwind CSS, Recharts, Leaflet/Mapbox, WebSockets.")
    add_bullet(doc, "• Features:", "View/edit round plans, live IoT sensor logs, predictive simulation engine, shift allotment, shift handovers approval, and automatic PDF report generator.")

    add_heading_2(doc, "6. Shift Operators Mobile App")
    add_bullet(doc, "• Tech Stack:", "Flutter / React Native / PWA, SQLite edge cache, Bloc state management.")
    add_bullet(doc, "• Features:", "Quick summary of shifts, tasks, issues, and alerts; detailed event logging during rounds; multi-language support; smart voice control; offline auto-sync.")

    add_heading_2(doc, "7. AI Components & ML Engine")
    add_bullet(doc, "• Predictive Simulation Engine:", "scikit-learn Random Forest Regressor predicting roof sag displacement and collapse risk. Evaluates 10 parameters, placing 42% weight on 5-min rate-of-change velocity (Δdisp/Δt, Δtilt/Δt). Performance: MAE 1.27 | R² 0.9969.")
    add_bullet(doc, "• Decision Tree Algorithm:", "Recommends specific workers and technicians for task assignment based on log issue categories and hazard priority.")

    img3 = os.path.join(assets_dir, "slide3_technical_architecture.png")
    add_image_reference(doc, img3, "Slide 3 Comprehensive Technical Approach & System Architecture Diagram")

    # =========================================================================
    # SLIDE 4
    # =========================================================================
    add_heading_1(doc, "SLIDE 4: Feasibility and Viability & Challenges Matrix")
    
    add_heading_2(doc, "Part 1: 4-Dimensional Feasibility & Market Viability Analysis")
    add_bullet(doc, "• Technical Feasibility:", "India's coal industry is projected to grow by 7.57% (2024-2029). Our low-cost ESP32 LoRa wireless system (~₹1,590/node) and AI engine (R² 0.9969) significantly improve mining safety without complex rewiring.")
    add_bullet(doc, "• Operational Feasibility:", "India's mining IT spending is at $2.48 Billion. MineGuard AI digitalizes paper logbooks and SMPs, reducing human reporting errors by 90% and streamlining shift handovers.")
    add_bullet(doc, "• Economic Feasibility:", "Developing our software and hardware in India costs 35-50% less than Western commercial packages (e.g. Minemax, Innovapptive). Complete panel setup costs ₹11,990 vs ₹10+ Lakhs cabled systems.")
    add_bullet(doc, "• Regulatory Feasibility:", "Software automates DGMS (Directorate General of Mines Safety) compliance checks under the Mines Act 1952, simplifying safety audits.")
    add_bullet(doc, "• Market Viability:", "Digital India and tech initiatives create a highly favorable adoption ecosystem in Indian coalfields.")
    add_bullet(doc, "• Sustainable Viability:", "Global mining software market is expanding at an 8.1% CAGR, ensuring long-term demand.")

    add_heading_2(doc, "Part 2: Technical Challenges & Mitigation Matrix")
    
    t_chal = doc.add_table(rows=4, cols=3)
    t_chal.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_chal.autofit = False
    
    headers = ["Domain Challenge", "Underground Operational Issue", "MineGuard AI Technical Solution"]
    w_list = [Inches(2.0), Inches(2.2), Inches(2.4)]
    
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
        ("Integration & User Adoption", "Language barriers, legacy ERP compatibility, system consistency, and worker training.", "Multi-language voice support (10+ Indian languages), API data mapping for ERPs, Docker containerization, and 2-week hands-on worker training program."),
        ("Safety & Productivity Validation", "Accurately cross-validating worker activity and roof stability under harsh conditions.", "Scalable ESP32 wireless nodes, multi-sensor safety vests, and Random Forest AI analysis evaluating 5-minute velocity rate of change."),
        ("No-Internet Communication & Data Privacy", "Severe RF signal loss underground, power outages, and data security risks.", "SX1276 LoRa peer-to-peer mesh network, SQLite local edge database caching to prevent data loss, Zero Trust policy, and AES-256 E2E encryption.")
    ]

    for row_idx, data_tuple in enumerate(chal_data, start=1):
        row_cells = t_chal.rows[row_idx].cells
        bg_color = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
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

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    img4 = os.path.join(assets_dir, "slide4_feasibility_market_chart.png")
    add_image_reference(doc, img4, "Slide 4 Market Growth CAGR & Feasibility Opportunity Chart")

    # =========================================================================
    # SLIDE 5
    # =========================================================================
    add_heading_1(doc, "SLIDE 5: Impacts, Stakeholder Workflow & UN SDGs")
    
    add_heading_2(doc, "Section 1: MULTI-SECTOR IMPACTS & BENEFITS")
    add_bullet(doc, "• Economic Benefits:", "Though there is a minor upfront hardware cost (₹1,590/node), the system pays off exponentially by cutting down mine downtime, avoiding panel destruction, and preventing roof collapse accidents, generating multi-crore long-term savings.")
    add_bullet(doc, "• Social Benefits:", "Enhances worker safety and well-being while promoting a zero-casualty mining culture across 300,000+ Indian underground coal miners, reducing panic, stress, and injuries.")
    add_bullet(doc, "• Environmental Benefits:", "Prevents surface land subsidence fissuring and groundwater depletion above mined-out panels; optimizes machinery usage to reduce carbon footprint.")

    add_heading_2(doc, "Section 2: STAKEHOLDERS & IMPACT FLOW (Sample Scenario)")
    add_bullet(doc, "• Step 1: Mine Operator (Worker/Electrician):", "Notices a roof crack or sensor registers tilt -> reports issue via smart voice controls or mobile app. Result: Reduced workload, improved task focus, enhanced safety, less pressure.")
    add_bullet(doc, "• Step 2: AI Engine Processing:", "Processes telemetry + issue, calculates 5-min velocity rate, predicts subsidence risk, and assigns priority to qualified personnel. Result: Faster decisions with real-time AI/IoT data, clear task documentation.")
    add_bullet(doc, "• Step 3: Mine Supervisor:", "Reviews AI risk heatmap, clears SMP checklist, cross-validates IoT data, approves evacuation/reinforcement task for smooth shift handover. Result: Simplified audits, continuous real-time safety tracking.")
    add_bullet(doc, "• Step 4: Mine Management & DGMS Regulators:", "ERP integration enhances operations and data storage; utilizes data analytics for regulatory compliance and safety audits. Result: Improved regulatory oversight, data-driven safety policies.")

    add_heading_2(doc, "Section 3: OUR PROMISE, UN SDGs & NATIONAL GOALS")
    add_bullet(doc, "• UN SDG Alignment:", "SDG 3 (Good Health & Well-Being), SDG 8 (Decent Work & Economic Growth), SDG 9 (Industry, Innovation & Infrastructure), SDG 12 (Responsible Consumption & Production).")
    add_bullet(doc, "• India's Coal Target:", "Supports India's national goal of reaching 1.5 Billion Tons of Coal Production by 2030 (FY 2030-31).")
    add_bullet(doc, "• Projected National Efficiency Gain:", "MineGuard AI is projected to improve operational safety & efficiency by 7.69%, adding 385.275 Million Tons of safe coal production and cutting the government's target gap by 22.67% for 2030.")

    img5 = os.path.join(assets_dir, "slide5_stakeholder_impact_flow.png")
    add_image_reference(doc, img5, "Slide 5 Stakeholder Hazard Response & Impact Flowchart")

    # =========================================================================
    # SLIDE 6
    # =========================================================================
    add_heading_1(doc, "SLIDE 6: Research, Market Economics & References")
    
    add_heading_2(doc, "Section 1: COAL MINES IN INDIA — RESEARCH")
    add_bullet(doc, "• Historical Context:", "Commercial coal mining in India began in 1774 in the Raniganj Coalfield. India is the 2nd largest coal producer globally.")
    add_bullet(doc, "• Production Stats:", "India's monthly coal production stands at ~62.67 Million Tons. Power utilities dispatch accounts for ~58.09 MT.")
    add_bullet(doc, "• DGMS Regulations:", "Directorate General of Mines Safety (DGMS) regulates coal mine safety under the Mines Act 1952, enforcing strict Strata Management Plans (SMP).")

    add_heading_2(doc, "Section 2: MARKET RESEARCH & UNIT ECONOMICS")
    add_bullet(doc, "• TAM (Total Addressable Market):", "₹77,190 Crore ($9.3 Billion USD) — Global & Indian Mining Safety & Telemetry Market.")
    add_bullet(doc, "• SAM (Serviceable Available Market):", "₹23,157 Crore — CIL Subsidiaries (ECL, BCCL, CCL, SECL, WCL) & SCCL Underground Coal Mines.")
    add_bullet(doc, "• SOM (Serviceable Obtainable Market):", "₹1,158 Crore — High-risk depillaring and longwall extraction panels in Indian coal seams.")

    add_heading_2(doc, "Mid-Sized Mine Financial Revenue Model (500 Workers Sample)")
    
    t_bom = doc.add_table(rows=6, cols=4)
    t_bom.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_bom.autofit = False
    
    bom_headers = ["Item Category", "Quantity", "Price per Unit (INR)", "Total Value (INR)"]
    bom_widths = [Inches(2.5), Inches(1.1), Inches(1.5), Inches(1.5)]
    
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
        ("Safety Vests (Sensors)", "100 Units", "₹728", "₹72,800"),
        ("Mine Danger Nodes", "100 Units", "₹720", "₹77,800"),
        ("Installation & Calibration", "200 Units", "₹980", "₹196,000"),
        ("Service & Monthly Audits", "12 Months", "₹5,000 / month", "₹60,000"),
        ("Year-1 Total Revenue", "500 Workers Panel", "-", "₹846,600")
    ]

    for row_idx, data_tuple in enumerate(bom_data, start=1):
        row_cells = t_bom.rows[row_idx].cells
        bg_color = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
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
            if col_idx in [0, 3]:
                r.font.bold = True

    add_bullet(doc, "• Profit Margins:", "Software Sales: 85% profit margin (low recurring cloud cost); Hardware Sales: 30% profit margin.")

    add_heading_2(doc, "Section 3: REFERENCES & BENCHMARKING")
    add_bullet(doc, "• GitHub Repository & Project Files:", "https://github.com/sharequesyed/MineGuard-AI")
    add_bullet(doc, "• IoT References:", "ESP MESH / ESP32 LoRa 868MHz Chirp Spread Spectrum technical datasheets; Wi-Fi in coal mines safety studies.")
    add_bullet(doc, "• AI/ML References:", "scikit-learn Random Forest Regressor & Classifier; velocity rate feature engineering for geotechnical subsidence prediction.")
    add_bullet(doc, "• Backend References:", "Apache Kafka message bus & Apache Flink real-time stream engine; FastAPI async Python backend.")
    add_bullet(doc, "• Mine Operations Benchmarking:", "Minemax (mine planning software) and Innovapptive (operations & plant maintenance) comparative benchmarking.")

    img6 = os.path.join(assets_dir, "slide6_market_economics_references.png")
    add_image_reference(doc, img6, "Slide 6 Market Sizing TAM/SAM/SOM Concentric Sizing & Reference Links Card")

    # Output paths
    output_docx = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Presentation_Content.docx"
    try:
        doc.save(output_docx)
        print(f"Docx file successfully created at: {output_docx}")
    except PermissionError:
        output_docx_alt = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Presentation_Content_v2.docx"
        doc.save(output_docx_alt)
        print(f"Original file was locked. Docx file saved at: {output_docx_alt}")

if __name__ == '__main__':
    build_docx()
