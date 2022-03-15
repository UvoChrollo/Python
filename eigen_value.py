from scipy.linalg import eigvals
import numpy as np

def eigen_value(matrices : np.array) -> np.array:
    """Function to get eigen value

    Args:
        matrices (np.array): matrices that we want to get eigen value

    Returns:
        np.array: eigen value

    >>> print(eigen_value(np.array([[1,2],[2,1]])))
    [ 3.+0.j -1.+0.j]
    """
    return eigvals(matrices)

if __name__ == '__main__':
    import doctest
    doctest.testmod()