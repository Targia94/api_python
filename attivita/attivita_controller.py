from fastapi import APIRouter, Response, status, HTTPException
from . import attivita_services
from . import attivita_model


router = APIRouter()


# @router.get("/get_all_utenti/")
# @router.get("/get_all_utenti", include_in_schema=False)
# def utenti(response: Response,):
#
#     return attivita_services.get_all_utenti()

@router.get("/test_2/")
@router.get("/test_2", include_in_schema=False)
def test_2(response: Response,):

    return attivita_services.get_all_utenti()


@router.post("/get_attivita/")
@router.post("/get_attivita", include_in_schema=False)
def utenti(attivita: attivita_model.AttivitaQuery,):

    return attivita_services.get_attivita(attivita)
