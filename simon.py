from collections import Counter
from random import random

###############################################################################
# Simulate Simon's rich-get-richer model, up to a time designated by the user
###############################################################################


def main(max_time, alpha, max_groups=float("Inf")):
    group_counts = Counter()
    initial_time = {}
    M = 0
    while M < max_groups:
        group_counts["1"] = 1
        initial_time["1"] = 1
        # Go up to max_time, first step is different
        for time in range(2, max_time + 1):
            if random() <= alpha:  # New word
                new_num = str(len(group_counts) + 1)
                group_counts[new_num] = 1
                initial_time[new_num] = time
                M += 1
            else:  # Old word, trickier case
                draw = random_pick(group_counts)
                group_counts[draw] += 1
        break

    return group_counts


def random_pick(group_counter):
    """
    Pick a random element from the counter, with the appropriate weighting
    and without converting it to an enormous list of elements
    """
    total_size = sum(group_counter.values())
    elements = list(group_counter.keys())
    percents = [group_counter[group] / total_size for group in elements]
    total = 0
    choice = random()
    for i, perc in enumerate(percents):
        total += perc
        if choice <= total:
            return elements[i]

    raise Exception("Error!")


if __name__ == "__main__":
    print(main())
