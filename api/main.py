from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from api.routers import user_router
from api.routers import english_router
from api.database import db


def init_app()-> FastAPI:

    db.init()

    app = FastAPI(
        title="Lern English",
        description="CRUD",
        version="1"
    )

    # Adicionando o middleware de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permite todas as origens. Substitua com origens específicas em produção.
        allow_credentials=True,
        allow_methods=["*"],  # Permite todos os métodos HTTP
        allow_headers=["*"],  # Permite todos os cabeçalhos
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    app.include_router(user_router.router, prefix="/users", tags=["Users"])        
    app.include_router(english_router.router, prefix="/english", tags=["English"])
    return app

app = init_app()

    
@app.get("/")
async def root():
    return {"message": "Hello Learn English"}