from collections import defaultdict
from src.output_handler import OutputHandler
from src.utils.constants import BINARY_LETTER_TABLE
from src.program_status import Status, ErrorMessage
from src.table_handler import TableHandler
import logging

logger = logging.getLogger(__name__)

class BinaryConverter:

    def __init__(self):
        self.binary_letter_table = BINARY_LETTER_TABLE
        self.output_handler = OutputHandler()
        self.table_handler = TableHandler()


    def single_letter_convert(self, letter: str) -> str:
        """
        Searchers for provided symbol in the BINARY_LETTER_TABLE and returns its value
        """
        converted_letter = self.table_handler.letter_convert(letter)  + ' '
        logger.info(f'Single letter: {letter} converted successfully')
        return converted_letter

    def letter_list_create(self, word: str) -> list:
        """
        Creates a list of all letters in the given word
        """
        letter_list = [letter for letter in word]
        logger.info('Letter list created successfully')
        return letter_list

    def symbol_presence_validate(self, letter: str) -> bool:
        """
        Returns a bool basing on whether the given letter is present in the BINARY_LETTER_TABLE
        """
        if letter in self.binary_letter_table:
            logger.info(f'Symbol presence: {letter} validated successfully')
            return True
        else:
            logger.info(f'Symbol presence: {letter} not validated')
            return False

    def user_words_iterator(self, word: str) -> dict:
        """
        Returns provided string in the utf-8 code
        """
        if word == '':
            logger.error('Provided string is empty')
            return {'status':Status.ERROR.value, 'output':ErrorMessage.EMPTYSTRING.value}
        if word == 'exit()':
            logger.info('Exited the program successfully')
            exit()
        output = {'found': '', 'non_found': defaultdict(list)}


        letter_table = self.letter_list_create(word)
        for index,letter in enumerate(letter_table):

            if self.symbol_presence_validate(letter):
                output['found'] += self.single_letter_convert(letter)
                logger.info(f'Added {letter} to output')
                ' '.join(output)
            else:
                 output['non_found'][letter].append(index)

        logger.info('User words iteration done successfully')
        return {'status': Status.SUCCESS.value,
                'output':self.output_handler.friendly_output_handler(output)}



# # TESTING PURPOSES
# converter = BinaryConverter(BINARY_LETTER_TABLE)
#
# x   =  converter.user_words_iterator('')
# print(x['status'])