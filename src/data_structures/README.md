# Data Structures
    
## Linked List
A Linked List is a sequence of elements that are linked to each other, but do
not require to be in sequence in the memory. Different from what usually happens
when declaring an Array, a Linked List evolves dynamically according to insert and
delete requests. Here you can find the implementation of a Linked List that is 
independent of python iterable variables. Below is an usage example:

```python
from src.data_structures.basic_data_structures import LinkedList

my_list = LinkedList()

if my_list.is_empty():
    my_list.add_at_head(12.9)

my_list.add_at_head(1)
my_list.add_at_tail("hello")
my_list.add_at_index(1, False)
print("Current List:")
print(my_list)

string_value = my_list.get_index(3)
print(f"\nThe string added was: '{string_value}'")

popped_value = my_list.delete_from_head()
print(f"\nValue removed from list: '{popped_value}'")

print("\nFinal List:")
print(my_list)
```

## Queue and Stack
Queues and Stacks are very similar on their behavior, having only the main difference that
the first works iterates with data in a FIFO (First In, First Out) order, while the
second in a LIFO (Last In, First Out) order.

```python
from src.data_structures.basic_data_structures import Queue, Stack

def add_items_to_data_structure(data_structure):
    items_to_add = [1, "a", 50.6, True]
    for item in items_to_add:
        data_structure.add(item)

    print(data_structure)
    print(type(data_structure))

queue_example = Queue()
stack_example = Stack()

print("\nQueue implementation example:")
add_items_to_data_structure(queue_example)

print("\nStack implementation example:")
add_items_to_data_structure(stack_example)

print(f"\nValue removed from Queue: {queue_example.remove()}")
print(f"Value removed from Stack: {stack_example.remove()}")
```

## BinaryTree
Binary trees are structures that are build remembering a Tree structure,
where each node can point to 2 children, being the child in the left always smaller
and the one in the right equal or bigger, following the property below:

**BinaryTree property:** *Let x be a node in a binary search tree. If y is a node in the left subtree
of x, then y:key <= x:key. If y is a node in the right subtree of x, then
y:key >= x:key.*

This property brings benefits to this data structure, making it possible to sort it in **O(n)** and
insert or search nodes in **O(log n)** (worst case **O(n)**).

```python
from src.data_structures.binary_tree import BinaryTree

my_binary_tree = BinaryTree()

my_binary_tree.insert_node(True, 1)
my_binary_tree.insert_node("a", 2)
my_binary_tree.insert_node(180, 3)
my_binary_tree.insert_node("fookey", 4)
my_binary_tree.insert_node(12.1, 5)

my_binary_tree.set_value("a", 150)
print(f"Value from 'fookey' is: {my_binary_tree.get_value('fookey')}")

print("\nAscending order:")
print(f"\tKeys: {my_binary_tree.get_sorted_tree_keys()}")
print(f"\tValues: {my_binary_tree.get_sorted_tree_values()}")

print("\nDescending order:")
print(f"\tKeys: {my_binary_tree.get_sorted_tree_keys(reverse=True)}")
print(f"\tValues: {my_binary_tree.get_sorted_tree_values(reverse=True)}")
```

## Graphs
