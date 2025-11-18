from collections.abc import Sequence


def find_median(nums1: Sequence[int], nums2: Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    m: int = len(nums1)
    n: int = len(nums2)

    i: int = 0
    j: int = 0

    prev: int = -1
    cur: int = -1

    while (i + j) < (m + n) // 2:
        if j >= n:
            cur = nums1[i]
            i += 1
        elif i >= m:
            cur = nums2[j]
            j += 1
        else:
            if nums1[i] <= nums2[j]:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1

        prev = cur

    if i >= m:
        cur = nums2[j]
    elif j >= n:
        cur = nums1[i]
    else:
        cur = min(nums1[i], nums2[j])

    if (n + m) % 2 == 1:
        prev = cur
    
    return (prev + cur) / 2
