class GameSettings:
    """Игровые настройки"""
    def __init__(self):
        self._max_mistakes = 8
        self._min_word_length = 5

    @property
    def max_mistakes(self):
        return self._max_mistakes

    @max_mistakes.setter
    def max_mistakes(self, value):
        self._max_mistakes = value

    @property
    def min_word_length(self):
        return self._min_word_length

    @min_word_length.setter
    def min_word_length(self, value):
        self._min_word_length = value