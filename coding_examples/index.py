print("Second-last level MAX values:")

for n in second_last:

    children = tree[n]

    max_v = leaf_values[children[0]]
    pruned = []

    if max_v >= beta:
        pruned = children[1:]

    else:
        for i in range(1, len(children)):
            v = leaf_values[children[i]]

            if v > max_v:
                max_v = v

            if max_v >= beta:
                pruned = children[i + 1:]
                break

    if pruned:
        print(n, "=", max_v, "-", pruned[0], "can be pruned")
    else:
        print(n, "=", max_v)
