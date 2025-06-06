import libraries.libraries as lib
from . import utenti_model


def get_all_utenti():

    utenti = utenti_model.get_all_utenti()

    return utenti
