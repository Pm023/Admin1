"""
Pydantic Schemas for Buyer
"""

from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional

class BuyerBase(BaseModel):
    name: str
    phone: str
    country: str
    city: str
    product: str
    quantity: int
    price: float
    terms: str
    is_active: bool = True

    @field_validator('terms')
    @classmethod
    def validate_terms(cls, v):
        if v.upper() not in ["FOB", "CIF"]:
            raise ValueError('Terms must be either "FOB" or "CIF"')
        return v.upper()
    
    @field_validator('quantity')
    @classmethod
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be greater than 0')
        return v
    
    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v

class BuyerCreate(BuyerBase):
    pass

class BuyerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    product: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    terms: Optional[str] = None
    is_active: Optional[bool] = None

class BuyerResponse(BuyerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)