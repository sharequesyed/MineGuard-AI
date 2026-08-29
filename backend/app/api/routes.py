from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database.session import get_db
from app.database.models import SensorNode, SensorReading, RiskPrediction, Alert
from app.models.schemas import (
    NodeSchema, SensorReadingCreate, SensorReadingResponse,
    RiskPredictionResponse, AlertSchema, DemoModeRequest
)
from app.services.risk_engine import risk_engine

router = APIRouter()

# Global state for SIH Demo Mode ('NORMAL' | 'WARNING' | 'SUBSIDENCE')
CURRENT_DEMO_MODE = "NORMAL"

@router.get("/health")
def health_check():
    return {
        "status": "HEALTHY",
        "system": "MineGuard AI Backend Engine",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "demo_mode": CURRENT_DEMO_MODE
    }

@router.get("/nodes", response_model=List[NodeSchema])
def get_nodes(db: Session = Depends(get_db)):
    nodes = db.query(SensorNode).all()
    if not nodes:
        # Fallback list if DB is not seeded yet
        return [
            {"id": "N1", "name": "Node N1 - Main Seam Entry", "location": "Panel A - North Drift", "depth": "180m", "latitude": 23.785, "longitude": 86.425, "status": "ONLINE", "last_communication": datetime.utcnow()},
            {"id": "N2", "name": "Node N2 - Pillar Line 4", "location": "Panel A - East Pillar", "depth": "210m", "latitude": 23.788, "longitude": 86.429, "status": "ONLINE", "last_communication": datetime.utcnow()},
            {"id": "N3", "name": "Node N3 - Goaf Edge South", "location": "Panel B - Active Extraction", "depth": "240m", "latitude": 23.782, "longitude": 86.432, "status": "ONLINE", "last_communication": datetime.utcnow()},
            {"id": "N4", "name": "Node N4 - Haulage Roadway", "location": "Panel B - Conveyor Belt 2", "depth": "195m", "latitude": 23.780, "longitude": 86.422, "status": "ONLINE", "last_communication": datetime.utcnow()},
            {"id": "N5", "name": "Node N5 - Roof Strata Junction", "location": "Panel C - High Stress Zone", "depth": "260m", "latitude": 23.786, "longitude": 86.436, "status": "ONLINE", "last_communication": datetime.utcnow()},
            {"id": "N6", "name": "Node N6 - Air Return Shaft", "location": "Shaft 2 - Ventilation Line", "depth": "225m", "latitude": 23.791, "longitude": 86.420, "status": "ONLINE", "last_communication": datetime.utcnow()},
        ]
    return nodes

@router.get("/nodes/{node_id}")
def get_node_details(node_id: str, db: Session = Depends(get_db)):
    node = db.query(SensorNode).filter(SensorNode.id == node_id).first()
    if not node:
        return {
            "id": node_id,
            "name": f"Node {node_id}",
            "location": "Underground Coal Seam",
            "depth": "210m",
            "status": "ONLINE",
            "battery": 94.0
        }
    latest = db.query(SensorReading).filter(SensorReading.node_id == node_id).order_by(SensorReading.timestamp.desc()).first()
    return {
        "node": node,
        "latest_reading": latest
    }

@router.post("/sensors/data", response_model=SensorReadingResponse)
def receive_sensor_data(reading: SensorReadingCreate, db: Session = Depends(get_db)):
    # 1. Store sensor reading
    db_reading = SensorReading(
        node_id=reading.node_id,
        tilt=reading.tilt,
        displacement=reading.displacement,
        crack_width=reading.crack_width,
        vibration=reading.vibration,
        load_change=reading.load_change,
        temperature=reading.temperature,
        humidity=reading.humidity,
        battery=reading.battery,
        timestamp=datetime.utcnow()
    )
    db.add(db_reading)

    # 2. Run AI risk engine evaluation
    eval_res = risk_engine.predict_risk(
        tilt=reading.tilt,
        displacement=reading.displacement,
        crack_width=reading.crack_width,
        vibration=reading.vibration,
        load_change=reading.load_change
    )

    db_pred = RiskPrediction(
        node_id=reading.node_id,
        risk_score=eval_res["risk_score"],
        risk_level=eval_res["risk_level"],
        primary_factor=eval_res["primary_factor"],
        timestamp=datetime.utcnow()
    )
    db.add(db_pred)

    # 3. Trigger alert if level is HIGH or CRITICAL
    if eval_res["risk_level"] in ["HIGH", "CRITICAL"]:
        alert = Alert(
            id=f"ALT-{int(datetime.utcnow().timestamp())}",
            node_id=reading.node_id,
            timestamp=datetime.utcnow(),
            risk_score=eval_res["risk_score"],
            risk_level=eval_res["risk_level"],
            reason=f"Accelerated Deformation on Node {reading.node_id}",
            details=f"Tilt: {reading.tilt}°, Displacement: {reading.displacement}mm, Crack: {reading.crack_width}mm"
        )
        db.add(alert)

    db.commit()
    db.refresh(db_reading)
    return db_reading

@router.get("/sensors/latest")
def get_latest_readings(db: Session = Depends(get_db)):
    readings = db.query(SensorReading).order_by(SensorReading.timestamp.desc()).limit(6).all()
    return readings

@router.get("/sensors/history")
def get_sensor_history(node_id: str = Query(None), limit: int = 30, db: Session = Depends(get_db)):
    query = db.query(SensorReading)
    if node_id:
        query = query.filter(SensorReading.node_id == node_id)
    readings = query.order_by(SensorReading.timestamp.desc()).limit(limit).all()
    return readings

@router.get("/risk")
def get_risk_evaluation(node_id: str = Query("N5"), db: Session = Depends(get_db)):
    reading = db.query(SensorReading).filter(SensorReading.node_id == node_id).order_by(SensorReading.timestamp.desc()).first()
    if not reading:
        return risk_engine.predict_risk(tilt=1.2, displacement=2.5, crack_width=0.4, vibration=0.1, load_change=5.0)
    return risk_engine.predict_risk(
        tilt=reading.tilt,
        displacement=reading.displacement,
        crack_width=reading.crack_width,
        vibration=reading.vibration,
        load_change=reading.load_change
    )

@router.get("/alerts")
def get_alerts(limit: int = 20, db: Session = Depends(get_db)):
    alerts = db.query(Alert).order_by(Alert.timestamp.desc()).limit(limit).all()
    return alerts

@router.get("/dashboard/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    active_nodes = 6
    alerts_count = db.query(Alert).filter(Alert.acknowledged == False).count()
    return {
        "overall_mine_risk_score": 18,
        "overall_mine_risk_level": "LOW",
        "active_nodes": active_nodes,
        "total_nodes": 6,
        "high_risk_zones": 0 if CURRENT_DEMO_MODE == "NORMAL" else 1,
        "active_alerts": alerts_count,
        "gateway_status": "ONLINE",
        "demo_mode": CURRENT_DEMO_MODE,
        "last_sync": datetime.utcnow().isoformat()
    }

@router.post("/demo/mode")
def set_demo_mode(req: DemoModeRequest):
    global CURRENT_DEMO_MODE
    CURRENT_DEMO_MODE = req.mode
    return {
        "success": True,
        "mode": CURRENT_DEMO_MODE,
        "message": f"SIH Demo Mode set to {CURRENT_DEMO_MODE}"
    }
