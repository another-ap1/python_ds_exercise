def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # new_list = list()
    # for val in lst:
    #     if bool(val) == True:
    #         new_list.append(val)
    # return new_list

    new_list = [val for val in lst if bool(val) == True]
    return new_list