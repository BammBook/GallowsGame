import random
from typing import List


class WordReader:
    def __init__(self, min_word_len, word_len=None):
        self._all_words = self._read_all_words()

        if word_len is None:
            self._word = self._get_word_by_min_length(self._all_words, min_word_len)
        else:
            self._word = self._get_word_by_length(self._all_words, word_len)

    @staticmethod
    def _read_all_words() -> List[str]:
        try:
            with open('../data_base/russian_nouns.txt', 'r', encoding='utf-8') as file:
                words = file.read().splitlines()
                return words
        except FileNotFoundError:
            print(f"Файл russian_nouns.txt не найден")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {str(e)}")

    @staticmethod
    def _get_word_by_length(words: List[str], word_length: int) -> str:
        filtered_words = [word.strip() for word in words if len(word.strip()) == word_length]

        try:
            if len(filtered_words) == 0:
                raise ValueError("В БД отсутствуют слова указанной длины")
            else:
                random_word = random.choice(filtered_words)
                return random_word
        except ValueError as e:
            print("Произошла ошибка:", e)

    @staticmethod
    def _get_word_by_min_length(words, min_word_len) -> str:
        filtered_words = [word.strip() for word in words if len(word.strip()) >= min_word_len]
        try:
            if len(filtered_words) == 0:
                raise ValueError("В БД отсутствуют слова указанной длины")
            else:
                random_word = random.choice(filtered_words)
                return random_word
        except ValueError as e:
            print("Произошла ошибка:", e)

    @property
    def word(self):
        return self._word

