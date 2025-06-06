from fastapi import APIRouter
from utenti.utenti_controller import router as utenti_routes
from attivita.attivita_controller import router as attivita_routes
from utenti.utenti_controller import router as utenti_router

api_router = APIRouter()

# api_router.include_router(utenti_routes, prefix="/api/utenti", tags=["utenti"])
api_router.include_router(attivita_routes, prefix="/api/attivita", tags=["attivita"])
api_router.include_router(utenti_router, prefix="/api/user", tags=["user"])
