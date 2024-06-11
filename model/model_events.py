from model.game_settings.settings import GameSettings
from model.game_status.game_status import GameStatus
from model.keyboard.keyboard import Keyboard
from model.word.alphabet import Alphabet
from model.word.word import Word
from model.word_reader.word_reader import WordReader


class GameEvents:
    """Реализация паттерна Фасад - скрываем логику в интерфейс взаимодействия"""
    def __init__(self, game_settings: GameSettings):
        self._settings = game_settings
        self._game_status = GameStatus()
        self._keyboard = Keyboard()
        self._word_reader = WordReader(min_word_len=self._settings.min_word_length)
        self._word = Word(word=self._word_reader.word)

    def start_game(self):
        """Начало игры"""
        pass

    def check_game_status(self):
        return self._game_status.is_game_over()

    def check_letter(self, letter: str):
        """Проверка наличия в слове буквы"""
        if not Alphabet.check_letter(letter):
            raise Exception("Invalid letter")
        self._word.check_letter(letter)
        # надо дописать check_letter чтобы он возвращал true\false
        # есть буква в слове или нет и в зависимости от этого менять статус клавиатуры
        # self._keyboard.