from src.utils.constants import BINARY_LETTER_TABLE

class TableHandler:
    def __init__(self):
        self.binary_table = BINARY_LETTER_TABLE


    def letter_convert(self, letter):
        converted_letter = self.binary_table[letter]
        return converted_letter