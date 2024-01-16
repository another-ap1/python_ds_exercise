def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    #this creates a dictionary with how many of each numbers are in the list
    num_count = dict()
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    return max(num_count, key=lambda key:num_count[key])

    #num_count = {num_count[num] += 1 if num in nums else num_count[num] = 1 for num in nums}
