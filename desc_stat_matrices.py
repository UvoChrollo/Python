import numpy as np

def dsm(matrices : np.array) -> dict:
    """
    >>> test = dsm(np.array([[1,2],[3,4]]))
    >>> print(test)
    {'row': {'mean': [1.5, 3.5], 'median': [1.5, 3.5], 'std': [0.5, 0.5]}, 'col': {'mean': [2.0, 3.0], 'median': [2.0, 3.0], 'std': [1.0, 1.0]}}
    """
    result = {
        'row':{
            'mean':[np.mean(matrices[n].mean()) for n in range(matrices.shape[0])], 
            'median':[np.median(matrices[n]) for n in range(matrices.shape[0])],
            'std':[np.std(matrices[n]) for n in range(matrices.shape[0])]
            },
        'col':{
            'mean':[np.mean(matrices[:,n].mean()) for n in range(matrices.shape[0])],
            'median':[np.median(matrices[:,n]) for n in range(matrices.shape[0])],
            'std':[np.std(matrices[:,n]) for n in range(matrices.shape[0])]
        }
    }
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()