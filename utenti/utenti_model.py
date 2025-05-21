from db.database import OrmConnector
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy import update
import libraries.libraries as lib
from pydantic import BaseModel
from schema.schema_db import Utente

Base = declarative_base()


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
        return [], True

    finally:
        session.close()
