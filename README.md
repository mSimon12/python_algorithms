# Python Algorithms

Performance processing an application is always welcome.
Therefore, here I include a set of data structures and algorithms implemented to 
execute their task in the most efficient way.

## Data Structures
Data structures are fundamental components of computer science that help in organizing,
storing, and managing data efficiently. 
They enable optimal data manipulation, retrieval, and storage, improving the performance of algorithms. 
Common data structures include arrays, linked lists, stacks, queues, trees, 
and graphs, each suited for specific tasks. 
I can consider the following table to do the best choice when deciding which one to use.

| **Data Structure**    | **Access Time** | **Search Time** | **Insertion/Deletion** | **Memory Usage** | **Best Use Cases** |
|-----------------------|----------------|-----------------|------------------------|------------------|---------------------|
| **Array**            | O(1)            | O(n)            | O(n) (for shifting)    | Fixed size       | Static data, fast index access |
| **Linked List**      | O(n)            | O(n)            | O(1) (at head/tail)    | Dynamic size     | Frequent insertions/deletions |
| **Stack**           | O(n)            | O(n)            | O(1) (push/pop)        | Dynamic size     | Backtracking, function calls |
| **Queue**           | O(n)            | O(n)            | O(1) (enqueue/dequeue) | Dynamic size     | Scheduling, breadth-first search |
| **Hash Table / Dict** | O(1) (average) | O(1) (average)  | O(1) (average)        | High (depends on load factor) | Fast lookups, key-value mapping (e.g., Python `dict`) |
| **Binary Tree**      | O(log n)        | O(log n)        | O(log n) (balanced)   | Dynamic size     | Hierarchical data, search trees |

In this repository I have implemented Linked List, Queue, Stack and BinaryTree which are introduced at
[Data Structures](src/data_structures). To verify the specifics of each type, I have accomplished a set of 
test to measure memory usage and performance in different conditions.

### Memory
When we put different data structures holding the same data we can verify the difference memory needed
by each one. I have compared the memory needed by [List, Dictionary, Linked List, Queue, Stack and Binary Tree]
to hold 400 random data values. These values were added one by one and the memory after each inclusion
was measured.

The result shows continuous increase in the memory for the types I have implements here, and continuous increase
followed by periodical resize of the data chunks for the List and the Dictionary. The memory required by 
the new structures is 4 to 5 times bigger than the needed for a List, due to the implementation of a Node
class that is used in the dynamic allocation of the data.

<p align="center">
 <img alt="Comparison of memory usage of data structures" src="src/outputs/memory_usage.png" width="500">
</p>

**Arrays** generally offer better memory efficiency for small datasets due to their contiguous storage, 
minimal overhead, and superior cache locality, making them ideal for fast random access. However, 
they suffer from resizing overhead and fragmentation issues when dynamically growing. 
In contrast, **Linked Lists** provide flexible memory allocation and efficient insertions/deletions without 
resizing, making them preferable for frequently changing data structures. Despite this advantage, 
linked lists have higher memory overhead due to pointers and suffer from poor cache locality.

### Processing Time
In addition to the memory analysis, we have verified the processing time to **Insert**, **Search** and **Delete**
values from 4 types of data structure (List, Linked List, Dictionary and Trees). Of course the comparison of a 
structure developed completely in Python against a built-in python type (processed a C code) is not fair. Although,
we can verify the complexity time for each type. The three tests (Insertion, Search and Deletion) where executed with 
20.000 random datapoints, to be processed in random indexes of the structures, avoiding getting only best time from the executions. 
- With the tests it was confirmed the **linear complexity O(n)** from the **List** and **Linked List**(as in the table above), 
due to the constant need of data shift for the List and the dependency on a search for the Linked List.
 - When we verify the processing time for the **Dictionary** and for the **Binary Tree**, we can see a better performance.
The Binary Tree presents the expected behavior of a **O(log n)**, verified by comparing it to the reference curve. 
And the Dictionary, since it is implemented in python as a hash table, has shown a constant behavior, with some
noticeable variations after 3.000 datapoints, which might be justified due to table resizing, memory overhead or 
hash collisions (rare cases).

<p align="center">
 <img alt="Insertion time comparison" src="src/outputs/insertion_time.png" width="250">
 <img alt="Search time comparison" src="src/outputs/search_time.png" width="250">
 <img alt="Delete time comparison" src="src/outputs/delete_time.png" width="250">
</p>

## Algorithms