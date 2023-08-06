#!/usr/bin/env python3
"""
    string and int/float to tuple
"""
from typing import Callable
import random


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        :param:
                multiplier: floats
                k: str
                v: Union[float, int]
        :return: Sum of all numbers in list
    """

    return lambda x: multiplier * x
