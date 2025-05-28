from enum import Enum

class Status(Enum):
    SUCCESS = 0
    ERROR = 1

class ErrorMessage(Enum):
    EMPTYSTRING = 'STRING CANT BE EMPTY'
