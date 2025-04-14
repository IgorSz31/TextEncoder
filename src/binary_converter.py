from constants import BINARY_LETTER_TABLE



class BinaryConverter:
    def __init__(self, binary_letter_table: dict):
        self.binary_letter_table = binary_letter_table

    def single_letter_convert(self, letter: str) -> str:
        """
        Searchers for provided symbol in the BINARY_LETTER_TABLE and returns its value
        """
        converted_letter = self.binary_letter_table[letter]
        return converted_letter

    def letter_list_create(self,word: str) -> list:

        letter_list = [letter for letter in word]
        return letter_list

    def user_words_iterator(self,word: str) -> str:
        """
        Returns provided string in the utf-8 code
        """
        output=''
        letter_table = self.letter_list_create(word)
        for letter in letter_table:
            if letter in self.binary_letter_table:
                output += self.single_letter_convert(letter) + ' '
            else:
                print(f"Symbol not found: {letter}")
        return output


converter = BinaryConverter(BINARY_LETTER_TABLE)
# print(converter.single_letter_convert('['))
print(converter.user_words_iterator('a[]bc'))