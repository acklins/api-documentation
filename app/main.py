#Polished Documentation
from fastapi import FastAPI
from app.routers import items

#Tag descriptions for Swagger UI
openapi_tags = [
    {
        "name": "items",
        "description": """
Manage inventory items using the following operations:
- **List items** currently in the inventory.
- **Create items** with validated request data.
- **Retrieve items** by their unique IDs.

All items are stored in memory for this exercise.
Data resets when the application restarts.
""",
    },
]

#FastAPI application metadata
app = FastAPI(
    title="Inventory Management API",
    description="""
## Welcome to the Inventory Management API
A RESTful API built with **FastAPI** and **Pydantics**.

### Features

- Create inventory items.
- Retrieve all inventory items.
- Retrieve individual inventory items by ID.
- Validate incoming data automatically.
- Prevent duplicate item names.

### Validation Rules

- **Name:** 1-100 characters.
- **Description:**: Optional, maximum 500 characters.
- **Price:** Must be greater than zero.
- **Category:** Required.

### HTTP Response Codes

| Code | Meaning |
|------|---------|
| 200 | Successful retrieval |
| 201 | Item created |
| 404 | Item not found |
| 409 | Duplicate item name |
| 422 | Invalid request data |

### Storage

This demonstration uses an in-memory Python list.

**Note:** Inventory data does not persist after the server restarts.
""",
    version="1.0.0",
    contact={
        "name": "Inventory API Support",
        "email": "support@example.com",
    },
    license_info={
        "name": "Educational Use - Course Assignment",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=openapi_tags,
)

#register the items router
app.include_router(
    items.router, 
    prefix="/items", 
    tags=["items"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
    )
