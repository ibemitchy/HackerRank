from collections import deque


def findMutationDistance(start, end, bank):
    visited_top = set()
    to_visit_top = deque()

    visited_bottom = set()
    to_visit_bottom = deque()

    depth = 0

    sequences = set(bank)

    # end must be in bank
    if end not in sequences:
        return -1

    # remove start to prevent cycle
    if start in sequences:
        bank.remove(start)

    to_visit_top.append(start)
    to_visit_top.append(None)
    to_visit_bottom.append(end)
    to_visit_bottom.append(None)

    return breadth_first_search(depth, bank, visited_top, to_visit_top, visited_bottom, to_visit_bottom)


def breadth_first_search(depth, bank, visited_top, to_visit_top, visited_bottom, to_visit_bottom):
    if len(to_visit_top) == 0:
        return -1
    current_sequence = to_visit_top.popleft()

    if current_sequence is None:
        depth += 1
        current_sequence = to_visit_top.popleft()

    visited_top.add(current_sequence)

    for sequence in bank:
        if sequence not in visited_top and is_single_mutation(current_sequence, sequence):
            if sequence in visited_bottom:
                return depth + 1
            to_visit_top.append(sequence)

    to_visit_top.append(None)

    return breadth_first_search(depth, bank, visited_bottom, to_visit_bottom, visited_top, to_visit_top)


def is_single_mutation(seq1, seq2):
    """
    Return True if sequences differ only at one base, else False.

    :type seq1: str
    :type seq2: str
    :rtype: bool
    """
    num_diff = 0

    for index in range(0, len(seq1)):
        if seq1[index] != seq2[index]:
            num_diff += 1

    return num_diff == 1
