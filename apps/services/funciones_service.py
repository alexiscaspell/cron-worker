from apps.models.tarea_programada import TareaProgramada
import glob
from typing import List,Dict
import pathlib
import zipfile
import calendar
from apps.utils.logger_util import get_logger
import apps.configs.configuration as conf
from apps.configs.vars import Vars
from datetime import date

logger = get_logger(__name__)

def tarea_de_prueba(tarea:TareaProgramada,un_path_archivo):
    logger.debug(f"Soy un debug que solo se muestra en desa !!")
    
    logger.exception(f"Soy un exception exceptional (xP)")

    with open(un_path_archivo,"rb") as f:
        file_bytes = f.read()

    return True,["Every day is friday...",file_bytes]

def evaluar(expresion:str,*args):
    return eval(expresion,globals(),{"args":args})