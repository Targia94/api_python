from fastapi import APIRouter, Response, status, HTTPException
from . import attivita_service
from . import attivita_dto


router = APIRouter()


# @router.get("/get_all_utenti/")
# @router.get("/get_all_utenti", include_in_schema=False)
# def utenti(response: Response,):
#
#     return attivita_services.get_all_utenti()

@router.get("/importa_db/")
@router.get("/importa_db", include_in_schema=False)
def importa_db(response: Response,):

    return attivita_service.importa_db()


@router.post("/get_attivita/")
@router.post("/get_attivita", include_in_schema=False)
def utenti(attivita: attivita_dto.AttivitaQuery,):

    return attivita_service.get_attivita(attivita)
