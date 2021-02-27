# -*- coding: utf-8 -*-
def search4vowels(word: str) -> set:
    """
    Returns vowels, found in given word
    
    :param word: str
    :return: set
    """
    vowels = set('aeiou')
    return vowels.intersection(set(word))
