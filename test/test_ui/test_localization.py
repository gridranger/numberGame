from unittest import TestCase

from ui import localization
from ui.localization import Term, ENGLISH


class TestLocalization(TestCase):

    def test___init__(self):
        t = Term("apple", "alma")
        self.assertEqual("alma", t.HU)

    def test___init__translation_missing(self):
        with self.assertLogs(level="WARNING") as caplog:
            t = Term("apple")
        self.assertEqual("apple", t.HU)
        self.assertEqual("WARNING:root:Translation of term 'apple' to language HU is missing.", caplog.output[0])

    def test___str__(self):
        original_language = localization.language
        localization.language = "HU"
        self.assertEqual("Angol", str(ENGLISH))
        localization.language = original_language

    def test___str__no_such_language(self):
        original_language = localization.language
        localization.language = "KLINGON"
        with self.assertLogs(level="ERROR") as caplog:
            self.assertEqual("English", str(ENGLISH))
        self.assertEqual("ERROR:root:Language KLINGON is not supported. English will be used instead. Set a supported "
                         "language to settings.py. Supported languages: EN, HU", caplog.output[0])
        localization.language = original_language
