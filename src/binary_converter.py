from constants import BINARY_LETTER_TABLE


class BinaryConverter:
    def __init__(self, binary_letter_table: dict):
        self.binary_letter_table = binary_letter_table

    def single_letter_convert(self, letter: str) -> str:
        """
        Searchers for provided symbol in the BINARY_LETTER_TABLE and returns its value
        """
        converted_letter = self.binary_letter_table[letter] + ' '
        return converted_letter

    def letter_list_create(self, word: str) -> list:
        """
        Creates a list of all letters in the given word
        """
        letter_list = [letter for letter in word]
        return letter_list

    def symbol_presence_validate(self, letter: str) -> bool:
        """
        Returns a bool basing on whether the given letter is present in the BINARY_LETTER_TABLE
        """
        if letter in self.binary_letter_table:
            return True
        else:
            return False

    def non_existent_symbols_listed(self, letter: str) -> list:
        letter_table = self.letter_list_create(letter)

        pass

    def user_words_iterator(self, word: str) -> str:
        """
        Returns provided string in the utf-8 code
        """
        output = {'found': '', 'non_found': {}  }
        letter_table = self.letter_list_create(word)
        for index,letter in enumerate(letter_table):

            if self.symbol_presence_validate(letter):
                output['found'] += self.single_letter_convert(letter)
                ' '.join(output)
            else:
                 output['non_found'][letter] = index
            # if letter in self.binary_letter_table:
            #     output += self.single_letter_convert(letter) + ' '
            # else:
            #     print(f"Symbol not found: {letter}")

        if output['found'] or output['non_found']:
            return output




converter = BinaryConverter(BINARY_LETTER_TABLE)
# print(converter.single_letter_convert('['))
x   =  converter.user_words_iterator('*%*')
print(x)