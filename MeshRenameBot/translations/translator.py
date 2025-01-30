from typing import Dict
from jinja2 import Template
from .en import EnglishTranslations
from ..config import Config

TRANSLATION_MAP: Dict[str, object] = {
    "en": EnglishTranslations(),
}


class Translator:
    def __init__(self, user_locale: str = None):
        user_locale = Config.DEFAULT_LOCALE[
            1
        ]  # Exception handling without get-config module
        self.user_locale = user_locale if user_locale in TRANSLATION_MAP else "en"

    def get(self, key: str, **kwargs) -> str:
        translations = TRANSLATION_MAP[self.user_locale]
        text_template = getattr(translations, key, f"[{key} not found]")
        return Template(text_template).render(**kwargs)