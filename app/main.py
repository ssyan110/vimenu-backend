from fastapi import FastAPI
from app.routers.menus import router as menus_router

app = FastAPI(title="vimenu-backend")

@app.get("/health")
def health():
    return {"status": "ok"}

# Mount /menus
app.include_router(menus_router)
