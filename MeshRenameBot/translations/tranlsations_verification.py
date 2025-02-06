from en import EnglishTranslations
from es import SpanishTranslations
from ar import ArabicTranslations
from hi import HindiTranslations
from ko import KoreanTranslations
from ru import RussianTranslations
from zh import ChineseTranslations

for directive in dir(EnglishTranslations):
    if directive.startswith("__"):
        continue
    for translation in [
        ArabicTranslations,
        ChineseTranslations,
        HindiTranslations,
        KoreanTranslations,
        RussianTranslations,
        SpanishTranslations,
    ]:
        if not hasattr(translation, directive):
            print(f"Missing {directive} in {translation.__name__}")
