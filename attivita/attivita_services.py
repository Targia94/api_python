import libraries.libraries as lib
from . import attivita_model


def get_all_utenti():

    utenti = attivita_model.get_all_utenti()

    return utenti


def get_attivita(attivita):

    return attivita_model.get_attivita(attivita)