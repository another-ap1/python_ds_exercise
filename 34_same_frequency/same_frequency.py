def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    #list_num1 = sorted([int(num) for num in str(num1)])
    #list_num2 = sorted([int(num) for num in str(num2)])
    return sorted([int(num) for num in str(num1)]) == sorted([int(num) for num in str(num2)])