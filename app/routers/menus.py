from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Menu(BaseModel):
    id: int
    name: str

# temporary in-memory data
_FAKE_MENUS: List[Menu] = [
    Menu(id=1, name="Sample Menu"),
]

@router.get("", response_model=List[Menu])
def list_menus() -> List[Menu]:
    """Return all menus (temporary in-memory)."""
    return _FAKE_MENUS
