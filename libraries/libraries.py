import hashlib
import base64
from json import dumps
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
import mimetypes
import smtplib
import logging
import configparser
from datetime import time, datetime
from config import config
import libraries.libraries


def init_environment():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        log_suffix = datetime.now().strftime('%Y%m%d')
        cfg_params = config['ENVIROMENT']['ENV']

        return cfg_params
    except Exception as e:
        print(e)
        exit(1)


def init_logger(name_file):
    try:
        # config = configparser.ConfigParser()
        # config.read('config.ini')
        log_suffix = datetime.now().strftime('%Y%m%d')
        cfg_params = config.get('params_config')

        logging.basicConfig(
            filename=(cfg_params + '/' + str(name_file) + '_' + log_suffix + '.log'),
            filemode='a',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger()
    except Exception as e:
        print(e)
        exit(1)


def info_log(logger, in_msg=''):
    logger.info(in_msg)


def error_log(logger, in_msg=''):
    logger.error(in_msg)


def xstr(s):
    if s is None:
        return ''
    return str(s).strip()


def xfloat(s):
    if s is None:
        return 0
    return float(s)


def ximporto(s):
    if s is None:
        return 0
    try:
        s = str(s).strip().replace(',', '.')
        if s == '':
            return 0
        else:
            return round(float(s), 2)
    except Exception as e:
        error_log('### ximporto')
        error_log('|' + s + '|')
        error_log('|' + str(s).replace(',', '.') + '|')
        exit(1)


def xint(s):
    if s is None:
        return 0
    return int(s)


def xstato(s):
    if s is None:
        return 0
    if s == 3:
        return 0
    return int(s)


def xbool(s):
    if s is None or str(s).strip().upper() == 'FALSE':
        return '0'
    return '1'


def xdate(s):
    if s is None:
        return '1001-01-01'
    if str(s).strip() == '':
        return '1001-01-01'
    return str(s).strip()


def explodeDest(destinatario):
    dict_Destinazione = {
        'Anagrafica': '',
        'Indirizzo': '',
        'Cap': '',
        'Localita': '',
        'Provincia': '',
        'Nazione': '',
        'Telefono': ''
    }
    if destinatario:
        try:
            tmp_Arr = destinatario.split('}|{')
            if len(tmp_Arr) > 1 and tmp_Arr[1]:
                dict_Destinazione['Anagrafica'] = tmp_Arr[1].replace('"', "").replace("'", "")
                if dict_Destinazione['Anagrafica'] == 'N':
                    dict_Destinazione['Anagrafica'] = ''
            if len(tmp_Arr) > 3 and tmp_Arr[3]:
                dict_Destinazione['Indirizzo'] = tmp_Arr[3].replace('"', "").replace("'", "")
            if len(tmp_Arr) > 5 and tmp_Arr[5]:
                dict_Destinazione['Cap'] = tmp_Arr[5].replace('$|$N', '').strip('N')
            if len(tmp_Arr) > 6 and tmp_Arr[6]:
                dict_Destinazione['Localita'] = tmp_Arr[6].replace('"', "").replace("'", "")
            if len(tmp_Arr) > 7 and tmp_Arr[7]:
                dict_Destinazione['Provincia'] = tmp_Arr[7].replace('$|$N', '')
            if len(tmp_Arr) > 8 and tmp_Arr[8]:
                dict_Destinazione['Nazione'] = tmp_Arr[8].replace('$|$N', '').strip('N').replace('$|$Y', '')
            if len(tmp_Arr) > 9 and tmp_Arr[9]:
                dict_Destinazione['Telefono'] = tmp_Arr[9].replace('$|$N', '').strip('N').replace('Y', '')
        except Exception as e:
            print(len(tmp_Arr))
            print(tmp_Arr)
            exit(1)

    else:
        return {}

    return dict_Destinazione


def generate_GUID():
    import uuid

    guid = uuid.uuid1()

    return xstr(guid).upper()


def generate_passwd(passwd):
    hashed_password = hashlib.sha256(passwd.encode()).hexdigest()

    return xstr(hashed_password).upper()
