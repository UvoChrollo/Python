from typing import List

def pythagoras_2d(vector : List[int]) -> float:
    """
    >>> print(pythagoras_2d([3,4]))
    5.0
    """
    if len(vector) != 2:
        raise ValueError("Equation for 2D Pythagoras = (a*a + b*b)*0.5")
    else:
        return sum([arr * arr for arr in vector])**0.5
    
 def pythagoras_3d(vector : List[int]) -> float:
    """
    >>> print(pythagoras_3d([2,3,6]))
    7.0
    """
    if len(vector) != 3:
        raise ValueError("Equation for 3D Pythagoras = (a*a + b*b + c*c)*0.5")
    else:
        return sum([arr * arr for arr in vector])**0.5
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
