from sqlalchemy import Column, Integer, String, Float, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Utente(Base):
    __tablename__ = 'utenti'
    __table_args__ = {'schema': 'public'}  # opzionale, se non hai schema personalizzati

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)


class Attivita(Base):
    __tablename__ = 'attivita'  # Nome della tabella

    id = Column(Integer, primary_key=True, autoincrement=True)  # id come chiave primaria
    data = Column(Date, nullable=False)  # data come tipo Date
    cliente = Column(String(255), nullable=False)  # cliente come varchar(255)
    contratto = Column(Float, nullable=False)  # contratto come float
    saldato = Column(Float, nullable=False)  # saldato come float
    commessa = Column(String(255), nullable=False)  # commessa come varchar(255)
    saldo = Column(String(255), nullable=False)
    extra_consegna = Column(Float, nullable=False)  # extra_consegna come float
