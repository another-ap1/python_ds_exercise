def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    # THE WAY I FIRST WROTE IT THE CODE BELOW THIS IS HOW I WROTE WITH TANARY OPERATOR
    # if operation == 'add':
    #     if make_int == False:
    #         return f'{message} {a+b}'
    #     else:
    #         return f'{message} {int(a+b)}'
    # elif operation == 'subtract':
    #     if make_int == False:
    #         return f'{message} {a-b}'
    #     else:
    #         return f'{message} {int(a-b)}'
    # elif operation == 'multiply':
    #     if make_int == False:
    #         return f'{message} {a*b}'
    #     else:
    #         return f'{message} {int(a*b)}'
    # elif operation == 'divide':
    #     if make_int == False:
    #         return f'{message} {a/b}'
    #     else:
    #         return f'{message} {int(a/b)}'
    # else:
    #     return None
    
    #addition
    if operation == 'add':
        return f'{message} {a+b}' if make_int == False else f'{message} {int(a+b)}' if operation == 'add' else None

    #subtraction
    if operation == 'subtract':
        return f'{message} {a-b}' if make_int == False else f'{message} {int(a-b)}' if operation == 'subtract' else None

    #multiplication
    if operation == 'multiply':
        return f'{message} {a*b}' if make_int == False else f'{message} {int(a*b)}' if operation == 'multiply' else None

    #division
    if operation == 'divide':
        return f'{message} {a/b}' if make_int == False else f'{message} {int(a/b)}' if operation == 'division' else None
    else:
        None