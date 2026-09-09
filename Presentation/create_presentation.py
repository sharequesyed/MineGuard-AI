import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_sih_presentation():
    prs = Presentation()
    # Widescreen 16:9 aspect ratio
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette
    DARK_SLATE = RGBColor(15, 23, 42)      # #0F172A
    INDIGO = RGBColor(79, 70, 229)        # #4F46E5
    CYAN = RGBColor(6, 182, 212)          # #06B6D4
    LIGHT_BG = RGBColor(248, 250, 252)    # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
    TEXT_DARK = RGBColor(30, 41, 59)      # #1E293B
    TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
    EMERALD = RGBColor(16, 185, 129)      # #10B981
    ROSE = RGBColor(239, 68, 68)          # #EF4444

    blank_slide_layout = prs.slide_layouts[6]

    # Helper: Set background color
    def set_bg(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    # Helper: Add Header
    def add_header(slide, title_text, category_text="SIH 2026 | PS ID: SIH26025"):
        # Category Pill
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf = cat_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = category_text.upper()
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = INDIGO
        
        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = DARK_SLATE

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Theme Hero)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s1, DARK_SLATE)

    # Decorative Card Box
    card1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.1))
    card1.fill.solid()
    card1.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card1.line.color.rgb = INDIGO

    # SIH Badge
    badge_box = s1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(8), Inches(0.4))
    p = badge_box.text_frame.paragraphs[0]
    p.text = "SMART INDIA HACKATHON 2026 | PROBLEM STATEMENT: SIH26025"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN

    # Main Project Title
    t_box = s1.shapes.add_textbox(Inches(1.5), Inches(2.1), Inches(10), Inches(1.2))
    p = t_box.text_frame.paragraphs[0]
    p.text = "MineGuard AI"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)

    # Subtitle
    sub_box = s1.shapes.add_textbox(Inches(1.5), Inches(3.3), Inches(10), Inches(1.0))
    tf = sub_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "AI-Enabled Low-Cost Real-Time Mine Subsidence Monitoring, Prediction & Early Warning System"
    p.font.size = Pt(18)
    p.font.color.rgb = RGBColor(203, 213, 225)

    # Team Credits Footer
    team_box = s1.shapes.add_textbox(Inches(1.5), Inches(4.8), Inches(10), Inches(0.8))
    tf = team_box.text_frame
    p = tf.paragraphs[0]
    p.text = "Team MineNova6: Shareque (Lead) | Monika | Aditya | Farhan | Atharva | Affan"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = EMERALD

    # =========================================================================
    # SLIDE 2: Problem Statement & Industry Impact
    # =========================================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s2, LIGHT_BG)
    add_header(s2, "1. The Underground Coal Mining Subsidence Challenge")

    # 3 Problem Cards
    cards_data_s2 = [
        ("40%+ Mining Fatalities", "Roof falls & rock caving account for over 40% of fatalities in Indian bord-and-pillar coal mines (Jharia & Raniganj coalfields).", ROSE),
        ("High Cost & Cabling Failure", "Existing cabled monitoring costs >₹5 Lakhs/panel. Cables snap during rock movements, disabling safety systems when needed most.", DARK_SLATE),
        ("Zero Pre-Collapse Warning", "Traditional systems rely on static thresholds that trigger too late, leaving miners zero evacuation time prior to structural roof collapse.", INDIGO)
    ]

    for idx, (title, desc, color) in enumerate(cards_data_s2):
        left = Inches(0.8 + idx * 3.9)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), Inches(3.6), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(226, 232, 240)

        # Header bar
        hbar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, Inches(1.8), Inches(3.6), Inches(0.1))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = color
        hbar.line.fill.background()

        # Text
        tb = s2.shapes.add_textbox(left + Inches(0.2), Inches(2.1), Inches(3.2), Inches(4.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(14)

    # =========================================================================
    # SLIDE 3: Proposed Solution — MineGuard AI
    # =========================================================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s3, LIGHT_BG)
    add_header(s3, "2. Proposed Solution — MineGuard AI Ecosystem")

    solution_pillars = [
        ("Wireless ESP32 LoRa Mesh", "₹1,590 low-cost wireless nodes operating on 868MHz frequency band, penetrating rock strata without cables.", INDIGO),
        ("AI Subsidence Predictor", "Random Forest ML engine correlating 10 parameters (42% weight on 5-min displacement velocity Δdisp/Δt) to detect pre-collapse deformation.", CYAN),
        ("Command Center Dashboard", "React + Vite light-theme web application with real-time Leaflet mine map, risk gauges, and dynamic trend curves.", EMERALD),
        ("Dual Fail-Safe Alarm Sirens", "1kHz local ESP32 buzzer sirens + real-time dashboard notifications + automated alert logging.", ROSE)
    ]

    for idx, (title, desc, color) in enumerate(solution_pillars):
        row = idx // 2
        col = idx % 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.8 + row * 2.5)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.6), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(226, 232, 240)

        tb = s3.shapes.add_textbox(left + Inches(0.3), top + Inches(0.2), Inches(5.0), Inches(1.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(8)

    # =========================================================================
    # SLIDE 4: End-to-End System Architecture
    # =========================================================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s4, LIGHT_BG)
    add_header(s4, "3. System Architecture & Data Flow")

    # Flow Steps
    steps = [
        ("1. Sensors", "MPU6050 Tilt/Vib\nString Pot\nLoad Cell"),
        ("2. ESP32 Node", "ADC Sampling\nLoRa Packet Payload"),
        ("3. LoRa Link", "868 MHz ISM\nLong Range Wireless"),
        ("4. Gateway", "SX1276 Receiver\nHTTP Forwarder"),
        ("5. FastAPI Backend", "REST API\nSQLite/PostgreSQL"),
        ("6. AI Risk Engine", "Random Forest\nRisk Score 0-100"),
        ("7. Command Center", "React Dashboard\nEarly Warning Sirens")
    ]

    for idx, (title, desc) in enumerate(steps):
        left = Inches(0.6 + idx * 1.75)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(2.2), Inches(1.6), Inches(3.8))
        card.fill.solid()
        card.fill.fore_color.rgb = DARK_SLATE if idx in [4, 5] else CARD_BG
        card.line.color.rgb = INDIGO

        tb = s4.shapes.add_textbox(left + Inches(0.1), Inches(2.4), Inches(1.4), Inches(3.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255) if idx in [4, 5] else INDIGO

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = RGBColor(203, 213, 225) if idx in [4, 5] else TEXT_MUTED
        p2.space_before = Pt(10)

    # Tech Stack Footer Banner
    tech_box = s4.shapes.add_textbox(Inches(0.6), Inches(6.3), Inches(12.0), Inches(0.6))
    tf = tech_box.text_frame
    p = tf.paragraphs[0]
    p.text = "TECH STACK: React + Vite | Tailwind CSS v4 | Python FastAPI | scikit-learn | Leaflet Maps | ESP32 C++ Arduino"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 5: Key Technical Innovations & SIH Demo
    # =========================================================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s5, LIGHT_BG)
    add_header(s5, "4. Technical Innovation & Demonstration Features")

    innovations = [
        ("Geotechnical Velocity Weighting", "Instead of static limits, model evaluates 5-min displacement velocity (Δdisp/Δt) and tilt rate, detecting pre-failure roof sagging in Stage 1."),
        ("SIH Emergency Simulator", "Includes an interactive SIH Demo controller (Normal State, Warning Drift, Subsidence Event) allowing judges to trigger live emergency escalation on stage."),
        ("Multi-Device Synchronized Telemetry", "Uses Global Epoch Time seeding and BroadcastChannel API so all judges' phones, laptops, and tablets display identical live numbers."),
        ("DGMS Compliance Ready", "Designed around Directorate General of Mines Safety guidelines with 3.3V intrinsically safe circuit principles and dual-channel warning alarms.")
    ]

    for idx, (title, desc) in enumerate(innovations):
        top = Inches(1.8 + idx * 1.3)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.733), Inches(1.15))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(226, 232, 240)

        tb = s5.shapes.add_textbox(Inches(1.1), top + Inches(0.15), Inches(11.0), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = INDIGO

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 6: Cost Analysis & Feasibility
    # =========================================================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s6, LIGHT_BG)
    add_header(s6, "5. Feasibility, Low-Cost Analysis & Scalability")

    # Left: Cost Table Card
    card_left = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = RGBColor(226, 232, 240)

    tb = s6.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Ultra Low-Cost Hardware BOM (Per Node):"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE

    bom_items = [
        "ESP32 Microcontroller: ₹450",
        "SX1276 LoRa Radio (868MHz): ₹350",
        "MPU6050 6-Axis Tilt/Vib Sensor: ₹180",
        "Linear Displacement String Pot: ₹80",
        "HX711 + Load Cell: ₹180",
        "DHT22 Temp/Humidity Sensor: ₹160",
        "LiFePO4 Battery + TP4056 Charger: ₹150",
        "TOTAL COST PER NODE: ~ ₹1,590 ($19 USD)"
    ]
    for item in bom_items:
        p2 = tf.add_paragraph()
        p2.text = "• " + item
        p2.font.size = Pt(12)
        p2.font.bold = "TOTAL" in item
        p2.font.color.rgb = EMERALD if "TOTAL" in item else TEXT_DARK
        p2.space_before = Pt(6)

    # Right: Scalability Card
    card_right = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.0))
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = RGBColor(226, 232, 240)

    tb2 = s6.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "Commercial Advantage & Scalability:"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = INDIGO

    scale_points = [
        ("96% Cost Reduction", "Commercial cabled sensors cost ₹50,000+ per unit. MineGuard AI delivers a full node array at ₹1,590/node."),
        ("Seamless PostgreSQL Scaling", "SQLAlchemy ORM allows instant migration from SQLite to PostgreSQL with TimescaleDB time-series indexing for 100+ mine nodes."),
        ("Vercel & Cloud Hosted", "Web Command Center hosted on Vercel with instant mobile and laptop access for control room engineers.")
    ]
    for stitle, sdesc in scale_points:
        p2 = tf2.add_paragraph()
        p2.text = stitle
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = DARK_SLATE
        p2.space_before = Pt(10)

        p3 = tf2.add_paragraph()
        p3.text = sdesc
        p3.font.size = Pt(11)
        p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 7: Team & Conclusion (Dark Theme Ending)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    set_bg(s7, DARK_SLATE)

    # Header
    tb_end = s7.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(0.8))
    tf = tb_end.text_frame
    p = tf.paragraphs[0]
    p.text = "Team MineNova6 — Ready for Deployment"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)

    # 6 Team Member Boxes
    team_members = [
        ("Shareque", "Team Leader & Tech Lead\nSystem Integration & Architecture"),
        ("Monika", "Research & Documentation Lead\nGeotechnical Domain Analysis"),
        ("Aditya", "UI/UX Design Lead\nDesign System & Glassmorphism"),
        ("Farhan", "Frontend React Engineer\nRecharts & Leaflet Map Integration"),
        ("Atharva", "Backend FastAPI Lead\nREST APIs & Database ORM"),
        ("Affan", "AI/ML & Data Lead\nRandom Forest ML Pipeline")
    ]

    for idx, (name, role) in enumerate(team_members):
        row = idx // 3
        col = idx % 3
        left = Inches(1.0 + col * 3.9)
        top = Inches(2.0 + row * 2.2)

        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.6), Inches(1.9))
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(30, 41, 59)
        card.line.color.rgb = INDIGO

        tb = s7.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.2), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = CYAN

        p2 = tf.add_paragraph()
        p2.text = role
        p2.font.size = Pt(11)
        p2.font.color.rgb = RGBColor(203, 213, 225)
        p2.space_before = Pt(6)

    # Call to action footer
    cta_box = s7.shapes.add_textbox(Inches(1.0), Inches(6.4), Inches(11.333), Inches(0.6))
    tf = cta_box.text_frame
    p = tf.paragraphs[0]
    p.text = "MineGuard AI — Protecting Underground Miners in India with AI & Low-Cost Hardware"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = EMERALD
    p.alignment = PP_ALIGN.CENTER

    # Save presentation
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "MineGuard_AI_SIH2026_Internal_Presentation.pptx")
    prs.save(out_path)
    print(f"Presentation successfully created at: {out_path}")

if __name__ == '__main__':
    build_sih_presentation()
