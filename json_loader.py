import json
import os
from document_model import Document
import re

class JSONLoader:

    def __init__(self):
        super(JSONLoader).__init__()

    def read_file(self, filename: str):
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
        text = ''
        return Document(text, filename=os.path.basename(filename))