import numpy as np
import math


def multivariate_0(x,y,z) -> tuple[float, float, float]:
    return x, y, z


def multivariate_1(x,y,z) -> tuple[float, float, float]:
    return x + 16 * math.sin(y) * math.sin(x) * math.cos(z), y + 16 * math.sin(z) * math.sin(y) * math.cos(x), z + 16 * math.sin(y) * math.sin(z) * math.cos(x)


def multivariate_2(x,y,z) -> tuple[float, float, float]:
    return x + 16 * math.sin(y), y + 16 * math.sin(z), z + 16 * math.sin(y)


def multivariate_3(x,y,z) -> tuple[float, float, float]:
    return x + 16 * math.cos(x), y + 16 * math.sin(x), z + 16 * math.sin(x)


functions = [multivariate_0, multivariate_1, multivariate_2, multivariate_3]