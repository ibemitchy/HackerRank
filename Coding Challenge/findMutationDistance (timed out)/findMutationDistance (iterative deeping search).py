visited = set()


def findMutationDistance(start, end, bank):
    def depth_first_search(sequence, depth):
        if sequence == end:
            return True

        if depth == 0:
            return False

        print(depth)

        for index in range(len(sequence)):
            for char in ['A', 'T', 'C', 'G']:
                if sequence[index] != char:
                    mutation = sequence[:index] + char + sequence[index + 1:]

                    if mutation in sequences and mutation not in visited:
                        found = depth_first_search(mutation, depth - 1)
                        if found:
                            return found

    def iterative_depth_first_search(sequence):
        for depth in range(0, len(bank)):
            found = depth_first_search(sequence, depth)

            if found:
                return depth

        return -1

    sequences = set(bank)

    # end must be in bank
    if end not in sequences:
        return -1

    return iterative_depth_first_search(start)
