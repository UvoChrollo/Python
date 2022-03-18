import numpy as np
from math import cos, radians

def dot_product(a : np.array, b : np.array) -> int:
    """
    >>> a,b = np.array([-1, 2, 3]), np.array([2, 0, -2])
    >>> print(dot_product(a,b))
    -8
    """
    return sum(a * b)

def dot_cos(a : int = 1, b : int = 1, cosine : int = 0) -> int:
    """
    >>> print(dot_cos(6, 5, 60))
    15

    >>> print(dot_cos(30, 60))
    15
    """
    return int(a * b * cos(radians(cosine)))

if __name__ == '__main__':
    import doctest
    doctest.testmod