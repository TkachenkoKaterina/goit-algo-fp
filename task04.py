import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_pos = x - 1 / 2 ** layer
            pos[node.left.id] = (left_pos, y - 1)
            left_pos = add_edges(
                graph, node.left, pos, x=left_pos, y=y - 1, layer=layer + 1
                )
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(
                graph, node.right, pos, x=r, y=y - 1, layer=layer + 1
                )
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors
        )
    plt.show()


def build_heap_tree(heap):
    nodes = [Node(val) for val in heap]

    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0] if nodes else None


if __name__ == "__main__":
    heap = [10, 20, 5, 6, 1, 8, 9]
    root = build_heap_tree(heap)
    draw_tree(root)
