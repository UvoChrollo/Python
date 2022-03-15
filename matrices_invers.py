import numpy as np

def matrices_inversion(matrics : np.array) -> np.array:
    """_summary_

    >>> print(matrices_inversion(np.array([[1,2],[3,4]])))
    [[-2.  1.  ]
     [1.5 -0.5]]
    """
    return np.linalg.inv(matrics)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
