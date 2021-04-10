from ..config import Config
from typing import Union


def get_var(variable_name: str) -> Union[str, list, bool, int]:
    val = None
    typename = None
    if hasattr(Config, variable_name):
        val = getattr(Config, variable_name)
        typename = val[0]
        val = val[1]
