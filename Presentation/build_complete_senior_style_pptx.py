import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def add_pill_badge(slide, left, top, width, height, text, bg_rgb, font_size=12, text_rgb=RGBColor(255, 255, 255)):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_rgb
    shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.name = 'Arial'
    run.font.size = Pt(font_size)
    run.font.bold = True
    run.font.color.rgb = text_rgb
    return shape

def add_card_box(slide, left, top, width, height, bg_rgb, border_rgb=None, border_width=1):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_rgb
    if border_rgb:
        shape.line.color.rgb = border_rgb
        shape.line.width = Pt(border_width)
    else:
        shape.line.fill.background()
    return shape

def add_circle_number(slide, left, top, number_str, font_size=12):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, Inches(0.35), Inches(0.35))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
    shape.line.color.rgb = RGBColor(0, 0, 0)
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = str(number_str)
    run.font.name = 'Arial'
    run.font.size = Pt(font_size)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return shape

def add_text_box(slide, left, top, width, height, text_runs):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    
    for idx, run_info in enumerate(text_runs):
        if idx == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
            
        p_text = run_info[0]
        is_bold = run_info[1] if len(run_info) > 1 else False
        font_size = run_info[2] if len(run_info) > 2 else 11
        color_rgb = run_info[3] if len(run_info) > 3 else RGBColor(0, 0, 0)
        space_after = run_info[4] if len(run_info) > 4 else 2
        align = run_info[5] if len(run_info) > 5 else PP_ALIGN.LEFT
        
        p.space_after = Pt(space_after)
        p.alignment = align
        run = p.add_run()
        run.text = p_text
        run.font.name = 'Arial'
        run.font.size = Pt(font_size)
        run.font.bold = is_bold
        run.font.color.rgb = color_rgb
    return txBox

def add_footer(slide, current_slide_num):
    # Blue Footer Bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.15), Inches(13.333), Inches(0.35))
    bar.fill.solid()
    bar.fill.fore_color.rgb = RGBColor(24, 144, 255)
    bar.line.fill.background()
    
    tf = bar.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "MineGuard AI - @SIH Idea Submission"
    run.font.name = 'Arial'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(255, 255, 255)
    
    # Page Number
    tx = slide.shapes.add_textbox(Inches(12.7), Inches(7.15), Inches(0.5), Inches(0.35))
    p2 = tx.text_frame.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    r2 = p2.add_run()
    r2.text = str(current_slide_num)
    r2.font.name = 'Arial'
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(255, 255, 255)

