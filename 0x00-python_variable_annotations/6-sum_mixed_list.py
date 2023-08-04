#!/usr/bin/env python3
"""
    sum_list annotation tutorial
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> int:
    """
        :param: mxd_lst: List of floats
        :return: Sum of all numbers in list
    """
    total_sum: int = 0
    for n in mxd_lst:
        total_sum = total_sum + n

    return total_sum
