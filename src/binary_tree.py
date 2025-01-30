# BinaryTree property
# Let x be a node in a binary search tree. If y is a node in the left subtree
# of x, then y:key <= x:key. If y is a node in the right subtree of x, then
# y:key >= x:key.

class TreeNode:

    def __init__(self, key, data = None, parent = None):
        self.key = key
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

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

    def __add_node_at_best_point(self, new_key, new_key_data, parent_node: TreeNode):
        if new_key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = TreeNode(new_key, data=new_key_data, parent=parent_node)
            else:
                self.__add_node_at_best_point(new_key, new_key_data, parent_node.left)
        else:
            if parent_node.right is None:
                parent_node.right = TreeNode(new_key, data=new_key_data, parent=parent_node)
            else:
                self.__add_node_at_best_point(new_key, new_key_data, parent_node.right)

    def __in_order_walk(self, node: TreeNode):
        if node is not None:
            self.__in_order_walk(node.left)
            print(f"{node.key}")
            self.__in_order_walk(node.right)

    def __pre_order_walk(self, node: TreeNode):
        if node is not None:
            print(f"{node.key}")
            self.__pre_order_walk(node.left)
            self.__pre_order_walk(node.right)

    def __post_order_walk(self, node: TreeNode):
        if node is not None:
            self.__post_order_walk(node.left)
            self.__post_order_walk(node.right)
            print(f"{node.key}")

    def __search_element(self, searched_element, node: TreeNode):
        if (searched_element == node.key) or (node is None):
            return node

        if searched_element <= node.key:
            return self.__search_element(node.left, searched_element)
        else:
            return self.__search_element(node.right, searched_element)

    @staticmethod
    def __get_tree_minimum(node: TreeNode):
        while node.left is not None:
            node = node.left

        return node

    @staticmethod
    def __get_tree_maximum(node: TreeNode):
        while node.right is not None:
            node = node.right

        return node

    def get_node_successor(self, node:TreeNode):
        if node.right is not None:
            return self.__get_tree_minimum(node.right)

        while node.parent and (node == node.parent.right):
            node = node.parent

        return node.parent

    def get_node_predecessor(self, node:TreeNode):
        if node.left is not None:
            return self.__get_tree_maximum(node.left)

        while node.parent and (node == node.parent.left):
            node = node.parent

        return node.parent

    def insert_node(self, new_key:int, new_key_data = None):
        if self.is_empty():
            self.__root = TreeNode(new_key, data=new_key_data)
        else:
            self.__add_node_at_best_point(new_key, new_key_data, self.__root)

    def get_value(self, key):
        key_node = self.__search_element(key, self.__root)
        return key_node.data

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

    my_binary_tree.insert_node(10, [10,52,"s"])
    my_binary_tree.insert_node(55)
    my_binary_tree.insert_node(5)
    my_binary_tree.insert_node(180)
    my_binary_tree.insert_node(120)

    print(my_binary_tree.get_value(10))

    # print(my_binary_tree)


