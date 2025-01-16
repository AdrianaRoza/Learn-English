import uvicorn
from fastapi import FastAPI
from api.routers import user_router 
from api.database import db


def init_app()-> FastAPI:

    db.init()

    app = FastAPI(
        title="Lern English",
        description="CRUD",
        version="1"
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    app.include_router(user_router.router, prefix="/users2", tags=["Users"])        

    return app

app = init_app()

    
@app.get("/")
async def root():
    return {"message": "Hello Learn English"}