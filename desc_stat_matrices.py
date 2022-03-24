import numpy as np


def mean(matrices: np.array) -> dict:
    """ Function for get mean, median and std for every row and col in matrices
    >>> test = mean(np.array([[1,2],[3,4]]))
    >>> print(test)
    {'row': [1.5, 3.5], 'col': [2.0, 3.0]}
    """
    result = {
        "row": [np.mean(matrices[n].mean()) for n in range(matrices.shape[0])],
        "col": [np.mean(matrices[:, n].mean()) for n in range(matrices.shape[0])]
    }
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
