from typing import List

def pythagoras(vector : List[int]) -> float:
    """
    >>> print(pythagoras([3,4]))
    5.0
    """
    if len(vector) != 2:
        raise ValueError("Equation for Pythagoras = (a*a + b*b)*0.5")
    else:
        return sum([arr * arr for arr in vector])**0.5
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
