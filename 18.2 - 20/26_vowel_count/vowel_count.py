def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {'o', 'a', 'e', 'u', 'i'}
    res = {}
    for c in phrase.lower():
        if c in vowels:
            res[c] = 1 + res.get(c, 0)
    return res
