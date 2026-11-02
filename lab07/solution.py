import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    if not values:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    return np.round(arr.mean(axis=0), 6).tolist()

