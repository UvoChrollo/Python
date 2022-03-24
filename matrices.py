import numpy as np


def scalar_multiplication(matrices: np.array, n: int) -> np.array:
    """Get a scalar multiplication
    >>> print(scalar_multiplication(np.array([[4,2],[2,5]]), 5))
    [[20 10]
     [10 25]]
    """
    return matrices * n

def determinant(matrices: np.array) -> int:
    """
    >>> print(determinant(np.array([[2,5],[4,3]])))
    -14
    """
    return int(np.linalg.det(matrices))


def matrices_inversion(matrics: np.array) -> np.array:
    """Function to get invers by a matrices

    >>> print(matrices_inversion(np.array([[1,2],[3,4]])))
    [[-2.   1. ]
     [ 1.5 -0.5]]
    """
    return np.linalg.inv(matrics)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
