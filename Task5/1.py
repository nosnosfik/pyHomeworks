from enum import Enum


class SortOrder(Enum):
    ASC = False
    DSC = True


def is_sorted(num_list: list[int], sort_order: SortOrder) -> bool:
    for num in num_list:
        if not isinstance(num, int):
            raise TypeError
    return num_list == sorted(num_list, reverse=sort_order.value)


def transform(num_list: list[int], sort_order: SortOrder) -> list[int]:
    if is_sorted(num_list, sort_order):
        tmp_list = num_list.copy()
        for i, v in enumerate(tmp_list):
            tmp_list[i] = i + v
        return tmp_list
    else:
        return num_list