from constants import BINARY_LETTER_TABLE



class BinaryConverter:
    def __init__(self, binary_letter_table: dict):
        self.binary_letter_table = binary_letter_table

    def single_letter_convert(self, letter):
        pass
        

converter = BinaryConverter(BINARY_LETTER_TABLE)
print(converter.single_letter_convert('a'))