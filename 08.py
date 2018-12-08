import aoc


def build_tree(data):
    def parse_node():
        nonlocal data
        n_nodes, n_meta, *data = data
        nodes = [parse_node() for _ in range(n_nodes)]
        meta, data = data[:n_meta], data[n_meta:]
        return (nodes, meta)
    return parse_node()


def sum_metadata(tree):
    nodes, meta = tree
    return sum(meta) + sum(map(sum_metadata, nodes))


def node_value(tree):
    nodes, meta = tree
    if nodes:
        return sum(node_value(nodes[i-1]) for i in meta if i <= len(nodes))
    else:
        return sum(meta)


tree = build_tree(aoc.split(int))

print('Part One:', sum_metadata(tree))
print('Part Two:', node_value(tree))
