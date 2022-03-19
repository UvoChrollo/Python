from pythagoras import pythagoras as size
from vector_dot_product import dot_product as dp
import numpy as np
from typing import List

def scalar_projection(ax : np.array, bx : np.array) -> int:
    """
    >>> ax = np.array([3, -4, 0])
    >>> bx = np.array([10, 5, 6])
    >>> print(scalar_projection(ax, bx))
    2
    """
    if len(ax) == len(bx):
        return int(dp(ax, bx) / size(ax))
    else:
        raise ValueError("Unmatched length of vector")
        
def vector_projection(ax : np.array, bx : np.array) -> List[int]:
    """
    >>> ax = np.array([3, -4, 0])
    >>> bx = np.array([10, 5, 6])
    >>> print(vector_projection(ax, bx))
    [ 1.2 -1.6  0. ]
    """
    if len(ax) != len(bx):
        raise ValueError("Unmatched length of vector")
    return (dp(ax, bx)/size(ax)**2)*ax
if __name__ == '__main__':
    import doctest
    doctest.testmod()