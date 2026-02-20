import math


def calculate_curved_function(k: float, c: float, p: float, a: float) -> float:
    if k * c > p:
        return math.sin(c * a)**2
    elif k * c < p:
        return math.cos(k * a)**2
    else:
        raise TypeError('Добуток k і c немає дорівнювати p')