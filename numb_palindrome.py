def numb_palindrome(nums : int) -> bool:
    """is this number is Palindrome ?

    Args:
        nums (int): number that want to checked

    Returns:
        bool: palindrome or not

    >>> print(numb_palindrome(123))
    False

    >>> print(numb_palindrome(-121))
    False

    >>> print(numb_palindrome(121))
    True
    """
    return str(nums) == str(nums)[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()