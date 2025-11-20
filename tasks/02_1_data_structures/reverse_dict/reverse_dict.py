import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    res_dict: dict[str, list[str]] = {}
    for key, value in dct.items():
        arr = res_dict.get(value)
        if arr is None:
            res_dict[value] = [key]
        else:
            arr.append(key)
    
    return res_dict