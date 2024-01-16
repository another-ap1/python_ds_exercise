def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # if len(lst):
    #     return lst[-1]
    # else:
    #     return None
    
    #rewrote with a one line if else
    return lst[-1] if len(lst) else None