def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    if b <= a <= c or c <= a <= b:
        return a
    
    if a <= b <= c or c <= b <= a:
        return b
    
    return c
