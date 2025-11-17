def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    i: int = 0
    j: int = 0
    lst_result: list[int] = []
    while i < len(lst_a):
        if j >= len(lst_b) or lst_a[i] < lst_b[j]:
            lst_result.append(lst_a[i])
            i += 1
        elif lst_b[j] == lst_a[i]:
            i += 1
        else:
            j += 1

    return lst_result
