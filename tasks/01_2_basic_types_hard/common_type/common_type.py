def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type1 == type2:
        if type1 == range:
            return tuple
        return type1
    
    numeric_types: list[type] = [bool, int, float, complex]
    data_types: list[type] = [range, tuple, list]

    if (type1 in numeric_types) and (type2 in numeric_types):
        idx1: int = numeric_types.index(type1)
        idx2: int = numeric_types.index(type2)
        return numeric_types[max(idx1, idx2)]
    
    if (type1 in data_types) and (type2 in data_types):
        idx1: int = data_types.index(type1)
        idx2: int = data_types.index(type2)
        return data_types[max(idx1, idx2)]
    
    return str