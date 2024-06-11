from enum import Enum
from typing import List

from model.word.word_letter import WordLetter, WordLetterStatus


class WordStatus(Enum):
    """Статус всего слова: разгадано или не разгадано"""
    SOLVED = "SOLVED"
    NOT_SOLVED = "NOT_SOLVED"


class Word:
    def __init__(self, word: str):
        self._letters = []
        self._status = WordStatus.NOT_SOLVED

        for letter in word:
            self._letters.append(WordLetter(letter))

    @property
    def letters(self) -> List[WordLetter]:
        return self._letters

    @property
    def status(self) -> WordStatus:
        return self._status

    def check_letter(self, input_letter: str):
        """Проверка, входит ли буква в слово"""
        for letter in self._letters:
            if letter.is_equal(input_letter):
                letter.status = WordLetterStatus.OPENED

    def check_word_status(self):
        """Проверка, все ли буквы в слове открыты"""
        self._status = WordStatus.SOLVED
        for letter in self._letters:
            if letter.status != WordLetterStatus.OPENED:
                self._status = WordStatus.NOT_SOLVED




if __name__ == "__main__":
    word = Word('паша')
    word.check_word_status()
    print(word.status)
    word.check_letter('П')
    word.check_letter('ш')
    word.check_word_status()
    print(word.status)
    word.check_letter('а')
    word.check_word_status()
    print(word.status)


