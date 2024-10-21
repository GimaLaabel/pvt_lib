from .common import Series_Type
from typing import List

def get_series(series_type: Series_Type, start, end, num_elements) -> List[float]:
    if series_type == Series_Type.LINEAR:
        return linear_series(start, end, num_elements)
    elif series_type == Series_Type.GEOMETRIC:
        return geometric_series(start, end, num_elements)


def linear_series(start, end, num_elements):
    if num_elements < 1:
        raise ValueError("Number of elements must be at least 1.")
    elif num_elements == 1:
        return [start]
    else:
        step = (end - start) / (num_elements - 1)
        series = [start + i * step for i in range(num_elements)]
        return series

def geometric_series(start, end, num_elements):
    if num_elements < 1:
        raise ValueError("Number of elements must be at least 1.")
    elif num_elements == 1:
        return [start]
    else:
        ratio = (end / start) ** (1 / (num_elements - 1))
        series = [start * (ratio ** i) for i in range(num_elements)]
        return series
