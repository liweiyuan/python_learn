#深度优先算法的实现(伪代码)
def depth_tree(node_tree):
    if node_tree is not None:
        print(node_tree)
        if node_tree._left is not None:
            return depth_tree(node_tree._left)
        if node_tree._right is not None:
            return depth_tree(node_tree._right)
