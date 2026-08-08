from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):

    IDENT = 1
    NUMBER = 2
    STRING = 3

    FUNCTION = 4
    LOCAL = 5
    END = 6

    COLON = 7
    DOT = 8
    EQUAL = 9

    LPAREN = 10
    RPAREN = 11

    COMMA = 12

    OTHER = 99


@dataclass
class Token:

    type: TokenType

    value: str

    line: int