#!/usr/bin/env python3
"""
    string and int/float to tuple
"""
from typing import Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[tuple[Sequence, int]]:
    """
        :param:
                lst: iterable object
        :return:
                element length
    """

    return [(i, len(i)) for i in lst]
