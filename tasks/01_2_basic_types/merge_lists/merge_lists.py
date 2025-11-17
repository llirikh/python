def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    lst_result: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(lst_a) or j < len(lst_b):
        if i >= len(lst_a):
            lst_result.append(lst_b[j])
            j += 1
            continue

        if j >= len(lst_b):
            lst_result.append(lst_a[i])
            i += 1
            continue

        if lst_a[i] <= lst_b[j]:
            lst_result.append(lst_a[i])
            i += 1
            continue

        lst_result.append(lst_b[j])
        j += 1

    return lst_result

def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a + lst_b)
