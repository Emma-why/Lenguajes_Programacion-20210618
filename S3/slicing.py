import numpy as np

def sum_col():
    array = np.random.randint(0, 101, size=(3, 3))
    col = array[:, 0]
    sumcol = np.sum(col)
    
    print(array)
    print(sumcol)

sum_col()
