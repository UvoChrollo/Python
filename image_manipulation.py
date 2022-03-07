"""
Google IT Automation with Python W1
Manipulating Images

1. Rotate the image 90° clockwise
2. Resize the image from 192x192 to 128x128
3. Save the image to a new folder in .jpeg format
"""
from PIL import Image

def image_manipulator(img):
    """Function for rotate, resize and save the image as a new format

    Args:
        img (_type_): which picture should we convert ?

    >>> image_manipulator() # doctest: +SKIP
    """
    fn = img.replace('jpg','jpeg')
    im = Image.open(img)
    im.rotate(90).resize((128,128)).save(fn)

if __name__ == '__main__':
    import doctest
    doctest.testmod()