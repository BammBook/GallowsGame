class Alphabet:
    """Класс русского алфавита"""
    _letters = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]

    @classmethod
    def letters(cls):
        return cls._letters

    @classmethod
    def check_letter(cls, letter):
        return letter.upper() in cls._letters
