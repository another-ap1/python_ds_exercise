def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    capitalize_phrase = [word.capitalize() for word in phrase.lower().split(" ")]
    return (" ".join(capitalize_phrase))
