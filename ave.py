class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def ave(root):
    if root is None:
        return 0

    # Accumulate the sum of the values at each node visited
    sum_values = root.value
    num_nodes = 1
    stack = [root]
    while stack:
        node = stack.pop()
        for child in node.children:
            sum_values += child.value
            num_nodes += 1
            stack.append(child)

    # Divide the sum by the number of nodes visited to obtain the average value
    return sum_values / num_nodes

tree = Tree(11, [Tree(12), Tree(13, [Tree(14), Tree(15)])])
average_value = ave(tree)
print(average_value)  
