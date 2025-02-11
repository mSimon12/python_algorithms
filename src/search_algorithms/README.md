# Item Search

## Linear Search
Linear Search is a simple searching algorithm that sequentially checks each element in a list until 
the target value is found or the entire list is traversed. It works on both sorted and unsorted data, 
making it highly versatile but inefficient for large datasets. With a worst-case time complexity of **O(n)**, 
Linear Search is best suited for small lists or unsorted collections where sorting isn't feasible. 
Despite its inefficiency, it is useful in situations where the list is const    antly changing, as it does 
not require preprocessing like sorting.

```python
from src.search_algorithms.search import LinearSearch

data = [10, -50, 96, 23, 1069]
interest_value = 23

my_searcher = LinearSearch()

value_idx = my_searcher.search(data, interest_value)

if value_idx is not None:
    print(f"The value '{interest_value} is at index {value_idx}")
else:
    print("The searched value is not in the list!")
```

## Binary Search
Binary Search is a much faster searching algorithm that works exclusively on sorted lists. It follows a 
**divide-and-conquer approach** by repeatedly splitting the search space, eliminating half of the elements 
at each step. This results in an efficient **O(log n)** time complexity, making Binary Search ideal for 
large datasets where fast lookups are required. However, its primary drawback is that the data 
must be sorted beforehand, adding **O(n log n) cost if sorting is necessary**. Binary Search is 
widely used in applications like database indexing, searching in dictionaries, and finding elements in 
sorted arrays.

```python
from src.search_algorithms.search import BinarySearch

data = [10, -50, 96, 23, 1069]
interest_value = 23

my_searcher = BinarySearch()

value_idx = my_searcher.search(data, interest_value)

if value_idx is not None:
    print(f"The value '{interest_value} is at index {value_idx}")
else:
    print("The searched value is not in the list!")
```

# Graph Search

Graph Search algorithms present multiple benefits, since they can be very easily
modified to fit the problem in question. Some example applications are:
- Verify which nodes are reachable.
- Verify node existence in the graph.
- Find a path or the smallest one between 2 nodes.
- Count the amount of direct or undirected connections.
- Identify possible infinite cycles.

## BFS - Breadth-First Search
Breadth-First Search (BFS) is a fundamental graph traversal algorithm used to explore nodes in a 
**level-by-level manner**. It starts from a given source node, visiting all its immediate neighbors before 
moving on to their neighbors, continuing this process until all reachable nodes are explored. 
BFS is implemented using a queue (FIFO structure), ensuring that the shortest path (in terms of the number
of edges) is always found first in unweighted graphs. This makes it particularly useful for applications 
like shortest path finding, network broadcasting, and connected component detection in graphs.

One of the biggest advantages of BFS is its efficiency in unweighted graphs, running in O(V + E) time. 
It guarantees the shortest path in terms of the number of edges, making it ideal for routing problems, 
social networks, and AI pathfinding. However, BFS has drawbacks, such as high memory usage, as it needs 
to store all nodes at the current level before moving forward. This can be problematic in large graphs 
or trees. Additionally, unlike DFS, BFS is not well-suited for problems requiring deep exploration, such 
as backtracking puzzles or topological sorting.

The example below provides the shortest path from node A to each of the nodes from the graph.

```python
from src.data_structures.graphs import AdjListGraph
from src.search_algorithms.graphs_search import BFS

my_graph = AdjListGraph()

# Add vertices
my_graph.add_vertice("A")
my_graph.add_vertice("B")
my_graph.add_vertice("C")
my_graph.add_vertice("D")
my_graph.add_vertice("E")

# Add edges
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "E")
my_graph.add_edge("D", "C")

bfs = BFS(my_graph)
bfs_result = bfs.run("A")

for vertex in bfs_result:
    print(f"Distance from 'A' to '{vertex}': {bfs.get_shortest_path('A', vertex)}")
```

