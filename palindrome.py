def palindrome(word : str) -> bool:
    """
    >>> print(palindrome("rar"))
    True

    >>> print(palindrome("marah"))
    False
    """
    return word == word[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()