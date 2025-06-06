from db.database import OrmConnector
from fastapi import HTTPException
from .attivita_dto import AttivitaQuery
from .attivita_dto import InsertAttivita
from sqlalchemy.exc import SQLAlchemyError
from schema.schema_db import Attivita
import sqlite3


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


def importa_db():
    from datetime import datetime
    engine = OrmConnector.get_engine('DATABASE')
    session = OrmConnector.get_session(engine)

    sqlite_conn = sqlite3.connect('database.db')
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute('SELECT * FROM lavoro')  # Supponendo che la tabella si chiami attivita
    rows = sqlite_cursor.fetchall()

    for row in rows:
        id, data, cliente, contratto, saldato, commessa, saldo, extra_consegna = row

        # Converti la data in formato Python (se necessario)
        data = datetime.strptime(data, '%Y-%m-%d')  # Assicurati che il formato sia corretto

        # Crea un nuovo oggetto Attivita
        new_attivita = Attivita(
            data=data,
            cliente=cliente,
            contratto=contratto,
            saldato=saldato,
            commessa=commessa,
            saldo=saldo,
            extra_consegna=extra_consegna
        )

        # Aggiungi l'oggetto alla sessione di SQLAlchemy
        session.add(new_attivita)

    session.commit()
    sqlite_conn.close()
    session.close()
    print("Dati trasferiti con successo!")


def inserisci_attivita(attivita: InsertAttivita):
    engine = OrmConnector.get_engine('DATABASE')
    session = OrmConnector.get_session(engine)

    try:
        # Creazione di un nuovo oggetto Attivita usando i dati di InsertAttivita
        new_attivita = Attivita(
            data=attivita.data,
            cliente=attivita.cliente,
            contratto=attivita.contratto,
            saldato=attivita.saldato,
            commessa=attivita.commessa,
            saldo=attivita.saldo,
            extra_consegna=attivita.extra_consegna or 0  # Default a 0 se non fornito
        )

        # Aggiungi l'oggetto alla sessione
        session.add(new_attivita)
        session.commit()  # Fai il commit per salvare nel database

        print("Attività inserita con successo!")
        return {"success": True, "message": "Attività inserita con successo!"}

    except Exception as e:
        print(f"Errore: {e}")
        session.rollback()  # Rollback in caso di errore
        return {"success": False, "error": f"Errore durante l'inserimento: {str(e)}"}

    finally:
        session.close()  # Chiudi la sessione