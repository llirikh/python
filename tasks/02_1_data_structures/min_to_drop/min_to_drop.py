from collections import Counter
import typing as tp


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    if not seq:
        return 0

    cntr: tp.Counter[tp.Any] = Counter(seq)
    _, max_freq = cntr.most_common(1)[0]

    return len(seq) - max_freq
