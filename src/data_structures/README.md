# Data Structures
Data structures are fundamental components of computer science that help in organizing,
storing, and managing data efficiently. 
They enable optimal data manipulation, retrieval, and storage, improving the performance of algorithms. 
Common data structures include arrays, linked lists, stacks, queues, trees, 
and graphs, each suited for specific tasks. Below you can find examples of implementations
of these data structures and how to make use of it in your own projects.

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

A **graph** is a fundamental data structure in computer science and mathematics 
that models relationships between objects. It consists of **nodes (vertices)** 
connected by **edges**, which can be either **directed** (one-way) or **undirected**
(two-way). Graphs are used to represent a wide range of real-world structures, 
such as **social networks, road maps, computer networks, and dependency 
relationships**. Depending on their properties, graphs can be **weighted or 
unweighted, cyclic or acyclic, sparse or dense**. Due to their versatility, 
graphs are widely applied in **pathfinding, recommendation systems, 
AI, and network analysis**, making them an essential concept in both theoretical 
and practical computing.  

Graphs can be represented in two main ways: **Adjacency Lists** and 
**Adjacency Matrices**.  

### **Adjacency List**  
An adjacency list represents a graph as a **collection of lists**, where each node
has a list of its directly connected neighbors. This representation is 
**memory-efficient**, especially for sparse graphs, as it only stores existing edges. 
It is widely used in applications requiring efficient traversal, such as 
**BFS and DFS**, since it allows quick access to a node's neighbors.  

**Example of an adjacency list:**  
A → B, C \
B → D \
C → E \
D → \
E → \


This means **A** connects to **B and C**, **B** connects to **D**, and so on.  

### **Adjacency Matrix**  
An adjacency matrix is a **2D array (matrix)** where rows and columns represent 
nodes, and each cell contains **1 (if an edge exists) or 0 (if it does not)**. 
For weighted graphs, the matrix stores the weight instead of just 1s and 0s. 
While an adjacency matrix provides **constant-time edge lookups**, it is 
**memory-intensive for large, sparse graphs**, as it allocates space for all 
possible edges, even if many are missing.  

**Example of an adjacency matrix:**  

|   | A | B | C | D | E |
|---|---|---|---|---|---| 
| A | 0 | 1 | 1 | 0 | 0 | 
| B | 0 | 0 | 0 | 1 | 0 | 
| C | 0 | 0 | 0 | 0 | 1 | 
| D | 0 | 0 | 0 | 0 | 0 | 
| E | 0 | 0 | 0 | 0 | 0 |   


### **Choosing Between Adjacency List and Adjacency Matrix**  
- Use an **Adjacency List** for **sparse graphs** where memory efficiency is important.  
- Use an **Adjacency Matrix** for **dense graphs** or when **fast edge lookups** are needed.  

By selecting the right representation, graph algorithms can be optimized for 
performance and memory usage in real-world applications. At ``graphs.py`` we 
provide two classes that simplifies the construction of such structures by 
providing insert/delete commands for vertices and edges. The example usage is 
presented below.


```python
from src.data_structures.graphs import AdjListGraph, AdjMatrixGraph

my_graph = AdjListGraph()
# my_graph = AdjMatrixGraph()

my_graph.add_vertice("a")
my_graph.add_vertice("b")
my_graph.add_vertice("c")
my_graph.add_edge("a", "b")
my_graph.add_edge("a", "c")
my_graph.add_edge("b", "c")
my_graph.add_edge("c", "b")

print(my_graph)
```