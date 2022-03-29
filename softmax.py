import numpy as np


def softmax(vector : np.array) -> np.array:
    """Function to get softmax value from a given vector

    >>> vec = np.array([5, 5])
    >>> softmax(vec)
    array([0.5, 0.5])

    >>> softmax([0])
    array([1.])
    """
    exponent_vector = np.exp(vector)

    sum_exponent = np.sum(exponent_vector)

    softmax_vector = exponent_vector / sum_exponent

    return softmax_vector


if __name__ == '__main__':
    import doctest
    doctest.testmod()