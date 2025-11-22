from collections import defaultdict
import heapq
import typing as tp

def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    return ''.join(c for c in text if c.isalpha() or c.isspace()).lower()


def get_words(
        query: str
        ) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    return [word for word in normalize(query).split() if len(word) > 3]


def build_index(
        banners: list[str]
        ) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    dict_: tp.DefaultDict[str, list[int]] = defaultdict(list[int])
    for banner_idx, banner_str in enumerate(banners):
        words: list[str]= get_words(banner_str)
        for word in words:
            banner_idx_list = dict_[word]
            if (not banner_idx_list) or (banner_idx_list[-1] != banner_idx):
                banner_idx_list.append(banner_idx)

    return dict_



def get_banner_indices_by_query(
        query: str,
        index: dict[str, list[int]]
        ) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    words: list[str] = get_words(query)

    ptrs: list[int] = [0] * len(words)
    heap: list[tuple[int, int]] = []
    for word_idx, word in enumerate(words):
        if index[word]:
            heap.append((index[word][0], word_idx))
    heapq.heapify(heap)

    cur_idx: int | None = None
    cur_idx_cnt: int = 0

    result: list[int] = []

    while heap:
        item, word_idx = heapq.heappop(heap)

        if item == cur_idx:
            cur_idx_cnt += 1
        else:
            cur_idx = item
            cur_idx_cnt = 1

        if (cur_idx is not None) and (cur_idx_cnt == len(words)):
            result.append(cur_idx)

        ptrs[word_idx] += 1
        word = words[word_idx]
        if (cur_ptr := ptrs[word_idx]) < len(index[word]):
            heapq.heappush(heap, (index[word][cur_ptr], word_idx))

    return result


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################


INDEX = {
   "купить": [0, 1, 2, 3, 4, 5, 6],
   "джинсы": [2, 3, 4],
   "скидка": [0, 3, 4, 5]
}

QUERY = "купить 5 джинсы скидка 100р"

LST = get_banner_indices_by_query(QUERY, INDEX)
