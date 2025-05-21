from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config


class OrmConnector:
    @staticmethod
    def get_engine(name_connection):
        connessioni = {
            'DATABASE': {
                'SERVER': config.get('database_host'),
                'DATABASE': config.get('database_name'),
                'UID': config.get('database_user'),
                'PWD': config.get('database_pass'),
                'PORT': config.get('database_port'),
            },
        }
        connection_info = connessioni.get(name_connection, {})
        if connection_info:
            database_uri = (
                f"postgresql+psycopg2://{connection_info['UID']}:{connection_info['PWD']}"
                f"@{connection_info['SERVER']}:{connection_info['PORT']}/{connection_info['DATABASE']}"
            )
            engine = create_engine(database_uri, echo=False)

            return engine
        else:
            raise ValueError("Informazioni di connessione non trovate")

    @staticmethod
    def get_session(engine):
        if engine is not None:
            session = sessionmaker(bind=engine)
            return session()
        else:
            raise ValueError("Engine non fornito")