def build_presentation():
    template_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\SIH2026-IDEA-Presentation-Format.pptx"
    output_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Official_Presentation.pptx"

    prs = Presentation(template_path)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Primary Colors
    BLACK = RGBColor(0, 0, 0)
    WHITE = RGBColor(255, 255, 255)
    BLUE_HEADER = RGBColor(24, 144, 255)
    DOCKER_BLUE = RGBColor(59, 130, 246)
    LIGHT_BLUE_BG = RGBColor(230, 247, 255)
    LIGHT_BLUE_BORDER = RGBColor(145, 213, 255)
    LIGHT_YELLOW_BG = RGBColor(255, 251, 230)
    LIGHT_YELLOW_BORDER = RGBColor(255, 229, 143)
    LIGHT_ORANGE_BG = RGBColor(255, 245, 230)
    LIGHT_ORANGE_BORDER = RGBColor(255, 213, 145)
    CRIMSON = RGBColor(220, 38, 38)
    DARK_GRAY = RGBColor(89, 89, 89)

    # =========================================================================
    # SLIDE 1: TITLE PAGE
    # =========================================================================
    slide1 = prs.slides[0]
    for shape in list(slide1.shapes):
        if shape.has_text_frame and ("Problem Statement" in shape.text or "SIH" in shape.text):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            runs = [
                ("Problem Statement ID: SIH26025\n", True, 16, BLUE_HEADER),
                ("Problem Statement Title: Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India\n\n", True, 13, BLACK),
                ("Theme: Smart Automation / Safety & Security / Disaster Management\n", False, 12, DARK_GRAY),
                ("PS Category: Software & Hardware (Hybrid IoT-AI System)\n\n", False, 12, DARK_GRAY),
                ("Team ID: SIH2026-MINENOVA6\n", True, 14, BLUE_HEADER),
                ("Team Name (Registered on Portal): MineNova6\n\n", True, 16, CRIMSON),
                ("Team Members: Shareque (Lead), Monika (Research), Aditya (UI/UX), Farhan (Frontend), Atharva (Backend), Affan (AI/ML)", False, 11, DARK_GRAY)
            ]
            for r_text, r_bold, r_size, r_color in runs:
                run = p.add_run()
                run.text = r_text
                run.font.name = 'Arial'
                run.font.size = Pt(r_size)
                run.font.bold = r_bold
                run.font.color.rgb = r_color

    # =========================================================================
    # SLIDE 2: PROPOSED SOLUTION & PROTOTYPE PANEL
    # =========================================================================
    slide2 = prs.slides[1]
    for shape in list(slide2.shapes):
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

    # Team Badge & Header
    add_card_box(slide2, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), WHITE, BLACK, 2)
    add_text_box(slide2, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), [("MineNova6", True, 14, BLACK, 0, PP_ALIGN.CENTER)])

    add_text_box(slide2, Inches(2.0), Inches(0.1), Inches(6.0), Inches(0.5), [("MINEGUARD AI — SOLUTION & PROTOTYPE", True, 22, BLACK, 0, PP_ALIGN.CENTER)])
    add_pill_badge(slide2, Inches(8.2), Inches(0.15), Inches(1.2), Inches(0.4), "SOLUTION", BLACK, 11)

    # Left Side: Solution & Why We Stand Out
    add_card_box(slide2, Inches(0.3), Inches(0.75), Inches(6.5), Inches(6.2), WHITE, DARK_GRAY, 1)
    add_text_box(slide2, Inches(0.4), Inches(0.85), Inches(6.3), Inches(5.9), [
        ("Proposed Solution Overview:", True, 14, BLUE_HEADER, 2),
        ("• Wireless ESP32 LoRa Sensor Mesh: Tracks roof tilt, sag displacement, crack growth, and load stress without fragile cabling.", False, 10.5, BLACK, 2),
        ("• AI Subsidence Predictor: Random Forest ML engine correlates 10 parameters, prioritizing 5-min velocity (Δdisp/Δt) to catch Stage-1 micro-sagging.", False, 10.5, BLACK, 2),
        ("• React Command Center: Web dashboard with Leaflet seam map, 60 FPS rolling charts, and SIH Emergency Simulator.", False, 10.5, BLACK, 2),
        ("• Edge & Cloud Dual Sirens: Triggers 1kHz local piezo sirens at mine face independently during network outages.", False, 10.5, BLACK, 2),
        ("• Tailored for Indian Coalfields: Replaces reactive cabled monitoring with predictive warnings for Jharia & Raniganj.", False, 10.5, BLACK, 2),
        ("• 100% Functional MVP: Validated with live hardware LoRa telemetry and real-time dashboard sync.\n", False, 10.5, BLACK, 4),
        ("WHY WE STAND OUT?", True, 13, CRIMSON, 2),
        ("1. Velocity-Weighted AI: Predicts roof sag in Stage 1 using 5-min rate of change (MAE: 1.27, R²: 0.9969).", False, 10, BLACK, 1),
        ("2. 98.8% Cost Reduction: ₹1,590/node ($19) vs ₹50,000+ cabled legacy sensors. Full 6-node panel for ₹11,990.", False, 10, BLACK, 1),
        ("3. Non-Line-Of-Sight Telemetry: 868MHz LoRa Chirp Spread Spectrum penetrates 2km solid rock strata.", False, 10, BLACK, 1),
        ("4. Fail-Safe Dual Edge Siren Resilience: ESP32 MCU fires local sirens on GPIO 12/13 automatically during outages.", False, 10, BLACK, 0)
    ])

    # Right Side: Prototype Panel Image Embed
    proto_img_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\prototype_white_theme.jpg"
    if os.path.exists(proto_img_path):
        slide2.shapes.add_picture(proto_img_path, Inches(7.0), Inches(0.75), Inches(6.0), Inches(6.2))

    add_footer(slide2, 2)

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH (EXACT SENIOR THEME + MINE SUBSIDENCE IMAGE)
    # =========================================================================
    slide3 = prs.slides[2]
    for shape in list(slide3.shapes):
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

    # Top Badges
    add_card_box(slide3, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), WHITE, BLACK, 2)
    add_text_box(slide3, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), [("MineNova6", True, 14, BLACK, 0, PP_ALIGN.CENTER)])

    add_text_box(slide3, Inches(2.0), Inches(0.1), Inches(9.3), Inches(0.5), [("Technical Approach", True, 26, BLACK, 0, PP_ALIGN.CENTER)])
    add_text_box(slide3, Inches(11.4), Inches(0.1), Inches(1.7), Inches(0.5), [("SIH 2026 OFFICIAL", True, 10, RGBColor(217, 119, 6), 0, PP_ALIGN.RIGHT)])

    # SECTION 4: BACKEND ARCHITECTURE
    add_circle_number(slide3, Inches(0.3), Inches(0.7), "4", 12)
    add_pill_badge(slide3, Inches(0.7), Inches(0.68), Inches(2.7), Inches(0.38), "BACKEND ARCHITECTURE", BLACK, 13)

    add_card_box(slide3, Inches(0.2), Inches(1.15), Inches(0.35), Inches(3.6), DOCKER_BLUE)
    add_text_box(slide3, Inches(0.2), Inches(2.0), Inches(0.35), Inches(2.0), [("Docker Container", True, 12, WHITE, 0, PP_ALIGN.CENTER)])

    add_card_box(slide3, Inches(0.6), Inches(1.15), Inches(3.2), Inches(3.6), LIGHT_BLUE_BG, LIGHT_BLUE_BORDER, 1.5)
    
    add_card_box(slide3, Inches(0.7), Inches(1.25), Inches(1.4), Inches(0.6), WHITE, DARK_GRAY, 1)
    add_text_box(slide3, Inches(0.7), Inches(1.25), Inches(1.4), Inches(0.6), [
        ("TimescaleDB / SQLite", True, 9, BLACK, 1),
        ("2.5s IoT telemetry DB", False, 8, DARK_GRAY, 0)
    ])

    add_card_box(slide3, Inches(2.2), Inches(1.25), Inches(1.5), Inches(0.6), WHITE, DARK_GRAY, 1)
    add_text_box(slide3, Inches(2.2), Inches(1.25), Inches(1.5), Inches(0.6), [
        ("PostgreSQL", True, 9, BLACK, 1),
        ("Relational ORM records", False, 8, DARK_GRAY, 0)
    ])

    add_card_box(slide3, Inches(0.7), Inches(1.95), Inches(3.0), Inches(0.5), LIGHT_ORANGE_BG, LIGHT_ORANGE_BORDER, 1)
    add_text_box(slide3, Inches(0.7), Inches(1.95), Inches(3.0), Inches(0.5), [
        ("Python FastAPI REST & WebSocket Server", True, 10, RGBColor(212, 107, 8), 1, PP_ALIGN.CENTER),
        ("Async ASGI Event Loop & Pydantic Validation", False, 8, DARK_GRAY, 0, PP_ALIGN.CENTER)
    ])

    add_card_box(slide3, Inches(0.7), Inches(2.55), Inches(1.4), Inches(0.45), WHITE, DARK_GRAY, 1)
    add_text_box(slide3, Inches(0.7), Inches(2.55), Inches(1.4), Inches(0.45), [("IoT Ingestion Service", True, 9, BLACK, 0)])

    add_card_box(slide3, Inches(2.2), Inches(2.55), Inches(1.5), Inches(0.45), LIGHT_ORANGE_BG, LIGHT_ORANGE_BORDER, 1)
    add_text_box(slide3, Inches(2.2), Inches(2.55), Inches(1.5), Inches(0.45), [("🐍 AI Inference Engine", True, 9, RGBColor(212, 107, 8), 0)])

    add_card_box(slide3, Inches(0.7), Inches(3.1), Inches(3.0), Inches(0.55), RGBColor(186, 231, 255), RGBColor(105, 192, 255), 1)
    add_text_box(slide3, Inches(0.7), Inches(3.1), Inches(3.0), Inches(0.55), [
        ("🚨 SIH Emergency Simulator Service", True, 10, RGBColor(0, 80, 179), 1, PP_ALIGN.CENTER),
        ("One-Click Stress Simulation Engine", False, 8, DARK_GRAY, 0, PP_ALIGN.CENTER)
    ])

    add_card_box(slide3, Inches(0.7), Inches(3.75), Inches(3.0), Inches(0.45), RGBColor(246, 255, 237), RGBColor(183, 235, 143), 1)
    add_text_box(slide3, Inches(0.7), Inches(3.75), Inches(3.0), Inches(0.45), [
        ("ESP32 LoRa Gateway Ingestion Service", True, 9, RGBColor(56, 158, 13), 0, PP_ALIGN.CENTER)
    ])

    add_card_box(slide3, Inches(3.9), Inches(1.15), Inches(0.3), Inches(3.6), BLUE_HEADER)
    add_text_box(slide3, Inches(3.9), Inches(1.3), Inches(0.3), Inches(3.3), [("API GATEWAY", True, 10, WHITE, 0, PP_ALIGN.CENTER)])

    add_card_box(slide3, Inches(4.25), Inches(1.15), Inches(0.25), Inches(3.6), RGBColor(245, 245, 245), DARK_GRAY, 1)

    # SECTION 8: AI SUBSIDENCE PREDICTOR
    add_circle_number(slide3, Inches(0.3), Inches(5.0), "8", 12)
    add_pill_badge(slide3, Inches(0.7), Inches(4.98), Inches(2.6), Inches(0.38), "AI SUBSIDENCE PREDICTOR", BLACK, 12)

    add_card_box(slide3, Inches(0.7), Inches(5.45), Inches(3.8), Inches(0.75), LIGHT_YELLOW_BG, LIGHT_YELLOW_BORDER, 1)
    add_text_box(slide3, Inches(0.7), Inches(5.45), Inches(3.8), Inches(0.75), [
        ("Random Forest ML Engine (MAE: 1.27 | R²: 0.9969)", True, 10, BLACK, 1),
        ("• Evaluates 10 parameters (tilt, sag, load, temp, hum).", False, 8, DARK_GRAY, 1),
        ("• Velocity Weighting (42% Weight): Prioritizes 5-min Δdisp/Δt & Δtilt/Δt to catch Stage-1 micro-sagging before collapse.", True, 8, CRIMSON, 0)
    ])

    add_card_box(slide3, Inches(4.55), Inches(5.45), Inches(0.35), Inches(1.5), RGBColor(105, 192, 255))
    add_text_box(slide3, Inches(4.55), Inches(5.7), Inches(0.35), Inches(1.0), [("FASTAPI", True, 10, BLACK, 0, PP_ALIGN.CENTER)])

    # SECTION 3: MINE SAFETY ADMIN
    add_circle_number(slide3, Inches(5.0), Inches(0.7), "3", 12)
    add_pill_badge(slide3, Inches(5.4), Inches(0.68), Inches(1.8), Inches(0.35), "MINE SAFETY ADMIN", BLUE_HEADER, 11)

    add_card_box(slide3, Inches(5.0), Inches(1.15), Inches(4.0), Inches(0.85), WHITE, DARK_GRAY, 1)
    add_text_box(slide3, Inches(5.0), Inches(1.15), Inches(4.0), Inches(0.85), [
        ("Efficient Task & Strata Management with Web App", True, 10, BLACK, 1),
        ("• Digitizes DGMS Strata Management Plans (SMP).", False, 8.5, DARK_GRAY, 1),
        ("• Zero Trust Intranet Access & Centralized Worker Shift Allotment.", False, 8.5, DARK_GRAY, 1),
        ("• Automatic PDF Compliance Reports.", True, 8.5, CRIMSON, 0)
    ])

    # SECTION 1: UNDERGROUND COAL SEAM & MINE SUBSIDENCE IMAGE EMBED
    add_circle_number(slide3, Inches(5.0), Inches(2.1), "1", 12)
    add_pill_badge(slide3, Inches(5.4), Inches(2.08), Inches(2.4), Inches(0.35), "UNDERGROUND COAL SEAM", BLACK, 11)

    subsidence_img_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\mine_subsidence_diagram.png"
    if os.path.exists(subsidence_img_path):
        slide3.shapes.add_picture(subsidence_img_path, Inches(5.0), Inches(2.5), Inches(4.1), Inches(2.3))

    # SECTION 7: ESP32 LORA SENSOR BOARD
    add_circle_number(slide3, Inches(5.0), Inches(4.9), "7", 12)
    add_pill_badge(slide3, Inches(5.4), Inches(4.88), Inches(2.3), Inches(0.35), "ESP32 LORA SENSOR BOARD", BLACK, 11)

    add_card_box(slide3, Inches(5.0), Inches(5.3), Inches(4.1), Inches(1.7), LIGHT_ORANGE_BG, LIGHT_ORANGE_BORDER, 1)
    add_text_box(slide3, Inches(5.0), Inches(5.3), Inches(4.1), Inches(1.7), [
        ("Hardware Sensor Node Suite (₹1,590/node):", True, 10, RGBColor(212, 107, 8), 1),
        ("• ESP32 32-bit MCU Board + SX1276 LoRa 868MHz Transceiver (2km range).", False, 8.5, BLACK, 1),
        ("• MPU6050 Gyro/Accel: Roof tilt θx, θy & vibration acceleration.", False, 8.5, BLACK, 1),
        ("• Linear String Potentiometer: Roof sag displacement (0-50mm).", False, 8.5, BLACK, 1),
        ("• HX711 Load Cell Amp: Hydraulic prop stress (0-200kN).", False, 8.5, BLACK, 1),
        ("• Edge Failover: Triggers local 1kHz piezo siren (GPIO 12/13) on network loss.", True, 8.5, CRIMSON, 0)
    ])

    # SECTION 5: STRATA CONTROL ENGINEER
    add_circle_number(slide3, Inches(9.3), Inches(0.7), "5", 12)
    add_pill_badge(slide3, Inches(9.7), Inches(0.68), Inches(2.5), Inches(0.35), "STRATA CONTROL ENGINEER", BLACK, 11)

    add_card_box(slide3, Inches(9.3), Inches(1.15), Inches(3.7), Inches(2.6), WHITE, DARK_GRAY, 1)
    add_text_box(slide3, Inches(9.3), Inches(1.15), Inches(3.7), Inches(2.6), [
        ("React 18 Command Center Dashboard", True, 11, BLUE_HEADER, 1),
        ("Stack: React 18, Vite, Tailwind CSS, Recharts 60 FPS, Leaflet Map", False, 8.5, DARK_GRAY, 2),
        ("• Interactive Underground Seam Map: Node badges N1-N6 over Jharia Coalfield #4.", False, 8.5, BLACK, 1),
        ("• SIH Live Emergency Simulator: 1-click subsidence event demo.", True, 8.5, BLUE_HEADER, 1),
        ("• Velocity-Weighted Warnings: Detects pre-failure sagging in Stage 1.", False, 8.5, BLACK, 1),
        ("• Real-Time 60 FPS Graphs: Rolling tilt, sag, and load curves.", False, 8.5, BLACK, 1),
        ("• Shift Allotment & Handover Approvals.", False, 8.5, BLACK, 0)
    ])

    # SECTION 6: SHIFT OPERATORS & SIRENS
    add_circle_number(slide3, Inches(9.3), Inches(3.9), "6", 12)
    add_pill_badge(slide3, Inches(9.7), Inches(3.88), Inches(2.5), Inches(0.35), "SHIFT OPERATORS & SIRENS", BLACK, 11)

    add_card_box(slide3, Inches(9.3), Inches(4.3), Inches(3.7), Inches(2.7), LIGHT_YELLOW_BG, LIGHT_YELLOW_BORDER, 1)
    add_text_box(slide3, Inches(9.3), Inches(4.3), Inches(3.7), Inches(2.7), [
        ("Mobile App & Edge Evacuation Sirens", True, 11, BLACK, 1),
        ("Stack: SQLite, BLoC, Flutter / Handheld Devices", False, 8.5, DARK_GRAY, 2),
        ("• 🔊 1kHz Local Piezo Siren Alarms: Instant audio warnings at mine face.", True, 9, CRIMSON, 1),
        ("• Quick summary of assigned shifts, tasks, and sag risk alerts.", False, 8.5, BLACK, 1),
        ("• Log details about tasks, issues, and prop load during rounds.", False, 8.5, BLACK, 1),
        ("• Multilingual Indian languages & smart voice-assisted logging.", False, 8.5, BLACK, 1),
        ("• Live Vercel Deployment: https://mineguard-ai.vercel.app", True, 8.5, BLUE_HEADER, 0)
    ])

    add_footer(slide3, 3)

    # =========================================================================
    # SLIDE 4: FEASIBILITY AND VIABILITY
    # =========================================================================
    slide4 = prs.slides[3]
    for shape in list(slide4.shapes):
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

    add_card_box(slide4, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), WHITE, BLACK, 2)
    add_text_box(slide4, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), [("MineNova6", True, 14, BLACK, 0, PP_ALIGN.CENTER)])

    add_text_box(slide4, Inches(2.0), Inches(0.1), Inches(6.0), Inches(0.5), [("FEASIBILITY AND VIABILITY", True, 24, BLACK, 0, PP_ALIGN.CENTER)])
    add_pill_badge(slide4, Inches(8.2), Inches(0.15), Inches(1.4), Inches(0.4), "CHALLENGES", BLACK, 11)

    # Left Side Feasibility Cards
    add_card_box(slide4, Inches(0.3), Inches(0.75), Inches(6.0), Inches(6.2), WHITE, DARK_GRAY, 1)
    add_text_box(slide4, Inches(0.4), Inches(0.85), Inches(5.8), Inches(6.0), [
        ("Technical Feasibility:", True, 13, BLUE_HEADER, 1),
        ("• Low power 3.3V DC logic; 3.7V LiFePO4 battery lasts 6+ months with deep sleep cycles.", False, 10, BLACK, 1),
        ("• 868MHz LoRa Chirp Spread Spectrum penetrates solid coal/rock strata up to 2km.\n", False, 10, BLACK, 2),
        ("Operational Feasibility:", True, 13, BLUE_HEADER, 1),
        ("• Simple clamp-on roof bolting installation requires zero specialized training for miners.\n", False, 10, BLACK, 2),
        ("Economic Feasibility:", True, 13, BLUE_HEADER, 1),
        ("• ₹1,590 ($19 USD) per node; ₹11,990 total panel setup (98.8% savings vs ₹10+ Lakhs cabled systems).\n", False, 10, BLACK, 2),
        ("Regulatory Feasibility:", True, 13, BLUE_HEADER, 1),
        ("• Automates compliance checks for DGMS Strata Management Plans (SMP).\n", False, 10, BLACK, 2),
        ("Market & Sustainable Viability:", True, 13, CRIMSON, 1),
        ("• TAM: ₹15,000 Cr | SAM: ₹4,500 Cr | SOM: ₹450 Cr in Indian depillaring panels.", False, 10, BLACK, 0)
    ])

    # Right Side Challenges & Product Photo
    add_card_box(slide4, Inches(6.5), Inches(0.75), Inches(6.5), Inches(6.2), WHITE, DARK_GRAY, 1)
    add_text_box(slide4, Inches(6.6), Inches(0.85), Inches(6.3), Inches(3.2), [
        ("Technical Challenges & Mitigation Matrix:\n", True, 13, CRIMSON, 2),
        ("1. Explosive Methane Atmosphere ➔ IP67 flameproof polycarbonate enclosure complying with DGMS Intrinsically Safe (IS Ex 'd') standards.\n", False, 10, BLACK, 2),
        ("2. Severe RF Rock Attenuation ➔ 868MHz Chirp Spread Spectrum (CSS) frequency modulation designed for non-line-of-sight penetration.\n", False, 10, BLACK, 2),
        ("3. Network / Server Outages ➔ Edge failover piezo sirens (GPIO 12/13) fire independently & log data to local SD buffer.\n", False, 10, BLACK, 2),
        ("4. Dust & Calibration Drift ➔ Auto-zero calibration routines on startup with protective IP65 dust-filtering membranes.", False, 10, BLACK, 0)
    ])

    # Embedded Product Photo
    product_img_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\team_sih_prep\sensor_node_final_product.jpg"
    if os.path.exists(product_img_path):
        slide4.shapes.add_picture(product_img_path, Inches(6.7), Inches(4.2), Inches(6.1), Inches(2.6))

    add_footer(slide4, 4)

    # =========================================================================
    # SLIDE 5: IMPACT AND BENEFITS
    # =========================================================================
    slide5 = prs.slides[4]
    for shape in list(slide5.shapes):
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

    add_card_box(slide5, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), WHITE, BLACK, 2)
    add_text_box(slide5, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), [("MineNova6", True, 14, BLACK, 0, PP_ALIGN.CENTER)])

    add_text_box(slide5, Inches(2.0), Inches(0.1), Inches(6.0), Inches(0.5), [("IMPACTS AND BENEFITS", True, 24, BLACK, 0, PP_ALIGN.CENTER)])
    add_pill_badge(slide5, Inches(8.2), Inches(0.15), Inches(1.4), Inches(0.4), "OUR PROMISE", BLACK, 11)

    # 3 Top Cards (Economic, Social, Environmental)
    add_card_box(slide5, Inches(0.3), Inches(0.75), Inches(4.1), Inches(1.8), LIGHT_ORANGE_BG, LIGHT_ORANGE_BORDER, 1)
    add_text_box(slide5, Inches(0.4), Inches(0.85), Inches(3.9), Inches(1.6), [
        ("Economic Benefits", True, 13, RGBColor(212, 107, 8), 2),
        ("Prevents multi-crore losses from damaged hydraulic supports, continuous miners, mine closure penalties, and legal compensation.", False, 10, BLACK, 0)
    ])

    add_card_box(slide5, Inches(4.6), Inches(0.75), Inches(4.1), Inches(1.8), LIGHT_YELLOW_BG, LIGHT_YELLOW_BORDER, 1)
    add_text_box(slide5, Inches(4.7), Inches(0.85), Inches(3.9), Inches(1.6), [
        ("Social Benefits", True, 13, RGBColor(217, 119, 6), 2),
        ("Protects 300,000+ underground miners in India by eliminating unpredicted roof collapses, fostering a zero-casualty safety culture.", False, 10, BLACK, 0)
    ])

    add_card_box(slide5, Inches(8.9), Inches(0.75), Inches(4.1), Inches(1.8), LIGHT_BLUE_BG, LIGHT_BLUE_BORDER, 1)
    add_text_box(slide5, Inches(9.0), Inches(0.85), Inches(3.9), Inches(1.6), [
        ("Environmental Benefits", True, 13, BLUE_HEADER, 2),
        ("Prevents surface land fissuring, groundwater table depletion, and soil degradation above mined-out panels.", False, 10, BLACK, 0)
    ])

    # Stakeholder Evacuation Flow
    add_card_box(slide5, Inches(0.3), Inches(2.7), Inches(12.7), Inches(2.2), WHITE, DARK_GRAY, 1)
    add_text_box(slide5, Inches(0.4), Inches(2.8), Inches(12.5), Inches(2.0), [
        ("STAKEHOLDERS & EVACUATION WORKFLOW:", True, 13, BLUE_HEADER, 2),
        ("👷 Underground Miner / Operator ➔ Gets instant 1kHz piezo siren audio alarm at mine face for safe evacuation.\n", False, 10.5, BLACK, 2),
        ("👮 Shift Safety Officer ➔ Receives real-time risk alert notification on mobile/handheld device with exact seam coordinates.\n", False, 10.5, BLACK, 2),
        ("👨‍💼 Strata Control Engineer ➔ Analyzes 10-parameter AI graphs to plan preventive roof bolting & prop reinforcement.\n", False, 10.5, BLACK, 2),
        ("🏛️ DGMS & Mine Management ➔ Accesses automated digital log reports for regulatory safety audits.", False, 10.5, BLACK, 0)
    ])

    # UN SDGs & National Goals
    add_card_box(slide5, Inches(0.3), Inches(5.0), Inches(12.7), Inches(1.95), LIGHT_YELLOW_BG, LIGHT_YELLOW_BORDER, 1)
    add_text_box(slide5, Inches(0.4), Inches(5.1), Inches(12.5), Inches(1.75), [
        ("UN Sustainable Development Goals & National Coal Target:", True, 13, CRIMSON, 2),
        ("• SDG 3 (Good Health) | SDG 8 (Decent Work) | SDG 9 (Industry & Innovation) | SDG 12 (Responsible Production).", True, 10.5, BLACK, 2),
        ("• Alignment with India's Goal: Supports Coal India's mission of producing 1.5 Billion Tons of Coal by 2030 safely.", False, 10.5, BLACK, 0)
    ])

    add_footer(slide5, 5)

    # =========================================================================
    # SLIDE 6: RESEARCH AND REFERENCES
    # =========================================================================
    slide6 = prs.slides[5]
    for shape in list(slide6.shapes):
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

    add_card_box(slide6, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), WHITE, BLACK, 2)
    add_text_box(slide6, Inches(0.3), Inches(0.15), Inches(1.2), Inches(0.45), [("MineNova6", True, 14, BLACK, 0, PP_ALIGN.CENTER)])

    add_text_box(slide6, Inches(2.0), Inches(0.1), Inches(6.0), Inches(0.5), [("RESEARCH AND REFERENCES", True, 24, BLACK, 0, PP_ALIGN.CENTER)])
    add_pill_badge(slide6, Inches(8.2), Inches(0.15), Inches(1.4), Inches(0.4), "MARKET & BOM", BLACK, 11)

    # Left Side Research & BOM Table
    add_card_box(slide6, Inches(0.3), Inches(0.75), Inches(6.5), Inches(6.2), WHITE, DARK_GRAY, 1)
    add_text_box(slide6, Inches(0.4), Inches(0.85), Inches(6.3), Inches(5.9), [
        ("Geotechnical Research & Market Economics:", True, 13, BLUE_HEADER, 2),
        ("• DGMS Strata Management Plan (SMP) Technical Circulars & CSIR-CIMFR Depillaring Stress Studies.\n", False, 10, BLACK, 2),
        ("• TAM: ₹15,000 Cr ($1.8B) | SAM: ₹4,500 Cr (CIL & SCCL Mines) | SOM: ₹450 Cr (High-Risk Panels).\n\n", False, 10, BLACK, 2),
        ("Itemized BOM Unit Economics (₹1,590 per Node):", True, 12, CRIMSON, 2),
        ("1. ESP32 32-bit MCU Board ➔ ₹450", False, 9.5, BLACK, 1),
        ("2. SX1276 LoRa 868MHz Transceiver ➔ ₹350", False, 9.5, BLACK, 1),
        ("3. MPU6050 Motion Sensor ➔ ₹150", False, 9.5, BLACK, 1),
        ("4. Linear String Potentiometer (0-50mm Sag) ➔ ₹300", False, 9.5, BLACK, 1),
        ("5. HX711 Load Cell Amp & Sensor (0-200kN) ➔ ₹250", False, 9.5, BLACK, 1),
        ("6. Polycarbonate Enclosure & PCB ➔ ₹90", False, 9.5, BLACK, 0)
    ])

    # Right Side References & Live Links
    add_card_box(slide6, Inches(7.0), Inches(0.75), Inches(6.0), Inches(6.2), LIGHT_BLUE_BG, LIGHT_BLUE_BORDER, 1)
    add_text_box(slide6, Inches(7.1), Inches(0.85), Inches(5.8), Inches(5.9), [
        ("Technical References & Project Links:", True, 13, BLUE_HEADER, 2),
        ("Hardware & Standards References:\n", True, 11, BLACK, 1),
        ("• Semtech SX1276 LoRa 868MHz Chirp Spread Spectrum Technical Datasheet.", False, 10, BLACK, 1),
        ("• IS/IEC 60079 Explosive Atmospheres & Intrinsically Safe (IS Ex 'd') Standard.\n\n", False, 10, BLACK, 2),
        ("Software & AI Model References:\n", True, 11, BLACK, 1),
        ("• scikit-learn Random Forest Regressor & Classifier Ensemble Documentation.", False, 10, BLACK, 1),
        ("• Python FastAPI Async ASGI & SQLAlchemy ORM Time-Series Architecture.\n\n", False, 10, BLACK, 2),
        ("Official Project Live Links:\n", True, 12, CRIMSON, 2),
        ("🌐 Live Web Dashboard: https://mineguard-ai.vercel.app", True, 10.5, BLUE_HEADER, 2),
        ("🐙 GitHub Repository: https://github.com/sharequesyed/MineGuard-AI", True, 10.5, BLUE_HEADER, 0)
    ])

    add_footer(slide6, 6)

    prs.save(output_path)
    print(f"Successfully generated complete senior-style SIH presentation at:\n{output_path}")

if __name__ == '__main__':
    build_presentation()
