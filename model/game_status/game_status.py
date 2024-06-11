class GameStatus:
    """Состояние игры"""
    def __init__(self):
        self._attempts: int = 0
        self._mistakes: int = 0
        self._max_mistakes: int = 8
        self._is_game_over: bool = False

    def check_is_game_over(self):
        if self._mistakes >= self._max_mistakes:
            self._is_game_over = True

    def add_attempt(self):
        self._attempts += 1

    def add_mistake(self):
        self._mistakes += 1

    @property
    def attempts(self):
        return self._attempts

    @property
    def mistakes(self):
        return self._mistakes

    @property
    def max_mistakes(self):
        return self._max_mistakes

    @max_mistakes.setter
    def max_mistakes(self, value: int):
        self._max_mistakes = value

    @property
    def is_game_over(self):
        return self._is_game_over
