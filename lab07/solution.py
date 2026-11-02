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
