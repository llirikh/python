from collections import defaultdict
import enum
from itertools import zip_longest
import typing as tp


class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2

def topological_sort(
        vertex: str,
        graph: dict[str, set[str]],
        stack: list[str],
        is_visited: dict[str, Status]
        ):
    """
    Topological sorting of graph
    :param vertex: vertex of graph
    :param graph: graph with partial order
    :param stack: stack of vertex
    :param is_visited: flag if vertex is visited
    """
    is_visited[vertex] = Status.EXTRACTED

    for v in graph[vertex]:
        if is_visited[v] == Status.NEW:
            topological_sort(v, graph, stack, is_visited)

    is_visited[vertex] = Status.FINISHED
    stack.append(vertex)

def extract_alphabet(
        graph: dict[str, set[str]]
        ) -> list[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    stack: list[str] = []
    is_visited: dict[str, Status] = {v : Status.NEW for v in graph}

    for vertex in graph:
        if is_visited[vertex] == Status.NEW:
            topological_sort(vertex, graph, stack, is_visited)

    stack.reverse()
    return stack

def build_graph(
        words: list[str]
        ) -> dict[str, set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    result: tp.DefaultDict[str, set[str]] = defaultdict(set)

    if not words:
        return result

    if len(words) == 1:
        for c in words[0]:
            result[c]

    for i in range(len(words) - 1):
        ignore_flag = False
        for left_c, right_c in zip_longest(words[i], words[i + 1]):
            if left_c is not None:
                parent = result[left_c]

                if right_c is not None:
                    if left_c != right_c and (not ignore_flag):
                        parent.add(right_c)
                        ignore_flag = True

            if right_c is not None:
                result[right_c]
    return result

#########################
# Don't change this code
#########################

def get_alphabet(
        words: list[str]
        ) -> list[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
