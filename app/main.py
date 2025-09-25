from fastapi import FastAPI
from app.routers import menus

app = FastAPI(title="vimenu-backend")

@app.get("/health")
def health():
    return {"status": "ok"}

# /menus -> list menus
app.include_router(menus.router, prefix="/menus", tags=["menus"])
