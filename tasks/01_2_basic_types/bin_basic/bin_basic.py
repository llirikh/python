def find_value(nums: list[int] | range, value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    i: int = -1
    j: int = len(nums)
    while i + 1 != j:
        middle: int = (i + j) // 2
        if nums[middle] <= value:
            i = middle
        else:
            j = middle

        if nums[i] == value:
            return True

    return False
