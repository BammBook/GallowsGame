from enum import Enum

from model.word.alphabet import Alphabet


class KeyboardLetterStatus(Enum):
    """Статус буквы на клавиатуре: не испробована, встречается в слове
     или не встречается"""
    OCCUR = "OCCUR"
    NOT_OCCUR = "NOT_OCCUR"
    NOT_TRIED = "NOT_TRIED"


class Keyboard:
    """Клавиатура со статусом букв"""

    def __init__(self):
        self.keyboard = {}
        for letter in Alphabet.letters():
            self.keyboard[letter] = KeyboardLetterStatus.NOT_TRIED

    def set_letter_status(self, letter: str, status: KeyboardLetterStatus):
        if not Alphabet.check_letter(letter) or letter not in self.keyboard.keys():
            raise Exception("Invalid letter")
        if not isinstance(status, KeyboardLetterStatus):
            raise Exception("Invalid status")
        self.keyboard[letter] = status

    def get_letter_status(self, letter: str) -> KeyboardLetterStatus:
        if not Alphabet.check_letter(letter) or letter not in self.keyboard.keys():
            raise Exception("Invalid letter")
        return self.keyboard[letter]