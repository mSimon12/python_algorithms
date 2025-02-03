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

    def __search_element(self, searched_key, start_node: TreeNode):
        """
            Search a node in the key according to the desired key
        :param searched_key: pattern to be found
        :param start_node: position to start the search
        :return: node with the searched key
        """
        if (searched_key == start_node.key) or (start_node is None):
            return start_node

        if searched_key <= start_node.key:
            return self.__search_element(start_node.left, searched_key)
        else:
            return self.__search_element(start_node.right, searched_key)

    @staticmethod
    def __get_subtree_minimum(start_node: TreeNode):
        """
            Get the node with the smallest key from the subtree rooted in start_node
        :param start_node: root for the subtree
        :return: node with the smallest key
        """
        while start_node.left is not None:
            start_node = start_node.left

        return start_node

    @staticmethod
    def __get_subtree_maximum(start_node: TreeNode):
        """
            Get the node with the biggest key from the subtree rooted in start_node
        :param start_node: root for the subtree
        :return: node with the biggest key
        """
        while start_node.right is not None:
            start_node = start_node.right

        return start_node

    def get_node_successor(self, node:TreeNode):
        if node.right is not None:
            return self.__get_subtree_minimum(node.right)

        while node.parent and (node == node.parent.right):
            node = node.parent

        return node.parent

    def get_node_predecessor(self, node:TreeNode):
        if node.left is not None:
            return self.__get_subtree_maximum(node.left)

        while node.parent and (node == node.parent.left):
            node = node.parent

        return node.parent

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

    def insert_node(self, new_key:int, new_key_data = None):
        if self.is_empty():
            self.__root = TreeNode(new_key, data=new_key_data)
        else:
            self.__add_node_at_best_point(new_key, new_key_data, self.__root)

    def __transplant_node(self, replaced_node:TreeNode, moved_node:TreeNode):
        if replaced_node.parent is None:
            self.__root = moved_node
        elif replaced_node == replaced_node.parent.left:
            replaced_node.parent.left = moved_node
        else:
            replaced_node.parent.right = moved_node

        if moved_node is not None:
            moved_node.parent = replaced_node.parent

    def delete_node(self, key_to_delete):
        node_to_delete = self.__search_element(key_to_delete, self.__root)

        if node_to_delete.left is None:
            self.__transplant_node(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self.__transplant_node(node_to_delete, node_to_delete.left)
        else:
            subtree_minimum = self.__get_subtree_minimum(node_to_delete.right)
            if subtree_minimum.parent != node_to_delete:
                self.__transplant_node(subtree_minimum, subtree_minimum.right)
                subtree_minimum.right = node_to_delete.right
                subtree_minimum.right.parent = subtree_minimum
            self.__transplant_node(node_to_delete, subtree_minimum)
            subtree_minimum.left = node_to_delete.left
            node_to_delete.left.parent = subtree_minimum


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


