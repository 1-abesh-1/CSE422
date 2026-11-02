print("Second-last level MAX values:")

for node in second_last:

    children = tree[node]

    max_value = leaf_values[children[0]]
    pruned = []

    if max_value >= beta:
        pruned = children[1:]

    else:
        for i in range(1, len(children)):
            value = leaf_values[children[i]]

            if value > max_value:
                max_value = value

            if max_value >= beta:
                pruned = children[i + 1:]
                break

    if pruned:
        print(node, "=", max_value, "-", pruned[0], "can be pruned")
    else:
        print(node, "=", max_value)
