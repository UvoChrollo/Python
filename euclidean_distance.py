import numpy as np


def euclidean(p1: np.array, p2: np.array) -> float:
    """get the distance between p1 and p2

    Args:
        p1 (np.array): _description_
        p2 (np.array): _description_

    Returns:
        float: euclidean distance between two points

    >>> p1 = np.array((1, 2, 3))
    >>> p2 = np.array((1, 1, 1))
    >>> print(euclidean(p1,p2))
    2.24
    """
    return round(np.linalg.norm(p1 - p2), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
