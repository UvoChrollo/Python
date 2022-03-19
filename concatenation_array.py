from typing import List


def concat_array(nums: List[int]) -> List[int]:
    """Leetcode Problem -> Concatenation of Array

    >>> print(concat_array([1,2,1]))
    [1, 2, 1, 1, 2, 1]
    >>> print(concat_array([1,3,2,1]))
    [1, 3, 2, 1, 1, 3, 2, 1]
    """
    nums2 = [nums[i] for i in range(len(nums))]
    nums.extend(nums2)
    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
