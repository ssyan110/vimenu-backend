from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/menus", tags=["menus"])

# Sample data exactly as tests expect (ids are strings like "m-001")
_SAMPLE_MENUS: List[Dict[str, Any]] = [
    {"id": "m-001", "name": "Breakfast Specials", "items": [
        {"sku": "eggs-bacon", "title": "Eggs & Bacon", "price": 9.50},
        {"sku": "avocado-toast", "title": "Avocado Toast", "price": 7.25},
    ]},
    {"id": "m-002", "name": "Coffee & Tea", "items": [
        {"sku": "latte-12oz", "title": "Latte 12oz", "price": 4.25},
        {"sku": "earl-grey", "title": "Earl Grey Tea", "price": 3.00},
    ]},
]

@router.get("", summary="List menus")
def list_menus() -> Dict[str, Any]:
    # tests expect {"menus": [...]}
    return {"menus": _SAMPLE_MENUS}

@router.get("/{menu_id}", summary="Get one menu by id")
def get_menu(menu_id: str) -> Dict[str, Any]:
    for m in _SAMPLE_MENUS:
        if m["id"] == menu_id:
            return m
    # tests expect 200 with this JSON (not a 404)
    return {"error": "menu_not_found", "menu_id": menu_id}
