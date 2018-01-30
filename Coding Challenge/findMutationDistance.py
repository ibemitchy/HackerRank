from collections import deque


def findMutationDistance(start, end, bank):
    """
    Convert DNA sequences to number and initialize breadth first search. Return minimal number of mutations.

    :param start: str
    :param end: str
    :param bank: str[]
    :return: number
    """
    # convert all DNA sequences to number
    sequences = set(map(to_number, bank))
    start = to_number(start)
    end = to_number(end)

    # end must be in bank
    if end not in sequences:
        return -1

    # remove start to prevent cycle
    if start in sequences:
        sequences.remove(start)

    # set up two way BFS
    visited_top = set()
    to_visit_top = deque()

    visited_bottom = set()
    to_visit_bottom = deque()

    # initialize root nodes
    to_visit_top.append(start)
    to_visit_bottom.append(end)

    depth = 0

    return breadth_first_search(depth, sequences, visited_top, to_visit_top, visited_bottom, to_visit_bottom)


def to_number(sequence):
    """
    Convert DNA sequence to number using bit operations. This allows for faster comparison of mutation positions later.

    :param sequence: str
    :return: number
    """
    nucleotide_dict = {
        'A': 0b00,
        'T': 0b01,
        'C': 0b10,
        'G': 0b11,
    }

    bin_sequence = 0b0

    for nucleotide in sequence:
        bin_sequence = bin_sequence << 2 | nucleotide_dict[nucleotide]

    return bin_sequence


def breadth_first_search(depth, sequences, visited_top, to_visit_top, visited_bottom, to_visit_bottom):
    """
    Two way breadth first search (same complexity as one-way, faster in practice). Return minimal number of mutations.

    :param depth: total depth from both top and bottom BFS.
    :param sequences: the sequence bank.
    :param visited_top: visited sequences by top BFS.
    :param to_visit_top: sequences top BFS should visit.
    :param visited_bottom: visited sequences by bottom BFS.
    :param to_visit_bottom: sequences bottom BFS should visit.
    :return: number
    """
    if len(to_visit_top) == 0:
        return -1

    new_to_visit = deque()

    # process all sequences that should be visited
    for sequence in to_visit_top:
        visited_top.add(sequence)

        # alter sequence in one sequence
        for index in range(0, 8):
            # choose one of four nucleotides
            for nucleotide in range(0, 4):
                # bitwise XOR allows for all permutations in one position
                # index * 2 because each nucleotide is 2 bits
                mutation = sequence ^ (nucleotide << (index * 2))

                if mutation in sequences and mutation not in visited_top:
                    # mutation visited by bottom BFS means the paths of two-way BFS have connected
                    if mutation in visited_bottom:
                        return depth
                    new_to_visit.append(mutation)
    
    # move to a new level
    depth += 1

    # top and bottom are flipped to allow BFS to alternate execution
    return breadth_first_search(depth, sequences, visited_bottom, to_visit_bottom, visited_top, new_to_visit)
