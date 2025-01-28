# This file provides examples of implementation of different data structures

class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class LinkedList:
    """
        Linked List class
    """

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """
            Verifies if the List is empty
        :return: emptiness status
        """
        if self.__head is None:
            return True

        return False

    def __get_last_node_and_parent(self):
        """
            Retrieve the last node from the list and his parent node
        :return: last_node, parent_from_last_node
        """
        if self.is_empty():
            return self.__head, None

        current_node = self.__head
        parent_node = current_node

        while current_node.next is not None:
            parent_node = current_node
            current_node = current_node.next

        return current_node, parent_node

    def __get_index_node_and_parent(self, index:int):
        """
            Retrieve the node in defined index position
        :param index: position to retrieve the node
        :return: node
        """
        if self.is_empty():
            raise IndexError("Index out of range!")

        count = 0
        current_node = self.__head
        parent_node = current_node

        while count != index:
            parent_node = current_node
            current_node = current_node.next
            if current_node is None:
                raise IndexError("Index out of range!")
            count += 1

        return current_node, parent_node

    def get_index(self, index:int):
        """
            Retrieve the item in defined index position
        :param index: position to retrieve the data
        :return: data
        """
        index_node, *_ =self.__get_index_node_and_parent(index)
        return index_node.data

    def add_at_head(self, new_value):
        """
            Add a new item to the beginning of th list
        :param new_value: value to be added to the list
        :return:
        """
        new_node = Node(new_value, self.__head)
        self.__head = new_node

    def add_at_tail(self, new_value):
        """
            Add a new item to the end of the list
        :param new_value: value to be added to the list
        :return:
        """
        if self.is_empty():
            self.__head = Node(new_value, None)
        else:
            last_node, *_ = self.__get_last_node_and_parent()
            last_node.next = Node(new_value, None)

    def add_at_index(self, new_value, index):
        """
            Add a new item to the specified index position
        :param new_value: value to be added to the list
        :param index: position to add the new item
        :return:
        """
        if self.is_empty():
            raise IndexError

        index_node, parent_node = self.__get_index_node_and_parent(index)
        parent_node.next = Node(new_value, index_node)

    def delete_from_head(self):
        """
            Remove the first item from the list
        :param index: position to remove the new item
        :return: value from the removed item
        """
        if self.is_empty():
            raise IndexError("Delete from empty list!")

        item_to_delete_data = self.__head.data
        self.__head = self.__head.next

        return item_to_delete_data

    def delete_from_end(self):
        """
            Remove the last item from the list
        :return: value from the removed item
        """
        if self.is_empty():
            raise IndexError("Delete from empty list!")

        last_node, parent_node = self.__get_last_node_and_parent()
        item_to_delete_data = last_node.data

        parent_node.next = None
        return item_to_delete_data

    def delete_from_index(self, index):
        """
            Remove the item from the list at index position
        :param index: position to remove the new item
        :return: value from the removed item
        """
        if self.is_empty():
            raise IndexError("Delete from empty list!")

        index_node, parent_node = self.__get_index_node_and_parent(index)
        parent_node.next = index_node.next

        return index_node.data

    def __str__(self):
        current_node = self.__head

        index = 0
        list_string = "index\tvalue"
        while current_node.next is not None:
            list_string += f"\n{index:5}\t{current_node.data}"
            current_node = current_node.next
            index += 1
        list_string += f"\n{index:5}\t{current_node.data}"

        return list_string


class Queue:

    def __init__(self):
        self.__queue_data = LinkedList()

    def add(self, new_queue_value):
        self.__queue_data.add_at_tail(new_queue_value)

    def remove(self):
        return self.__queue_data.delete_from_head()

    def __str__(self):
        return self.__queue_data.__str__()


class Stack:

    def __init__(self):
        self.__queue_data = LinkedList()

    def add(self, new_queue_value):
        self.__queue_data.add_at_head(new_queue_value)

    def remove(self):
        return self.__queue_data.delete_from_head()

    def __str__(self):
        return self.__queue_data.__str__()


class Tree:

    def __init__(self):
        pass


if __name__ == "__main__":
    my_list = LinkedList()

    def add_items_to_data_structure(data_structure):
        items_to_add = [1, "a", 50.6, True]
        for item in items_to_add:
            data_structure.add(item)

        print(data_structure)
        print(type(data_structure))

    queue_example = Queue()
    stack_example = Stack()

    print("Queue implementation example:")
    add_items_to_data_structure(queue_example)

    print("\nStack implementation example:")
    add_items_to_data_structure(stack_example)
