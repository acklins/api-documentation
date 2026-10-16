# Documented item endpoints

from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()

items: list[dict] = []
_next_id = 1

#Retrieve all inventory items.
@router.get(
        "/",
        response_model=list[ItemResponse],
        summary="List all inventory items",
)
#Returns a list of inventory items currently stored in the app.
def list_items():
    """
    Retrieve all inventory items.

    Returns a list of inventory items currently stored in the app.

    - **Filtering:** Not currently implemented.
    - **Sorting:** Not currently implemented.
    - **Pagination:** Not currently implemented.
    - **Parameters:** None.
    - **Response:** An array of inventory items.

    Returns an empty list when no itmes exist.                  
    """
    return items

@router.post(
    "/",
    response_model=ItemResponse,
    status_code=201,
    summary="Create a new inventory item",
    responses={
        409: {
            "description": "An item with the same name already exists."
        },
        422: {
            "description": "Invalid item data or failed validation."
        },
    },
)
def create_item(item: ItemCreate):
    """
    Create a new inventory item.

    Accepts a JSON request body containing:

    - **name:** Required string, 1-100 characters.
    - **description:** Optional string, up to 500 characters.
    - **price:** Required positive number.
    - **category:** Required string.

    **Possible responses:**

    - **201 Created:** Item successfully created.
    - **409 Conflict:** Item name already exists.
    - **422 Unprocessable Entity:** Invalid request data.

    The API assigns a unique integer ID to each new item.
    """
    global _next_id

    for existing_item in items:
        if existing_item["name"] == item.name:
            raise HTTPException(
                status_code=409,
                detail="An item with the same name already exists."
            )
    new_item ={
        "id": _next_id,
        **item.model_dump(),
    }

    items.append(new_item)
    _next_id += 1

    return new_item

@router.get(
    "/{item_id}",
    response_model=ItemResponse,
    summary="Retrieve an inventory item by ID",
    responses={
        404: {
            "description": "Item not found."
        },
        422: {
            "description": "Invalid item ID format."
        },
    },
)
def get_item(item_id: int):
    """
    Retrieve a single inventory item by its ID.

    - **item_id:** Required integer path parameter.
    - **200 OK:** Returns the requested inventory item.
    - **404 Not Found:** No item matches the supplied ID.
    - **422 Unprocessable Entity:** Invalid ID format.

    Example: `GET /items/1`
    """
    for item in items:
        if item["id"] == item_id:
            return item
        
    raise HTTPException(
        status_code=404,
        detail=f"Item {item_id} not found",
    )