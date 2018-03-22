# 深度优先算法的实现(伪代码)
def depth_tree(node_tree):
    if node_tree is not None:
        print(node_tree)
        if node_tree._left is not None:
            return depth_tree(node_tree._left)
        if node_tree._right is not None:
            return depth_tree(node_tree._right)


# 广度优先搜索
def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lChild is not None:
            my_queue.append(node.lChild)
        if node.rChild is not None:
            my_queue.append(node.rChild)


##深度用栈来实现(递归)
##广度用队列实现(FIFO)

