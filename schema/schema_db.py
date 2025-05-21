from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Utente(Base):
    __tablename__ = 'utenti'
    __table_args__ = {'schema': 'public'}  # opzionale, se non hai schema personalizzati

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
