from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SensorReadingBase(BaseModel):
    node_id: str
    tilt: float
    displacement: float
    crack_width: float
    vibration: float
    load_change: float
    temperature: float
    humidity: float
    battery: float = 100.0

class SensorReadingCreate(SensorReadingBase):
    pass

class SensorReadingResponse(SensorReadingBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class NodeSchema(BaseModel):
    id: str
    name: str
    location: str
    depth: str
    latitude: float
    longitude: float
    status: str
    last_communication: datetime

    class Config:
        from_attributes = True

class RiskPredictionResponse(BaseModel):
    node_id: str
    risk_score: float
    risk_level: str
    primary_factor: Optional[str]
    confidence: float
    timestamp: datetime

class AlertSchema(BaseModel):
    id: str
    node_id: str
    timestamp: datetime
    risk_score: float
    risk_level: str
    reason: str
    details: Optional[str]
    acknowledged: bool

    class Config:
        from_attributes = True

class DemoModeRequest(BaseModel):
    mode: str = Field(..., description="NORMAL | WARNING | SUBSIDENCE")
