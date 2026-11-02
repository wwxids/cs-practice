import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    if not values:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()
