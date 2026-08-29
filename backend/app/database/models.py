from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class SensorNode(Base):
    __tablename__ = "sensor_nodes"

    id = Column(String, primary_key=True, index=True) # e.g. "N1"
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    depth = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    status = Column(String, default="ONLINE")
    last_communication = Column(DateTime, default=datetime.utcnow)

    readings = relationship("SensorReading", back_populates="node")
    predictions = relationship("RiskPrediction", back_populates="node")
    alerts = relationship("Alert", back_populates="node")

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    node_id = Column(String, ForeignKey("sensor_nodes.id"), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    tilt = Column(Float, nullable=False)           # Pitch/roll in degrees
    displacement = Column(Float, nullable=False)   # Roof displacement in mm
    crack_width = Column(Float, nullable=False)    # Crack growth in mm
    vibration = Column(Float, nullable=False)      # Peak ground acceleration in g
    load_change = Column(Float, nullable=False)    # Stress change in kg
    temperature = Column(Float, nullable=False)    # Ambient temp in °C
    humidity = Column(Float, nullable=False)       # Relative humidity %
    battery = Column(Float, default=100.0)         # Node battery %

    node = relationship("SensorNode", back_populates="readings")

class RiskPrediction(Base):
    __tablename__ = "risk_predictions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    node_id = Column(String, ForeignKey("sensor_nodes.id"), nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    risk_score = Column(Float, nullable=False)     # 0 to 100
    risk_level = Column(String, nullable=False)     # LOW | MEDIUM | HIGH | CRITICAL
    primary_factor = Column(String, nullable=True)
    confidence = Column(Float, default=0.95)

    node = relationship("SensorNode", back_populates="predictions")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(String, primary_key=True, index=True)
    node_id = Column(String, ForeignKey("sensor_nodes.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    risk_score = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
    reason = Column(String, nullable=False)
    details = Column(String, nullable=True)
    acknowledged = Column(Boolean, default=False)

    node = relationship("SensorNode", back_populates="alerts")

class SystemEvent(Base):
    __tablename__ = "system_events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    event_type = Column(String, nullable=False)
    message = Column(String, nullable=False)
