def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    def combine_keys_and_values(keys, values):
        combine = {}
        for key in keys:
            for val in values:
                combine[key] = val
                values.remove(val)
                break
        return combine
    
    if len(values) == len(keys):
        print('1')
        return combine_keys_and_values(keys, values)
    elif len(values) < len(keys):
        print('2')
        while len(values)< len(keys):
            values.append('None')
        return combine_keys_and_values(keys, values)
    elif len(keys) < len(values):
        print('3')
        return combine_keys_and_values(keys, values[:len(keys)])
    