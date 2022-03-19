from typing import Union


def relu(num: Union[int, float]) -> Union[int, float]:
    """function for get relu activation function

    Args:
        num (Union[int, float]): nilai weight

    Returns:
        Union[int, float]: output

    >>> print(relu(3))
    3

    >>> print(relu(-4))
    0
    """
    return max(0, num)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
