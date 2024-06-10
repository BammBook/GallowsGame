from enum import Enum

from model.letters.alphabet import Alphabet


class WordLetterStatus(Enum):
    OPENED = "OPENED"
    CLOSED = "CLOSED"


class WordLetter:
    """Буква, входящая в слово"""
    def __init__(self, letter: str):
        self._status = WordLetterStatus.CLOSED

        if Alphabet.check_letter(letter):
            self._letter = letter
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


if __name__ == "__main__":
    a = WordLetter("ф")
    print(type(a.letter))
    print(type(a.status))