import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def update_text_frame(tf, text_runs):
    tf.clear()
    for idx, (p_text, is_bold, font_size, color_rgb, space_after, bullet) in enumerate(text_runs):
        if idx == 0 and len(tf.paragraphs) > 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        
        p.space_after = Pt(space_after)
        if bullet:
            p.level = 0
        run = p.add_run()
        run.text = p_text
        run.font.name = 'Calibri'
        run.font.size = Pt(font_size)
        run.font.bold = is_bold
        if color_rgb:
            run.font.color.rgb = color_rgb

def main():
    template_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\SIH2026-IDEA-Presentation-Format.pptx"
    output_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\MineGuard_AI_SIH2026_Official_Presentation.pptx"

    prs = pptx.Presentation(template_path)
    
    # Primary Colors
    NAVY = RGBColor(27, 54, 93)
    DARK_BLUE = RGBColor(44, 82, 130)
    CHARCOAL = RGBColor(45, 55, 72)
    CRIMSON = RGBColor(197, 48, 48)

    # -------------------------------------------------------------
    # SLIDE 1: TITLE PAGE
    # -------------------------------------------------------------
    slide1 = prs.slides[0]
    for shape in slide1.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "Problem Statement ID" in txt or "Problem Statement Title" in txt:
                runs = [
                    ("Problem Statement ID: SIH26025", True, 14, NAVY, 4, False),
                    ("Problem Statement Title: Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India", True, 12, DARK_BLUE, 6, False),
                    ("Theme: Smart Automation / Safety & Security / Disaster Management", False, 12, CHARCOAL, 4, False),
                    ("PS Category: Hardware / Software (Hybrid IoT-AI System)", False, 12, CHARCOAL, 4, False),
                    ("Team ID: SIH2026-MINENOVA6", True, 12, NAVY, 4, False),
                    ("Team Name: MineNova6", True, 14, CRIMSON, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)

    # -------------------------------------------------------------
    # SLIDE 2: IDEA TITLE & PROPOSED SOLUTION
    # -------------------------------------------------------------
    slide2 = prs.slides[1]
    for shape in slide2.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "IDEA TITLE" in txt:
                shape.text_frame.text = "MineGuard AI — Real-Time Mine Subsidence Early Warning System"
            elif "Proposed Solution" in txt:
                runs = [
                    ("Proposed Solution & Architectural Overview:", True, 13, NAVY, 3, False),
                    ("• MineGuard AI is an ultra-low-cost (₹1,590/node), wireless IoT-AI system designed to protect underground coal miners from roof collapse hazards.", False, 11, CHARCOAL, 2, False),
                    ("• Integrates ESP32 LoRa wireless sensor nodes, a Python FastAPI REST server, a Random Forest ML predictive engine, and a React 18 web command center.", False, 11, CHARCOAL, 4, False),
                    ("How It Addresses Problem Statement SIH26025:", True, 13, NAVY, 3, False),
                    ("• Replaces manual telltales and prohibitively expensive cabled systems (₹10 Lakhs/seam) with continuous 2.5s automated strata telemetry.", False, 11, CHARCOAL, 2, False),
                    ("• Evaluates 5-minute displacement and tilt velocity rates (Δdisp/Δt, Δtilt/Δt), detecting progressive strata failure in Stage 1 before roof collapse.", False, 11, CHARCOAL, 4, False),
                    ("Key Innovation & Uniqueness:", True, 13, NAVY, 3, False),
                    ("• Dynamic Rate-of-Change AI Feature Acceleration (MAE: 1.27, R²: 0.9969).", False, 11, CHARCOAL, 2, False),
                    ("• 98.8% Cost Reduction (₹11,990 complete panel setup).", False, 11, CHARCOAL, 2, False),
                    ("• Dual Edge + Cloud Failover Resilience (GPIO 12/13 sirens trigger independently during internet outages).", False, 11, CHARCOAL, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)
            elif "Your Team Name" in txt:
                shape.text_frame.text = "MineNova6"

    # -------------------------------------------------------------
    # SLIDE 3: TECHNICAL APPROACH
    # -------------------------------------------------------------
    slide3 = prs.slides[2]
    for shape in slide3.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "TECHNICAL APPROACH" in txt:
                shape.text_frame.text = "TECHNICAL APPROACH & SYSTEM ARCHITECTURE"
            elif "Technologies to be used" in txt or "Methodology" in txt:
                runs = [
                    ("Hardware Perception & Transmission Layer:", True, 13, NAVY, 2, False),
                    ("• ESP32 32-bit MCU (240MHz) + SX1276 LoRa 868MHz Chirp Spread Spectrum transceiver (2km rock strata penetration).", False, 11, CHARCOAL, 2, False),
                    ("• MPU6050 (Tilt & Vibration), Linear String Potentiometer (Sag 0-50mm), HX711 Load Cell Amp (Stress), DHT22.", False, 11, CHARCOAL, 4, False),
                    ("Backend & AI Processing Layer:", True, 13, NAVY, 2, False),
                    ("• Python FastAPI (Async ASGI event loop), Pydantic validation, SQLAlchemy ORM (SQLite / PostgreSQL+TimescaleDB).", False, 11, CHARCOAL, 2, False),
                    ("• scikit-learn Random Forest Regressor & Classifier evaluating 10 parameters (joblib serialized bundle).", False, 11, CHARCOAL, 4, False),
                    ("Frontend Presentation Layer:", True, 13, NAVY, 2, False),
                    ("• React 18 + Vite, Glassmorphism UI, Recharts 60 FPS rolling buffers, Leaflet geospatial map, BroadcastChannel sync.", False, 11, CHARCOAL, 4, False),
                    ("End-to-End Data Flow Pipeline:", True, 13, NAVY, 2, False),
                    ("• [Sensors] ──(868MHz LoRa)──► [ESP32 Gateway] ──(HTTP POST)──► [FastAPI] ──► [Random Forest ML] ──► [React Dashboard & Siren]", True, 10, CRIMSON, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)
            elif "Your Team Name" in txt:
                shape.text_frame.text = "MineNova6"

    # Add Wiring Diagram Image to Slide 3 if available
    img_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\team_sih_prep\sensor_node_wiring_diagram.jpg"
    if os.path.exists(img_path):
        slide3.shapes.add_picture(img_path, Inches(8.2), Inches(1.8), width=Inches(4.8))

    # -------------------------------------------------------------
    # SLIDE 4: FEASIBILITY AND VIABILITY
    # -------------------------------------------------------------
    slide4 = prs.slides[3]
    for shape in slide4.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "FEASIBILITY AND VIABILITY" in txt:
                shape.text_frame.text = "FEASIBILITY, RISK ANALYSIS & MITIGATION"
            elif "Analysis of the feasibility" in txt or "Potential challenges" in txt:
                runs = [
                    ("Feasibility Analysis & Manufacturing Economics:", True, 13, NAVY, 2, False),
                    ("• Economic Feasibility: ₹1,590 ($19 USD) per sensor node; ₹11,990 total for 6 nodes + 1 gateway (98.8% cost saving vs ₹10 Lakhs legacy systems). Immediate ROI (<1 month).", False, 11, CHARCOAL, 2, False),
                    ("• Technical Feasibility: Low-power 3.3V DC logic; 3.7V LiFePO4 battery lasts 6+ months; 868MHz LoRa penetrates solid coal/rock strata without cables.", False, 11, CHARCOAL, 4, False),
                    ("Potential Challenges & Technical Risks:", True, 13, NAVY, 2, False),
                    ("1. Explosive Firedamp / Methane Atmosphere in coal mines.", False, 11, CHARCOAL, 1, False),
                    ("2. Severe RF Attenuation through thick rock strata & curved galleries.", False, 11, CHARCOAL, 1, False),
                    ("3. Central Internet / Server Connection Outages.", False, 11, CHARCOAL, 4, False),
                    ("Risk Mitigation Strategies:", True, 13, NAVY, 2, False),
                    ("• Mitigation 1: IP67 flameproof polycarbonate enclosure complying with DGMS Intrinsically Safe (IS Ex 'd') standards.", False, 11, CHARCOAL, 2, False),
                    ("• Mitigation 2: 868MHz Chirp Spread Spectrum (CSS) frequency modulation designed for non-line-of-sight underground penetration.", False, 11, CHARCOAL, 2, False),
                    ("• Mitigation 3: Edge Failover Redundancy — Gateway MCU independently fires GPIO 12/13 buzzer sirens and logs data over USB Serial bridge.", False, 11, CHARCOAL, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)
            elif "Your Team Name" in txt:
                shape.text_frame.text = "MineNova6"

    # Add Product Image to Slide 4 if available
    product_img_path = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\team_sih_prep\sensor_node_final_product.jpg"
    if os.path.exists(product_img_path):
        slide4.shapes.add_picture(product_img_path, Inches(8.2), Inches(1.8), width=Inches(4.8))

    # -------------------------------------------------------------
    # SLIDE 5: IMPACT AND BENEFITS
    # -------------------------------------------------------------
    slide5 = prs.slides[4]
    for shape in slide5.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "IMPACT AND BENEFITS" in txt:
                shape.text_frame.text = "POTENTIAL IMPACT AND MULTI-SECTOR BENEFITS"
            elif "Potential impact on the target audience" in txt or "Benefits of the solution" in txt:
                runs = [
                    ("Impact on Target Audience (300,000+ Underground Miners & Engineers):", True, 13, NAVY, 2, False),
                    ("• Primary Users: Strata Control Engineers, Mine Managers, Shift Safety Officers, and Control Room Operators in CIL subsidiaries (ECL, BCCL, CCL, SECL, WCL) & SCCL.", False, 11, CHARCOAL, 2, False),
                    ("• Directly eliminates fatal casualties caused by unpredicted roof falls during depillaring and longwall extraction.", False, 11, CHARCOAL, 4, False),
                    ("Social Benefits:", True, 13, NAVY, 2, False),
                    ("• Establishes a zero-casualty safety culture in Indian coal mining, improving miner morale and family security.", False, 11, CHARCOAL, 3, False),
                    ("Economic Benefits:", True, 13, NAVY, 2, False),
                    ("• Saves coal mining companies multi-crores in damaged hydraulic supports, continuous miners, mine closure penalties, and legal compensation.", False, 11, CHARCOAL, 3, False),
                    ("Environmental & Operational Regulatory Benefits:", True, 13, NAVY, 2, False),
                    ("• Full alignment with Directorate General of Mines Safety (DGMS) strata management guidelines.", False, 11, CHARCOAL, 2, False),
                    ("• Prevents surface land fissuring, groundwater depletion, and environmental degradation caused by unmonitored surface subsidence.", False, 11, CHARCOAL, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)
            elif "Your Team Name" in txt:
                shape.text_frame.text = "MineNova6"

    # -------------------------------------------------------------
    # SLIDE 6: RESEARCH AND REFERENCES
    # -------------------------------------------------------------
    slide6 = prs.slides[5]
    for shape in slide6.shapes:
        if shape.has_text_frame:
            txt = shape.text.strip()
            if "RESEARCH" in txt:
                shape.text_frame.text = "RESEARCH, REFERENCES & PROJECT LINKS"
            elif "Details / Links" in txt:
                runs = [
                    ("Geotechnical & Mining Engineering Research References:", True, 13, NAVY, 2, False),
                    ("• Directorate General of Mines Safety (DGMS) Strata Management & Convergence Monitoring Technical Circulars.", False, 11, CHARCOAL, 2, False),
                    ("• CSIR-Central Institute of Mining and Fuel Research (CIMFR) studies on Bord-and-Pillar Depillaring Stress Dynamics.", False, 11, CHARCOAL, 4, False),
                    ("Hardware & Standards References:", True, 13, NAVY, 2, False),
                    ("• Semtech SX1276 LoRa 868MHz Chirp Spread Spectrum (CSS) Technical Datasheet.", False, 11, CHARCOAL, 2, False),
                    ("• IS/IEC 60079 Standard for Explosive Atmospheres & Intrinsically Safe (IS) Electrical Apparatus.", False, 11, CHARCOAL, 4, False),
                    ("Software & Machine Learning References:", True, 13, NAVY, 2, False),
                    ("• scikit-learn Random Forest Regressor & Classifier Ensemble Documentation.", False, 11, CHARCOAL, 2, False),
                    ("• FastAPI Asynchronous ASGI Framework & SQLAlchemy Time-Series ORM Architecture.", False, 11, CHARCOAL, 4, False),
                    ("Live Project Deployment & Source Code Links:", True, 13, NAVY, 2, False),
                    ("• Live Vercel Web Dashboard: https://mineguard-ai.vercel.app", True, 11, CRIMSON, 2, False),
                    ("• Official GitHub Repository: https://github.com/sharequesyed/MineGuard-AI", True, 11, CRIMSON, 2, False),
                ]
                update_text_frame(shape.text_frame, runs)
            elif "Your Team Name" in txt:
                shape.text_frame.text = "MineNova6"

    # -------------------------------------------------------------
    # REMOVE SLIDE 7 (Instructions slide, per SIH rules limit max 6 slides)
    # -------------------------------------------------------------
    if len(prs.slides) >= 7:
        rId = prs.slides._sldIdLst[6].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[6]

    prs.save(output_path)
    print(f"Successfully generated official SIH 2026 presentation at:\n{output_path}")

if __name__ == "__main__":
    main()
