from .utils.constants import BINARY_LETTER_TABLE
import logging

logger = logging.getLogger(__name__)

class TableHandler:
    def __init__(self):
        self.binary_letter_table = BINARY_LETTER_TABLE


    def letter_convert(self, letter):
        converted_letter = self.binary_letter_table[letter]
        return converted_letter

    def symbol_presence_validate(self, letter: str) -> bool:
       try:
           return self.binary_letter_table[letter]
       except KeyError:
           logger.info(f'Symbol presence: {letter} not validated')
           return False

    def reverse_table(self):
        reversed_table = {v: k for k, v in BINARY_LETTER_TABLE.items()}
        return reversed_table




