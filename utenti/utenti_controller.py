from fastapi import APIRouter, Response, status, HTTPException
from . import utenti_services
from . import utenti_model


router = APIRouter()


@router.get("/get_all_utenti/")
@router.get("/get_all_utenti", include_in_schema=False)
def utenti(response: Response,):

    return utenti_services.get_all_utenti()
