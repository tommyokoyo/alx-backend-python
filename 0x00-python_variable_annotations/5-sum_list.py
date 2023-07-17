#!/usr/bin/env python3
from typing import List
"""
    sum_list annotation tutorial
"""


def sum_list(input_list: List[float]) -> float:
    """
        :param input_list: List of floats
        :return: Sum of all numbers in list
    """
    total_sum: float = 0.0
    for n in input_list:
        total_sum = total_sum + n

    return total_sum
