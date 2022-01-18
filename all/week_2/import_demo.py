# sample script

def some_function():
    '''
    () -> None

    Prints Happy Canada Day to the user

    REQ: No requirements for this function

    >>> some_function()
    Happy Canada Day2
    '''
    # just print the function
    print("Happy Canada Day")
    # and return nothing
    return None

some_variable = 23

def some_other_func():
    '''
    Does nothing
    '''
    return None

def some_other_fun():
    '''
    Does nothing
    '''
    return None

def some_oth_func():
    '''
    Does nothing
    '''
    return None

if __name__ == "__main__": # don't want the marker to see what's below
    print("This is trash")
    import doctest
    doctest.testmod()
