"""
This equation, can be used to get length or magnitude of a vector
https://lakschool.com/en/math/vectors/vector-length-or-magnitude
"""

from typing import List

def pythagoras(vector : List[int]) -> float:
    """
    >>> print(pythagoras([3,4]))
    5.0
    
    >>> print(pythagoras([2,3,6]))
    7.0
    """
    return sum([arr * arr for arr in vector])**0.5
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
