import heapq
import typing as tp

def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    ptrs: list[int] = [0] * len(seq)

    heap: list[tuple[int, int]] = [
        (s[0], seq_idx) for (seq_idx, s) in enumerate(seq) if s
    ]
    heapq.heapify(heap)

    result: list[int] = []

    while heap:
        item, seq_idx = heapq.heappop(heap)

        result.append(item)

        ptrs[seq_idx] += 1
        if ptrs[seq_idx] < len(seq[seq_idx]):
            heapq.heappush(heap, (seq[seq_idx][ptrs[seq_idx]], seq_idx))

    return result
