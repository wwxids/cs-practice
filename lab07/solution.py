import numpy as np


def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:
        return []
    if not values:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()

def block(matrix, rows, columns):
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix):
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    return np.round(arr.mean(axis=0), 6).tolist()

def column_range(matrix,column):
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    col = arr[:, column]
    return round(float(col.max() - col.min()), 6)


test_matrix=[[1,2,3],[4,5,6],[7,8,9]]
test_values=[10,20,30,40,50,60]
if __name__=="__main__":
    print('reshape_rows:',reshape_rows(test_values,3))
    print('block:',block(test_matrix,[0,2],[1]))
    print('column_means:',column_means(test_matrix))
    print('column_range:',column_range(test_matrix,2))
    

