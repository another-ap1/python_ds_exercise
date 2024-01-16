def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    vowel_total = {}
    for ltr in phrase.lower():
        if ltr in vowels:
            if ltr in vowel_total:
                vowel_total[ltr]+=1
            else:
                vowel_total[ltr]=1
    return vowel_total