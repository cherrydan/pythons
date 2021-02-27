# -*- coding: utf-8 -*-


def search4vowels(word: str) -> set:
    """
    Returns vowels, found in given word

    :param word: str
    :return: set
    """
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """
    Возвращает множество букв из letters, найденных в указаной фразе
    phrase
    :param phrase: str
    :param letters: str
    :return: set
    """
    return set(letters).intersection(phrase)

