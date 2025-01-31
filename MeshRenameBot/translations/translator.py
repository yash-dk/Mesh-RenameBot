from typing import Dict
from jinja2 import Template
from .en import EnglishTranslations
from .es import SpanishTranslations
from .ar import ArabicTranslations
from .hi import HindiTranslations
from .ko import KoreanTranslations
from .ru import RussianTranslations
from .zh import ChineseTranslations
from ..config import Config

TRANSLATION_MAP: Dict[str, object] = {
    "en": EnglishTranslations(),
    "es": SpanishTranslations(),
    "ar": ArabicTranslations(),
    "hi": HindiTranslations(),
    "ko": KoreanTranslations(),
    "ru": RussianTranslations(),
    "zh": ChineseTranslations(),
}


class Translator:
    def __init__(self, user_locale: str = None):
        self.user_locale = (
            user_locale if user_locale in TRANSLATION_MAP else Config.DEFAULT_LOCALE[1]
        )

    def get(self, key: str, **kwargs) -> str:
        translations = TRANSLATION_MAP[self.user_locale]
        text_template = getattr(translations, key, f"[{key} not found]")
        return Template(text_template).render(**kwargs)
