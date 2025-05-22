from db.database import OrmConnector
from fastapi import HTTPException
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
from typing import Optional
from schema.schema_db import Attivita

Base = declarative_base()


class AttivitaQuery(BaseModel):
    data_da: Optional[str] = None
    data_a: Optional[str] = None


def get_all_utenti():
    engine = OrmConnector.get_engine('DATABASE')
    session = OrmConnector.get_session(engine)

    try:
        utenti = session.query(Utente).all()
        lista_utenti = []

        for u in utenti:
            lista_utenti.append({
                "id": u.id,
                "full_name": u.full_name
            })

        return lista_utenti

    except Exception as e:
        print(f"Errore durante la query utenti: {e}")
        return []

    finally:
        session.close()


def get_attivita(attivita: AttivitaQuery):
    engine = OrmConnector.get_engine('DATABASE')
    session = OrmConnector.get_session(engine)

    try:
        query_filter = session.query(Attivita)

        # Aggiungi i filtri dalla richiesta
        if attivita.data_da:
            query_filter = query_filter.filter(Attivita.data >= attivita.data_da)

        if attivita.data_a:
            query_filter = query_filter.filter(Attivita.data <= attivita.data_a)

        # Esegui la query
        attivita_list = query_filter.all()

        # Se non ci sono risultati, lancia un errore
        if not attivita_list:
            raise HTTPException(status_code=404, detail="Attività non trovata")

        return attivita_list
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Errore nel database: " + str(e))

    finally:
        session.close()
