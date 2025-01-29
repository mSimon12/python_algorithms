
class TreeNode:

    def __init__(self, data, parent = None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.__root = None

    def is_empty(self):
        """
            Verifies if the Tree is empty
        :return: emptiness status
        """
        if self.__root is None:
            return True

        return False

    def __add_node_at_best_point(self, new_value, parent_node: TreeNode):
        if new_value < parent_node.data:
            if parent_node.left is None:
                parent_node.left = TreeNode(new_value, parent=parent_node)
            else:
                self.__add_node_at_best_point(new_value, parent_node.left)
        else:
            if parent_node.right is None:
                parent_node.right = TreeNode(new_value, parent=parent_node)
            else:
                self.__add_node_at_best_point(new_value, parent_node.right)

    def insert_node(self, new_value):
        if self.is_empty():
            self.__root = TreeNode(new_value)
        else:
            self.__add_node_at_best_point(new_value, self.__root)

    def __in_order_walk(self, node: TreeNode):
        if node is not None:
            self.__in_order_walk(node.left)
            print(f"{node.data}")
            self.__in_order_walk(node.right)

    def __pre_order_walk(self, node: TreeNode):
        if node is not None:
            print(f"{node.data}")
            self.__pre_order_walk(node.left)
            self.__pre_order_walk(node.right)

    def __post_order_walk(self, node: TreeNode):
        if node is not None:
            self.__post_order_walk(node.left)
            self.__post_order_walk(node.right)
            print(f"{node.data}")

    def __str__(self):
        tree_string = "Tree"
        self.__pre_order_walk(self.__root)
        print()
        self.__in_order_walk(self.__root)
        print()
        self.__post_order_walk(self.__root)
        print()
        return tree_string


if __name__ == "__main__":
    my_binary_tree = BinaryTree()

    my_binary_tree.insert_node(10)
    my_binary_tree.insert_node(55)
    my_binary_tree.insert_node(5)
    my_binary_tree.insert_node(180)
    my_binary_tree.insert_node(120)

    print(my_binary_tree)
    # 10
    #     55
    #         180
    #       120


