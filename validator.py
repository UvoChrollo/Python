import re

def email_validator(email : str) -> bool:
    """Melakukan pengecekan terhadap email, apakah valid atau tidak

    Args:
        email (str): Email yang akan dilakukan validasi

    Returns:
        bool: valid atau tidak nya suatu
    """
    pattern = r"[A-Za-z0-9_]+@gmail.com"
    result = [re.findall(pattern, email)]
    if len(result) > 0:
        return True
    else:
        return False

def pass_validator(pass: str) -> bool:
    """Melakukan pengecekan terhadap password, apakah valid atau tidak

    Args:
        pass (str): Password yang akan dilakukan validasi

    Returns:
        bool: valid atau tidak
    """
    pattern = r"[A-Za-z0-9!#%$&_-]{8, 20}"
    result = [re.findall(pattern, pass)]
    if len(result) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()