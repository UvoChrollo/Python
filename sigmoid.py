import numpy as np


def sigmoid(vector: np.array) -> np.array:
    """Function to get a sigmoid value from given vector

    >>> sigmoid(np.array([-1.0, 1.0, 2.0]))
    array([0.26894142, 0.73105858, 0.88079708])
    >>> sigmoid(np.array([0.0]))
    array([0.5])
    """
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
