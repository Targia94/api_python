from fastapi import APIRouter
from utenti.utenti_controller import router as utenti_routes
from attivita.attivita_controller import router as attivita_routes

api_router = APIRouter()

# api_router.include_router(utenti_routes, prefix="/api/utenti", tags=["utenti"])
api_router.include_router(attivita_routes, prefix="/api/attivita", tags=["attivita"])
