# -*- coding: utf-8 -*-
def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    Возвращает множество букв из letters, найденных в указаной фразе
    phrase
    :param phrase: str
    :param letters: str
    :return: set
    """
    return set(letters).intersection(phrase)
