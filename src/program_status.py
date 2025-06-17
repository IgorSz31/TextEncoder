from enum import Enum

class Status(Enum):
    SUCCESS = 0
    ERROR = 1

class ErrorMessage(Enum):
    EMPTY_INPUT = 'INPUT CANT BE EMPTY'
    EMPTYSTRING = 'STRING CANT BE EMPTY'
