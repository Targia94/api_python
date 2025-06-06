from db.database import OrmConnector
from fastapi import HTTPException
from .attivita_dto import AttivitaQuery
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