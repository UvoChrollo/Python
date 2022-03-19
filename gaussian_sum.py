def gaussian_sum(n: int) -> int:
    """ Fungsi untuk menghitung penjumlahan gaussian
    >>> print(gaussian_sum(10))
    55
    
    >>> print(gaussian_sum(100))
    5050
    """
    return int(n * (n + 1) / 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
