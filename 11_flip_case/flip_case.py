def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_phrase = list()
    for ltr in list(phrase):
        if (ltr == to_swap) or (ltr.swapcase() == to_swap):
            ltr = ltr.swapcase()
            swap_phrase.append(ltr)
        else:
            swap_phrase.append(ltr)
    return "".join(swap_phrase)
    