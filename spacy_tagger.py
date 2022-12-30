import spacy
#spacy.cli.download("en_core_web_sm")

class Tagger(object):

    def __init__(self):
        self._spacy_tagger = spacy.load("en_core_web_sm")

    def tokenize_text(self, text: str):

        return [t for t in self._spacy_tagger(text)]
