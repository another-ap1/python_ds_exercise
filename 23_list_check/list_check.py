def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    check_if_true = all([True if isinstance(val, list) else False for val in lst])
    return check_if_true
    