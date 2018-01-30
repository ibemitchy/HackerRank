let toVisit = [];
let sequences;
let endSequence;

function findMutationDistance(start, end, bank) {
    sequences = bank;
    endSequence = end;

    // bank must contain end sequence
    if (!bank.includes(end)) {
        return -1;
    }

    // remove starting sequence to prevent cycles in search
    if (sequences.includes(start)) {
        sequences.splice(sequences.indexOf(start), 1);
    }

    toVisit.push(start);
    // null indicates the end of the current tree level
    toVisit.push(null);

    let depth = 0;
    return search(depth);
}

/**
 * Breadth first search by adding single mutation sequences to frontier.
 *
 * @param depth: current level in search tree.
 * @returns {*}
 */
function search(depth) {
    // mutation not possible
    if (toVisit.length === 0) {
        return -1;
    }

    // BFS frontier
    let currSequence = toVisit.shift();

    // move onto the next level in tree
    if (currSequence === null) {
        depth++;
        currSequence = toVisit.shift();
    }

    if (currSequence === endSequence) {
        return depth;
    }

    // filter out single mutations
    for (let sequence of sequences) {
        if (isSingleMutation(currSequence, sequence)) {
            toVisit.push(sequence);
        }
    }

    // indicator of next level of tree
    toVisit.push(null);

    // remove sequences pushed to toVisit
    sequences = sequences.filter(seq => !isSingleMutation(seq, currSequence));
    return search(depth);
}

/**
 * Check if sequences differ at single base.
 *
 * @param seq1: first genetic sequence
 * @param seq2: second genetic sequence
 * @returns {boolean}
 */
function isSingleMutation(seq1, seq2) {
    let numDiff = 0;

    for (let index = 0; index < seq1.length; index++) {
        if (seq1.charAt(index) !== seq2.charAt(index)) {
            numDiff++;
        }
    }

    return numDiff === 1;
}
