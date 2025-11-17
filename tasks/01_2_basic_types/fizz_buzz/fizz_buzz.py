def get_fizz_buzz(n: int) -> list[int | str]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    list_: list[int | str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            list_.append("FizzBuzz")
            continue
        if i % 5 == 0:
            list_.append("Buzz")
            continue
        if i % 3 == 0:
            list_.append("Fizz")
            continue
        list_.append(i)
    return list_
