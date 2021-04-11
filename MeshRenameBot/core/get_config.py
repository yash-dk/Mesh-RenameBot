from ..config import Config
from typing import Union
import logging
import os
from ..translations.trans import Trans

renamelog = logging.getLogger(__name__)


def get_var(variable_name: str) -> Union[str, list, bool, int]:
    val = None
    typename = None

    if hasattr(Config, variable_name):
        val = getattr(Config, variable_name)
        typename = val[0]
        val = val[1]

        new_val = os.environ.get(variable_name, None)
        if new_val is not None:
            if typename == int:
                try:
                    new_val = int(new_val)
                except ValueError:
                    renamelog.error(Trans.WRONG_VALUE_ERROR.format(variable_name))
            
            elif typename == bool:
                new_val = new_val.lower()
                if new_val == "true":
                    new_val = True
                else:
                    new_val = False
            
            elif typename == list:
                new_val = new_val.split(",")

            val = new_val

        return val
                    
    return None
