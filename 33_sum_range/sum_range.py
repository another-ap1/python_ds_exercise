import math
def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    if start == 0 and end == None:
        return int(math.fsum(nums))
    elif end == None:
        return int(math.fsum(nums[start:]))
    # elif start == 0:
    #     return int(math.fsum(nums[:end+1]))
    else:
        return int(math.fsum(nums[start:end+1]))
    

