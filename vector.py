import numpy as np
import math
import multivariate


def new(x: float, y: float, z: float) -> np.array:
    """
    :param x,y,z:
        The components of the new vector
    :return np.array:
        Returns a new vector
    """
    return np.array([x, y, z])


def get(vec: np.array) -> tuple[float, float, float]:
    """
    :param vec:
    :return:
        Returns the components of the vector
    """
    return vec[0], vec[1], vec[2]


def set(vec: np.array, x: float, y: float, z: float) -> None:
    """
    :param vec:
        The vector to set components of
    :param x,y,z:
        The components of the vector
    :return None:
    """
    vec[0], vec[1], vec[2] = x, y, z


def clone(vec: np.array) -> np.array:
    """
    :param vec:
        The vector to clone
    :return np.array:
        Returns a vector clone
    """
    return new(get(vec))


def add(vec1: np.array, vec2: np.array) -> np.array:
    """
    :param vec1, vec2:
        The vectors to be added
    :return np.array:
        Returns the sum of two vectors
    """
    return new(vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])


def sub(vec1: np.array, vec2: np.array) -> np.array:
    """
    :param vec1, vec2:
        The vectors to be subtracted
    :return np.array:
        Returns the subtraction of two vectors
    """
    return new(vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])


def mult(vec1: np.array, vec2: np.array) -> np.array:
    """
    :param vec1, vec2:
        The vectors to be multiplied
    :return np.array:
        Returns the product of two vectors
    """
    return new(vec1[0] * vec2[0], vec1[1] * vec2[1], vec1[2] * vec2[2])


def div(vec1: np.array, vec2: np.array) -> np.array:
    """
    :param vec1, vec2:
        The vectors to be divided
    :return np.array:
        Returns the quotient of two vectors
    """
    return new(vec1[0] / vec2[0], vec1[1] / vec2[1], vec1[2] / vec2[2])


def magnitude(vec: np.array) -> float:
    """
    :param vec:
        The vector to measure
    :return float:
        Returns the magnitude of the vector
    """
    return np.linalg.norm(vec)


def normal(vec: np.array) -> np.array:
    """
    :param vec:
        The vector to normalize
    :return np.array:
        Returns the normal of the vector
    """
    mag = magnitude(vec)
    if mag == 0:
        return new(0,0,0)
    else:
        return new(vec[0] / mag, vec[1] / mag, vec[2] / mag)


def dot(vec1: np.array, vec2: np.array) -> float:
    """
        :param vec1, vec2:
            The vectors to take dot product of
        :return float:
            Returns the dot product
        """
    return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]


def cross(vec1: np.array, vec2: np.array) -> np.array:
    """
    :param vec1, vec2:
        The vectors to take the cross product of
    :return np.array:
        Returns the cross products of the vectors
    """
    return new(
        vec1[1] * vec2[2] - vec1[2] * vec2[1],
        vec1[2] * vec2[0] - vec1[0] * vec2[0],
        vec1[0] * vec2[1] - vec1[1] * vec2[0]
    )


def rotate(vec: np.array, theta: float, phi: float) -> None:
    """
    :param vec:
        The vector to rotate
    :param theta, phi:
        The angles to rotate the vector by
    :return None:
    """
    ct, st = math.cos(theta), math.sin(theta)
    cp, sp = math.cos(phi), math.sin(phi)
    x, y, z = get(vec)
    set(vec,
        ct * x - st * y,
        cp * (st * x + ct * y) - sp * z,
        sp * (st * x + ct * y) + sp * z
    )


def apply_function(vec: np.array, index: int) -> None:
    """
    :param vec:
        The vector to apply the function to
    :param index:
        Index of the function to use
    :return None:
    """
    f = multivariate.functions[index]
    x, y, z = get(vec)
    x, y, z = f(x, y, z)
    set(vec, x, y, z)
