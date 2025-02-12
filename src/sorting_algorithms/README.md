# Sorting Algorithms

Sorting algorithms are fundamental in computer science, used to arrange data in a 
specific order, typically numerical or lexicographical. These algorithms improve 
efficiency in searching, organizing, and processing data. Common sorting techniques 
include **Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and 
Heap Sort**, each with different time complexities and use cases. Simple algorithms 
like **Bubble Sort** are easy to implement but inefficient for large datasets, while 
advanced ones like **Quick Sort** and **Merge Sort** offer better performance with O(n log n)
complexity. Choosing the right sorting algorithm depends on factors like data size,
memory constraints, and stability requirements.

## Insertion Sort
The Insertion Sort is a simple algorithm the has as principle the iteration over all elements
of the array, comparing it to all the other elements. Due to this need of iterating over
all elements (n times) and the need to compare it to all the remaining (n + 1), the 
execution time gets a complexity of **O(n²)**. 

The algorithm keeps comparing the current
element with all the elements of smaller index until there are no elements or ir finds a 
smaller value. At each comparison that the value in the left is still bigger, it dislocates
the compared value to the right. When the smaller value is found, it finally places the current
value at the last free position.

```prettier
Example: 
    Initial array: [4, 3, 2, 1]

    Step 1: Insert 3 
    [4, 3, 2, 1]  → Compare 3 with 4, shift 4 right \
    [3, 4, 2, 1]  → Insert 3 at position 0 \
    
    Step 2: Insert 2 \
    [3, 4, 2, 1]  → Compare 2 with 4, shift 4 right \
    [3, 3, 4, 1]  → Compare 2 with 3, shift 3 right \
    [2, 3, 4, 1]  → Insert 2 at position 0 \
    
    Step 3: Insert 1 \
    [2, 3, 4, 1]  → Compare 1 with 4, shift 4 right \
    [2, 3, 3, 4]  → Compare 1 with 3, shift 3 right \
    [2, 2, 3, 4]  → Compare 1 with 2, shift 2 right \
    [1, 2, 3, 4]  → Insert 1 at position 0 \
    
    Sorted array: [1, 2, 3, 4]
```


