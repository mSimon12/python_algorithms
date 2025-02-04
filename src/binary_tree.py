
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

    @staticmethod
    def __hash_key(input_key):
        """
            Convert the key to a unique type to be processed as same for all request
        :param input_key: key provided by the user
        :return: hashed key
        """
        try:
            return str(input_key)
        except TypeError:
            raise IndexError("Invalid key type! It must be hashable.")

    def __search_element(self, searched_key, start_node: TreeNode):
        """
            Search a node in the key according to the desired key
        :param searched_key: pattern to be found
        :param start_node: position to start the search
        :return: node with the searched key
        """
        hashed_searched_key = self.__hash_key(searched_key)

        if (start_node is None) or (hashed_searched_key == self.__hash_key(start_node.key)):
            return start_node

        if hashed_searched_key <= self.__hash_key(start_node.key):
            return self.__search_element(searched_key, start_node.left)
        else:
            return self.__search_element(searched_key, start_node.right)

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

    def get_node_successor(self, reference_node:TreeNode):
        """
            Get the node that succeeds the provided node
        :param reference_node: node to have successor found
        :return: successor node
        """
        if reference_node.right is not None:
            return self.__get_subtree_minimum(reference_node.right)

        while reference_node.parent and (reference_node == reference_node.parent.right):
            reference_node = reference_node.parent

        return reference_node.parent

    def get_node_predecessor(self, reference_node:TreeNode):
        """
            Get the node that proceeds the provided node
        :param reference_node: node to have predecessor found
        :return: predecessor node
        """
        if reference_node.left is not None:
            return self.__get_subtree_maximum(reference_node.left)

        while reference_node.parent and (reference_node == reference_node.parent.left):
            reference_node = reference_node.parent

        return reference_node.parent

    def __add_node(self, new_key, new_key_data, parent_node: TreeNode):
        """
            Recurrent method for adding node to the right tree position
        :param new_key: new key to be added
        :param new_key_data: value associated to the key
        :param parent_node: node parent to the new node
        :return: None
        """
        hashed_new_key = self.__hash_key(new_key)

        if hashed_new_key < self.__hash_key(parent_node.key):
            if parent_node.left is None:
                parent_node.left = TreeNode(new_key, data=new_key_data, parent=parent_node)
            else:
                self.__add_node(new_key, new_key_data, parent_node.left)
        else:
            if parent_node.right is None:
                parent_node.right = TreeNode(new_key, data=new_key_data, parent=parent_node)
            else:
                self.__add_node(new_key, new_key_data, parent_node.right)

    def insert_node(self, new_key, new_key_data = None):
        """
            Inserts a new element to the Tree
        :param new_key: key from the new element
        :param new_key_data: value from the new element
        :return: None
        """
        if isinstance(new_key, list):
            raise IndexError("Key must not be a List!")
        elif isinstance(new_key, dict):
            raise IndexError("Key must not be a Dict!")

        if self.is_empty():
            self.__root = TreeNode(new_key, data=new_key_data)
        else:
            node_exist = self.__search_element(new_key, self.__root)
            if node_exist:
                raise IndexError("Key already exists!")

            self.__add_node(new_key, new_key_data, self.__root)

    def __transplant_node(self, replaced_node:TreeNode, moved_node:TreeNode):
        """
            Transplant node to a position of another node (moved_node >> replace_node
        :param replaced_node: node to be substituted
        :param moved_node: node having the position on tree changed
        :return: None
        """
        if replaced_node.parent is None:
            self.__root = moved_node
        elif replaced_node == replaced_node.parent.left:
            replaced_node.parent.left = moved_node
        else:
            replaced_node.parent.right = moved_node

        if moved_node is not None:
            moved_node.parent = replaced_node.parent

    def delete_node(self, key_to_delete):
        """
            Delete node with specified key from the Tree
        :param key_to_delete: key from the element to be deleted
        :return: None
        """
        node_to_delete = self.__search_element(key_to_delete, self.__root)
        if node_to_delete is None:
            raise IndexError("Invalid key!")

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

    def set_value(self, key, element_data):
        """
            Update the value from an existing element
        :param key: key from the node to receive a new value
        :param element_data: value to be assigned to the node
        :return: None
        """
        key_node = self.__search_element(key, self.__root)
        if key_node is None:
            raise IndexError("Invalid key!")
        key_node.data = element_data

    def get_value(self, key):
        """
            Get the value from the node matching the desired key
        :param key: key from the node be returned
        :return: value from the requested node
        """
        key_node = self.__search_element(key, self.__root)
        if key_node is None:
            raise IndexError("Invalid key!")
        return key_node.data

    def __in_order_walk_ascending(self, node: TreeNode, result: list):
        if node is not None:
            self.__in_order_walk_ascending(node.left, result)
            result.append(node)
            self.__in_order_walk_ascending(node.right, result)

    def __in_order_walk_descending(self, node: TreeNode, result: list):
        if node is not None:
            self.__in_order_walk_descending(node.right, result)
            result.append(node)
            self.__in_order_walk_descending(node.left, result)

    def __pre_order_walk(self, node: TreeNode, result: list):
        if node is not None:
            result.append(node)
            self.__pre_order_walk(node.left, result)
            self.__pre_order_walk(node.right, result)

    def __post_order_walk(self, node: TreeNode, result: list):
        if node is not None:
            self.__post_order_walk(node.left, result)
            self.__post_order_walk(node.right, result)
            result.append(node)

    def get_sorted_tree_keys(self, reverse=False):
        """
            Get the keys from the Tree sorted nodes
        :param reverse: The reverse flag can be set to sort in descending order
        :return: sorted nodes keys
        """
        sorted_nodes = []
        if reverse:
            self.__in_order_walk_descending(self.__root, sorted_nodes)
        else:
            self.__in_order_walk_ascending(self.__root, sorted_nodes)

        sorted_keys = [node.key for node in sorted_nodes]
        return sorted_keys

    def get_sorted_tree_values(self, reverse=False):
        """
            Get the values from the Tree sorted nodes
        :param reverse: The reverse flag can be set to sort in descending order
        :return: sorted nodes values
        """
        sorted_nodes = []
        if reverse:
            self.__in_order_walk_descending(self.__root, sorted_nodes)
        else:
            self.__in_order_walk_ascending(self.__root, sorted_nodes)

        sorted_values = [node.data for node in sorted_nodes]
        return sorted_values

    def __str__(self):
        tree_string = "Tree"
        return tree_string
