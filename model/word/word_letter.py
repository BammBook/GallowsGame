from enum import Enum

from model.word.alphabet import Alphabet


class WordLetterStatus(Enum):
    """Статус буквы в слове: разгадана или не разгадана"""
    OPENED = "OPENED"
    CLOSED = "CLOSED"


class WordLetter:
    """Буква, входящая в слово"""
    def __init__(self, letter: str):
        self._status = WordLetterStatus.CLOSED

        if Alphabet.check_letter(letter):
            self._letter = letter.upper()
        else:
            raise Exception("Invalid letter")

    @property
    def letter(self) -> str:
        return self._letter

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: WordLetterStatus):
        self._status = status

    def is_equal(self, letter: str) -> bool:
        return self._letter == letter.upper()


if __name__ == "__main__":
    a = WordLetter("ф")
    print(type(a.letter))
    print(type(a.status))
    print(a.is_equal('ы'))