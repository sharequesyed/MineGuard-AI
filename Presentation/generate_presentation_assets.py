import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dir = r"c:\Shareque Coding\SIH 2026\project 2\MineNova6\Presentation\assets"
os.makedirs(output_dir, exist_ok=True)

def generate_slide1_hero():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#0F172A')
    
    # Outer box
    rect = patches.FancyBboxPatch((0.05, 0.08), 0.9, 0.84, boxstyle="round,pad=0.03", 
                                fc='#1E293B', ec='#00A8E8', lw=2)
    ax.add_patch(rect)
    
    # Title badge
    badge = patches.FancyBboxPatch((0.2, 0.72), 0.6, 0.14, boxstyle="round,pad=0.02", 
                                 fc='#00A8E8', ec='none')
    ax.add_patch(badge)
    ax.text(0.5, 0.79, "SMART INDIA HACKATHON 2026", color='white', fontsize=18, 
            fontweight='bold', ha='center', va='center')
    
    # Details
    ax.text(0.1, 0.60, "Problem Statement ID:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.38, 0.60, "SIH26025", color='#38BDF8', fontsize=13, fontweight='bold')
    
    ax.text(0.1, 0.48, "Problem Statement Title:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.38, 0.48, "Development of an AI-enabled Low Cost Real Time Mine Subsidence\nMonitoring, Prediction & Early Warning System for Underground Coal Mines", 
            color='white', fontsize=11, fontweight='bold', va='top')
    
    ax.text(0.1, 0.32, "Theme:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.22, 0.32, "Smart Automation / Safety", color='#F59E0B', fontsize=12, fontweight='bold')
    
    ax.text(0.52, 0.32, "PS Category:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.68, 0.32, "Software & Hardware", color='#10B981', fontsize=12, fontweight='bold')
    
    ax.text(0.1, 0.20, "Team ID:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.22, 0.20, "SIH2026-MINENOVA6", color='#E2E8F0', fontsize=12)
    
    ax.text(0.52, 0.20, "Team Name:", color='#94A3B8', fontsize=12, fontweight='bold')
    ax.text(0.68, 0.20, "MineNova6", color='#38BDF8', fontsize=14, fontweight='bold')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    path = os.path.join(output_dir, "slide1_title_hero.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

def generate_slide2_prototype():
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    
    # 3 Column Cards
    titles = ["1. Worker Mobile App", "2. ESP32 LoRa Hardware Node", "3. Command Center Dashboard"]
    subtitles = ["Shift Details, Voice Log, Sirens", "MPU6050, String Pot, Load Cell", "Live Telemetry, Leaflet Map, AI Risk"]
    colors = ['#0284C7', '#D97706', '#059669']
    
    for i in range(3):
        x = 0.03 + i * 0.32
        rect = patches.FancyBboxPatch((x, 0.1), 0.30, 0.8, boxstyle="round,pad=0.02", 
                                    fc='white', ec=colors[i], lw=2)
        ax.add_patch(rect)
        
        # Header banner inside card
        header = patches.FancyBboxPatch((x + 0.01, 0.78), 0.28, 0.1, boxstyle="round,pad=0.01", 
                                      fc=colors[i], ec='none')
        ax.add_patch(header)
        ax.text(x + 0.15, 0.83, titles[i], color='white', fontsize=12, fontweight='bold', ha='center', va='center')
        ax.text(x + 0.15, 0.73, subtitles[i], color='#64748B', fontsize=9, ha='center', va='center')
        
        # Diagram elements inside card
        if i == 0:
            app_box = patches.FancyBboxPatch((x + 0.05, 0.2), 0.20, 0.48, boxstyle="round,pad=0.01", fc='#E0F2FE', ec='#0284C7', lw=1.5)
            ax.add_patch(app_box)
            ax.text(x + 0.15, 0.58, "📱 MineGuard Mobile", color='#0369A1', fontsize=10, fontweight='bold', ha='center')
            ax.text(x + 0.15, 0.48, "• Shift Logs & Tasks\n• Smart Voice Controls\n• Instant Siren Buzz\n• 10+ Languages", 
                    color='#334155', fontsize=8.5, ha='center')
        elif i == 1:
            hw_box = patches.FancyBboxPatch((x + 0.05, 0.2), 0.20, 0.48, boxstyle="round,pad=0.01", fc='#FEF3C7', ec='#D97706', lw=1.5)
            ax.add_patch(hw_box)
            ax.text(x + 0.15, 0.58, "📟 ESP32 LoRa Node", color='#92400E', fontsize=10, fontweight='bold', ha='center')
            ax.text(x + 0.15, 0.48, "• MPU6050 (Tilt & Accel)\n• String Pot (Displacement)\n• Load Cell (Prop Stress)\n• 868MHz SX1276 LoRa", 
                    color='#334155', fontsize=8.5, ha='center')
        else:
            dash_box = patches.FancyBboxPatch((x + 0.05, 0.2), 0.20, 0.48, boxstyle="round,pad=0.01", fc='#ECFDF5', ec='#059669', lw=1.5)
            ax.add_patch(dash_box)
            ax.text(x + 0.15, 0.58, "💻 Web Command Center", color='#065F46', fontsize=10, fontweight='bold', ha='center')
            ax.text(x + 0.15, 0.48, "• Leaflet Underground Map\n• 60 FPS Recharts Graphs\n• Random Forest AI Engine\n• Auto DGMS PDF Export", 
                    color='#334155', fontsize=8.5, ha='center')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    path = os.path.join(output_dir, "slide2_prototype_diagram.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

def generate_slide3_architecture():
    fig, ax = plt.subplots(figsize=(14, 7), dpi=300)
    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#0F172A')
    
    ax.text(0.5, 0.94, "MINEGUARD AI — TECHNICAL APPROACH & SYSTEM ARCHITECTURE", 
            color='#38BDF8', fontsize=15, fontweight='bold', ha='center')
    
    # 7 Core Pipeline Modules
    modules = [
        ("1. Underground Seam Sensors", "ESP32 + LoRa 868MHz\nMPU6050, String Pot, Load Cell", 0.05, 0.55, '#38BDF8'),
        ("2. LoRa Mesh Gateway", "P2P Wireless Mesh Relay\nOffline Fallback Buffer", 0.28, 0.55, '#F59E0B'),
        ("3. FastAPI REST/WS Backend", "Python Async ASGI Engine\nSQLAlchemy / SQLite / Timescale", 0.51, 0.55, '#10B981'),
        ("4. AI Risk Engine", "Random Forest Regressor\n5-min Velocity Rate (Δdisp/Δt)", 0.74, 0.55, '#EF4444'),
        ("5. Manual Logs & OCR", "Paper Logbook Digitization\nSmart Voice Multi-Lang Control", 0.16, 0.18, '#8B5CF6'),
        ("6. Shift Supervisor Web App", "React 18 + Tailwind + Recharts\nLeaflet Underground Map & Sirens", 0.51, 0.18, '#06B6D4'),
        ("7. Operator Mobile App", "Flutter / PWA Cross-Platform\nOffline Cache & Siren Buzz", 0.74, 0.18, '#EC4899'),
    ]
    
    for title, desc, x, y, col in modules:
        rect = patches.FancyBboxPatch((x, y), 0.20, 0.30, boxstyle="round,pad=0.02", 
                                    fc='#1E293B', ec=col, lw=2)
        ax.add_patch(rect)
        ax.text(x + 0.10, y + 0.24, title, color=col, fontsize=10.5, fontweight='bold', ha='center')
        ax.text(x + 0.10, y + 0.12, desc, color='#CBD5E1', fontsize=8.5, ha='center', va='center')
        
    # Arrows connecting flow
    arrow_style = dict(arrowstyle="->", color='#38BDF8', lw=2.5, mutation_scale=15)
    ax.annotate("", xy=(0.28, 0.70), xytext=(0.25, 0.70), arrowprops=arrow_style)
    ax.annotate("", xy=(0.51, 0.70), xytext=(0.48, 0.70), arrowprops=arrow_style)
    ax.annotate("", xy=(0.74, 0.70), xytext=(0.71, 0.70), arrowprops=arrow_style)
    
    ax.annotate("", xy=(0.51, 0.33), xytext=(0.36, 0.33), arrowprops=arrow_style)
    ax.annotate("", xy=(0.61, 0.55), xytext=(0.61, 0.48), arrowprops=arrow_style)
    ax.annotate("", xy=(0.84, 0.48), xytext=(0.84, 0.55), arrowprops=arrow_style)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    path = os.path.join(output_dir, "slide3_technical_architecture.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

def generate_slide4_feasibility():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    
    # Left: Market Growth Bar Chart
    years = ['2022', '2024', '2026 (Est)', '2028 (Proj)', '2030 (Proj)']
    market_val = [4.2, 5.8, 7.5, 9.8, 12.5]
    
    bars = ax1.bar(years, market_val, color=['#94A3B8', '#64748B', '#0284C7', '#0369A1', '#075985'], width=0.55)
    ax1.set_title("Global Mining Tech Market ($ Billion USD)\nCAGR Growth: 8.1%", fontsize=11, fontweight='bold', color='#1E293B')
    ax1.set_ylabel("$ Billions", fontsize=9.5, color='#475569')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    ax1.set_facecolor('white')
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.2, f"${height}B", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0F172A')

    # Right: TAM / SAM / SOM Breakdown
    sectors = ['TAM (Global)', 'SAM (Indian Coal)', 'SOM (High Risk)']
    values = [77190, 23157, 1158] # in Crores INR
    
    bars2 = ax2.barh(sectors, values, color=['#0F172A', '#0284C7', '#10B981'], height=0.5)
    ax2.set_title("Addressable Market Opportunity (INR Crores)", fontsize=11, fontweight='bold', color='#1E293B')
    ax2.set_xlabel("₹ Crores", fontsize=9.5, color='#475569')
    ax2.grid(axis='x', linestyle='--', alpha=0.5)
    ax2.set_facecolor('white')
    
    for bar in bars2:
        width = bar.get_width()
        ax2.text(width + 1500, bar.get_y() + bar.get_height()/2., f"₹{width:,} Cr", ha='left', va='center', fontsize=8.5, fontweight='bold', color='#0F172A')

    plt.tight_layout()
    path = os.path.join(output_dir, "slide4_feasibility_market_chart.png")
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

def generate_slide5_stakeholder_flow():
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    fig.patch.set_facecolor('#F1F5F9')
    ax.set_facecolor('#F1F5F9')
    
    ax.text(0.5, 0.90, "STAKEHOLDER IMPACT & HAZARD RESPONSE SCENARIO FLOW", 
            color='#1E3A8A', fontsize=14, fontweight='bold', ha='center')
    
    steps = [
        ("Step 1: Mine Operator", "Detects strata movement\nor reports hazard via\nsmart voice UI", 0.04, '#0284C7'),
        ("Step 2: AI Risk Engine", "Processes 10 parameters,\ncalculates 5-min velocity,\nassigns risk level", 0.28, '#D97706'),
        ("Step 3: Shift Supervisor", "Receives web map alert,\napproves evacuation &\nsmits SMP handover", 0.52, '#059669'),
        ("Step 4: DGMS & Mgmt", "Accesses real-time data\nanalytics & automated\ncompliance PDF logs", 0.76, '#7C3AED'),
    ]
    
    for title, desc, x, col in steps:
        rect = patches.FancyBboxPatch((x, 0.25), 0.20, 0.50, boxstyle="round,pad=0.02", 
                                    fc='white', ec=col, lw=2)
        ax.add_patch(rect)
        ax.text(x + 0.10, 0.65, title, color=col, fontsize=10.5, fontweight='bold', ha='center')
        ax.text(x + 0.10, 0.45, desc, color='#334155', fontsize=8.5, ha='center', va='center')
        
    # Arrows
    arrow_style = dict(arrowstyle="->", color='#1E3A8A', lw=2.5, mutation_scale=15)
    ax.annotate("", xy=(0.28, 0.50), xytext=(0.24, 0.50), arrowprops=arrow_style)
    ax.annotate("", xy=(0.52, 0.50), xytext=(0.48, 0.50), arrowprops=arrow_style)
    ax.annotate("", xy=(0.76, 0.50), xytext=(0.72, 0.50), arrowprops=arrow_style)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    path = os.path.join(output_dir, "slide5_stakeholder_impact_flow.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

def generate_slide6_market_economics():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#0F172A')
    ax.set_facecolor('#0F172A')
    
    ax.text(0.5, 0.90, "TAM / SAM / SOM MARKET SIZING & UNIT ECONOMICS", 
            color='#38BDF8', fontsize=14, fontweight='bold', ha='center')
    
    # Concentric circles for TAM/SAM/SOM
    circle1 = patches.Circle((0.25, 0.45), 0.35, fc='#1E293B', ec='#38BDF8', lw=2)
    circle2 = patches.Circle((0.25, 0.45), 0.25, fc='#0284C7', ec='white', lw=1.5)
    circle3 = patches.Circle((0.25, 0.45), 0.14, fc='#10B981', ec='white', lw=1.5)
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    
    ax.text(0.25, 0.45, "SOM\n₹1,158 Cr", color='white', fontsize=9, fontweight='bold', ha='center', va='center')
    ax.text(0.25, 0.63, "SAM: ₹23,157 Cr", color='white', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(0.25, 0.74, "TAM: ₹77,190 Cr", color='#38BDF8', fontsize=10, fontweight='bold', ha='center')
    
    # Unit economics summary box
    rect = patches.FancyBboxPatch((0.55, 0.15), 0.40, 0.65, boxstyle="round,pad=0.02", 
                                fc='#1E293B', ec='#F59E0B', lw=2)
    ax.add_patch(rect)
    ax.text(0.75, 0.72, "💰 Mid-Sized Mine Unit Economics", color='#F59E0B', fontsize=11, fontweight='bold', ha='center')
    
    text_content = (
        "• Number of Workers: 500\n"
        "• Safety Nodes (100 @ ₹728): ₹72,800\n"
        "• Danger Nodes (100 @ ₹720): ₹77,800\n"
        "• Installation Fees (200 @ ₹980): ₹1,96,000\n"
        "• Service & Audits (Monthly): ₹5,000\n"
        "• Total Revenue (Year 1): ₹846,600\n"
        "• Software Profit Margin: 85%\n"
        "• Hardware Profit Margin: 30%"
    )
    ax.text(0.58, 0.42, text_content, color='#E2E8F0', fontsize=8.5, va='center')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    path = os.path.join(output_dir, "slide6_market_economics_references.png")
    plt.tight_layout()
    plt.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {path}")

if __name__ == '__main__':
    generate_slide1_hero()
    generate_slide2_prototype()
    generate_slide3_architecture()
    generate_slide4_feasibility()
    generate_slide5_stakeholder_flow()
    generate_slide6_market_economics()
    print("All slide visual reference images generated successfully!")
