from typing import List


def array_permutation(nums: List[int]) -> List[int]:
    """Leetcode Problem : Build Array from Permutation

    >>> print(array_permutation([5,0,1,2,3,4]))
    [4, 5, 0, 1, 2, 3]

    >>> print(array_permutation([0,2,1,5,3,4]))
    [0, 1, 2, 4, 5, 3]
    """
    return [nums[nums[x]] for x in range(len(nums))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
