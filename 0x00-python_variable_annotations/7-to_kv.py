#!/usr/bin/env python3
"""
    string and int/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        :param:
                mxd_lst: List of floats
                k: str
                v: Union[float, int]
        :return: Sum of all numbers in list
    """

    return k, pow(v, 2)
