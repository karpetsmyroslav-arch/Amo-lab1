from typing import List, Callable


def calculate_quantr(n: int, fun: Callable[[int], float], mode: str, start: int = 1) -> float:
    s: List[float] =[]
    for i in range(start, n + 1):
        s.append(fun(i))
    if mode == "sum":
        return sum(s)
    elif mode == "multiply":
        return multiply(s)
    else:
        raise ValueError("mode повинен бути 'sum' або 'multiply'")



def multiply(l: List[float]) -> float:
    result = 1
    for i in l:
        result *= i

    return result


def calculate_cyclic(a: List[float], b: List[float]) -> float:
    n = len(a)
    p = len(b)
    return calculate_quantr(
        n = n,
        fun = lambda i: calculate_quantr(
            n = p,
            fun = lambda j: formula(a[i - 1], b[j - 1]),
            mode = "multiply"
        ),
        mode = "sum"
    )


def formula(a: float, b: float) -> float:
    return a**2 + b**3