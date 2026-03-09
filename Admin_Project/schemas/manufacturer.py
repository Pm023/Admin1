"""
Pydantic Schemas for Manufacturer
"""

from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional

class ManufacturerBase(BaseModel):
    name: str
    phone: str
    city: str
    product: str
    price: float
    is_active: bool = True

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    product: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class ManufacturerResponse(ManufacturerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)