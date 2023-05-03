def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = list(phrase)
    for i in range(len(res)):
        if res[i] == to_swap.lower():
            res[i] = res[i].upper()
        elif res[i] == to_swap.upper():
            res[i] = res[i].lower()
    return ''.join(res)
