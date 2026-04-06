from pydantic import BaseModel
from typing import List, Optional


# Request Models

class AskRequest(BaseModel):
    question: str


class ExtractRequest(BaseModel):
    file_path: str


# Response Models

class AskResponse(BaseModel):
    answer: str
    sources: List[str]
    confidence: float


class ExtractionResponse(BaseModel):
    shipment_id: Optional[str] = None
    shipper: Optional[str] = None
    consignee: Optional[str] = None
    pickup_datetime: Optional[str] = None
    delivery_datetime: Optional[str] = None
    equipment_type: Optional[str] = None
    mode: Optional[str] = None
    rate: Optional[float] = None
    currency: Optional[str] = None
    weight: Optional[str] = None
    carrier_name: Optional[str] = None