from logging import error, warning
from settings import language


class Term:
    SUPPORTED_LANGUAGES = ["HU"]

    def __init__(self, en: str, *args):
        self.EN = en
        for index, supported_language in enumerate(self.SUPPORTED_LANGUAGES):
            try:
                self.__dict__[supported_language] = args[index]
            except IndexError:
                warning(f"Translation of term '{en}' to language {supported_language} is missing.")
                self.__dict__[supported_language] = en

    def __str__(self):
        try:
            return self.__dict__[language]
        except KeyError:
            error(f"Language {language} is not supported. English will be used instead. Set a supported language to "
                  f"settings.py. Supported languages: {', '.join(['EN'] + self.SUPPORTED_LANGUAGES)}")
            return self.EN


ENGLISH = Term("English", "Angol")
HIGH_SCORES = Term("High scores", "Dicsőségfal")
HUNGARIAN = Term("Hungarian", "Magyar")
NEW_GAME = Term("New game", "Új játék")
QUIT = Term("Quit", "Kilépés")
