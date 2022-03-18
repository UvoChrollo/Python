from numpy import pi, sqrt, exp

def normal_pdf(x : int, mu : float = 0.0, sigma : float = 1.0) -> float:
    """
    Fungsi untuk menghitung normal probability density function

    Args:
        mu (float): rata-rata yang diketahui
        sigma (float) : standard deviasi yang diketahui

    Return:
        float : Probability Density Function

    >>> print(normal_pdf(1,0,1))
    0.242

    >>> print(normal_pdf(3,4,5))
    0.078
    """
    result = 1 / sqrt(2 * pi * sigma**2) * exp(-((x - mu) ** 2) / (2 * sigma**2))
    return round(result, 3)