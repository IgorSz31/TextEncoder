from constants import BINARY_LETTER_TABLE



class BinaryConverter:
    def __init__(self, binary_letter_table: dict):
        self.binary_letter_table = binary_letter_table

    def single_letter_convert(self, letter):
        """
        Searchers for provided symbol in the BINARY_LETTER_TABLE and returns its value
        """
        output = ''
        if letter in self.binary_letter_table:
            output += self.binary_letter_table[letter]
        return output

    def user_words_iterator(self,word):
        """
        Returns provided string in the utf-8 code
        """
        output=''
        letter_table = []
        for letter in word:
            letter_table.append(letter)
        for letters in letter_table:
            if letters in self.binary_letter_table:
                output +=self.binary_letter_table[letters] + ' '
        return output


converter = BinaryConverter(BINARY_LETTER_TABLE)
print(converter.single_letter_convert('Ą'))
print(converter.user_words_iterator('abc'))