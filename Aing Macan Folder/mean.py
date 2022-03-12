from typing import List

def mean(nums : List[int]) -> float:
    """Fungsi manual untuk menghitung rata-rata

    Args:
        nums (List[int]): Data bilangan yang akan di inputkan

    Returns:
        float: rata-rata dari bilangan yang telah diinputkan

    >>> print(mean([1, 2, 3]))
    2.0
    """
    if type(nums) != list:
        raise TypeError("Hanya menerima List")

    return sum(nums) / len(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