## DFS - Depth-First Search
Depth-First Search (DFS) is a graph traversal algorithm that **explores as deeply as possible** before 
backtracking. Starting from a given source node, it moves to an unvisited neighbor, continuing this 
process recursively until reaching a dead end, at which point it backtracks to explore other unexplored 
paths. DFS is typically implemented using a stack (either explicitly or via recursion) and is well-suited 
for problems requiring deep exploration, such as detecting cycles, topological sorting, and solving mazes. 
Unlike BFS, DFS does not guarantee the shortest path but is useful for systematically searching large or 
complex graphs.

One of the key advantages of DFS is its low memory usage compared to BFS, as it only needs to store the 
current path instead of maintaining all nodes at the current level. This makes it ideal for searching deep
trees or large graphs with sparse connections. However, DFS has some disadvantages, such as being 
inefficient for shortest path finding in unweighted graphs, where BFS is a better choice. Additionally, 
its recursive nature can lead to stack overflow issues in very deep graphs, requiring an iterative 
approach with an explicit stack for better control.

The example below makes use of the DFS to find a valid task sequence that keeps the tasks dependencies.

```python
from src.data_structures.graphs import AdjListGraph
from src.search_algorithms.graphs_search import DFS

task_graph = AdjListGraph()

tasks = ["A", "B", "C", "D", "E", "F"]
for t in tasks:
    task_graph.add_vertice(t)

# Tasks dependencies
task_graph.add_edge("A", "B")
task_graph.add_edge("A", "C")
task_graph.add_edge("B", "D")
task_graph.add_edge("C", "E")
task_graph.add_edge("E", "F")

dfs = DFS(task_graph)
dfs.run("F")

# Print task dependencies
print("Task Dependencies:")
for vertex in tasks:
    dependent_tasks = task_graph.get_graph()[vertex]
    if dependent_tasks:
        print(f"{vertex} -> {dependent_tasks}")

execution_order = dfs.get_topological_sort()
print("Task Execution Order:", execution_order)
```

## Dijkstra 
Dijkstra’s algorithm is a well-known method for finding the shortest path from a single source node to all 
other nodes in a weighted graph. It begins by initializing the source node’s distance to zero while setting
all other nodes to infinity. Using a priority queue, the algorithm selects the node with the smallest known
distance, updates its neighboring nodes with the shortest possible distances, and marks it as visited. 
This process repeats until all nodes have been processed, ensuring that each node’s shortest path from the 
source is found. The algorithm works efficiently with graphs that have non-negative weights and is widely 
applied in areas like GPS navigation, network routing, and transportation planning.

One of the main advantages of Dijkstra’s algorithm is its efficiency and accuracy in finding the shortest 
path in polynomial time, especially when implemented with a priority queue, reducing the complexity to 
O((V+E)logV). It is optimal for graphs with non-negative weights and works well for real-time pathfinding 
in maps and communication networks. However, a major disadvantage is that it fails with graphs containing 
negative weight edges, as it assumes that once a node’s shortest path is found, it cannot be improved.

```python
from src.data_structures.graphs import AdjMatrixGraph
from src.search_algorithms.graphs_search import Dijkstra

paths_graph = AdjMatrixGraph()

vertices = ["A", "B", "C", "D", "E"]
for vertex in vertices:
    paths_graph.add_vertice(vertex)

# Tasks dependencies
paths_graph.add_edge("A", "B", 5)
paths_graph.add_edge("A", "C", 10)
paths_graph.add_edge("B", "C", 3)
paths_graph.add_edge("B", "D", 9)
paths_graph.add_edge("B", "E", 2)
paths_graph.add_edge("C", "B",2)
paths_graph.add_edge("C", "D", 1)
paths_graph.add_edge("D", "E", 4)
paths_graph.add_edge("E", "A",7)
paths_graph.add_edge("E", "D", 6)

djk = Dijkstra(paths_graph)
djk_result = djk.run("A")

for vertex in djk_result:
    print(f"Distance from 'A' to '{vertex}': {djk_result[vertex].distance}")
```