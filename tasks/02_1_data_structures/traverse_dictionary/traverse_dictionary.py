import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result: list[tuple[str, int]] = []
    for key in dct:
        if isinstance(dct[key], int):
            result.append((prefix + key, dct[key]))
        else:
            result_key: list[tuple[str, int]] = traverse_dictionary_immutable(dct[key], prefix + key + '.')
            result.extend(result_key)

    return result

def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for key in dct:
        if isinstance(dct[key], int):
            result.append((prefix + key, dct[key]))
        else:
            traverse_dictionary_mutable(dct[key], result, prefix + key + '.')


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    res: list[tuple[str, int]] = []
    stack: list[tp.Mapping[str, tp.Any]] = [dct]

    while stack:
        last: tp.Mapping[str, tp.Any] = stack.pop()
        for key in last:
            if isinstance(last[key], int):
                res.append((key, last[key]))
            else:
                new_dct: tp.Mapping[str, tp.Any] = {
                    (key + '.' + name):val for (name, val) in last[key].items()
                }
                stack.append(new_dct)

    return res
