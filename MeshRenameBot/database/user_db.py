from ..core.get_config import get_var

if get_var("IS_MONGO"):
    from .mongo_impl import UserDB
else:
    from .postgres_impl import UserDB
