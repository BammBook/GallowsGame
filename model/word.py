from typing import List

from model.letters.word_letter import WordLetter


class Word:
    def __init__(self, word: str):
        self._letters = []

        for letter in word:
            self._letters.append(WordLetter(letter))

    @property
    def letters(self) -> List[WordLetter]:
        return self._letters

    def check_all_word(self):
        for letter in self._letters:
            print(letter.status)




if __name__ == "__main__":
    word = Word('папа')
    word.check_all_word()
