from googletrans import LANGUAGES, Translator

from dialect.translators.basetrans import TranslatorBase, TranslationError


class GTranslator(TranslatorBase):
    history = []
    languages = LANGUAGES
    supported_features = {
        'mistakes': True,
        'pronunciation': True,
        'voice': True,
    }

    def __init__(self):
        super().__init__()
        self._translator = Translator()

    def detect(self, src_text):
        try:
            return self._translator.detect(src_text)
        except Exception as e:
            raise TranslationError(e)

    def translate(self, src_text, src, dest):
        try:
            return self._translator.translate(src_text, src=src, dest=dest)
        except Exception as e:
            raise TranslationError(e)
