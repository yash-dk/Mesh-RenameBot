current_lang = "en"
if current_lang == "en":
    from .en import EnTrans as Trans
else:
    ...
#def get_trans(title, lang = None) -> str:
#    if lang is None:
#        if current_lang == "en":
#            return getattr(EnTrans, title)
#    else:
#        if current_lang == "en":
#            return getattr(EnTrans, title)
