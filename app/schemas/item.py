# Item schema with documentation
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

#An item in the inventory.
class Item(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="The name of the inventory item.",
    )
    description: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional item description.",
    )
    price: float = Field(
        gt=0,
        description="Item price. Must be greater than zero.",
        examples=[29.99],
    )
    category: str = Field(
        description="Category of the inventory item.",
        examples=["Electronics"],
    )
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Wireless Mouse",
                "description": "Ergonomic Bluetooth mouse",
                "price": 29.99,
                "category": "Electronics",
            }
        }
    )
#Schema for creating an inventory item.
class ItemCreate(Item):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Wireless Keyboard",
                "description": "Compact Bluetooth keyboard",
                "price": 49.99,
                "category": "Electronics",
            }
        }
    )

#Schema returned to clients with a  server-assigned ID.
class ItemResponse(ItemCreate):
    id: int = Field(
        description="Unique identifier assigned by the API.",
        examples=[1],
    )
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Wireless Keyboard",
                "description": "Compact Bluetooth keyboard",
                "price": 49.99,
                "category": "Electronics",
            }
        },
    )
