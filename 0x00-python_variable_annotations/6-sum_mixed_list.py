#!/usr/bin/env python3
"""
    sum_list annotation tutorial
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        :param: mxd_lst: List of floats
        :return: Sum of all numbers in list
    """

    return sum(mxd_lst)
