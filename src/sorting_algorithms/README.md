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

## Merge Sort
The Merge Sort algorithm follows the dived-and-conquer principle, where it breaks
the problem into several subproblems that are similar to the original problem but
smaller in size, solve the subproblems recursively, and then combine these 
solutions to create a solution to the original problem. The algorithm proceeds (lg n + 1) 
levels of recursion, since it breaks the array in two at every recursion. Also, the process
of merging back the subarrays takes O(n), which makes Merge Sort outperform Insertion Sort 
by having a final complexity of **O(n * lg n)**.

The divide-and-conquer paradigm involves three steps at each level of the recursion:
1. Divide the problem into a number of subproblems that are smaller instances of the 
same problem.
2. Conquer the subproblems by solving them recursively. If the subproblem sizes 
are small enough, however, just solve the subproblems in a straightforward manner.
3. Combine the solutions to the subproblems into the solution for the original 
problem.

Merge Sort follows this principle by doing the following steps:
1. **Divide**: Divide the n-element sequence to be sorted into two subsequences 
of n/2 elements each.
2. **Conquer**: Sort the two subsequences recursively using merge sort.
3. **Combine**: Merge the two sorted subsequences to produce the sorted answer (compare
the smallest value from the 2 subsequences and get the smallest).

*The recursion “bottoms out” when the sequence to be sorted has length 1, in which
case there is no work to be done, since every sequence of length 1 is already in
sorted order.

    Example:
    Initial array: [4, 3, 2, 1]

        [4, 3, 2, 1]
          /        \
       [4, 3]      [2, 1]
        / \          / \
      [4] [3]      [2] [1] 
        \ /          \ /
       [3, 4]      [1, 2]
          \        /
         [1, 2, 3, 4]

    Final array: [4, 3, 2, 1]

## QuickSort

QuickSort is a divide-and-conquer sorting algorithm that works by selecting a "pivot" 
element from the array, then partitioning the remaining elements into two subarrays: 
one with elements less than the pivot and one with elements greater than the pivot. 
The pivot is then placed in its correct position in the sorted array. This process is 
recursively applied to the subarrays until the entire array is sorted.

The performance of QuickSort depends on the choice of the pivot. In the average and 
best-case scenarios, when the pivot divides the array roughly in half each time, QuickSort
runs in **O(n log n)** time due to the logarithmic depth of the recursion and the linear time
spent partitioning each level. However, in the worst case—if the pivot is consistently 
chosen poorly (e.g., always the smallest or largest element in an already sorted array),
like in the example below — the time complexity degrades to **O(n²)** because the 
partitioning process only reduces the array size by one at each step. QuickSort is often 
faster than other O(n log n) sorts (like MergeSort) due to lower constant factors and 
efficient in-place sorting.

    Example:
    Initial array: [4, 3, 2, 1]

    Pick pivot = 1 → Partition into [] (less than 1) and [4, 3, 2] (greater than 1)
    Combine: [] + [1] + [4, 3, 2]
    Recursively sort [4, 3, 2]:
        Pick pivot = 2 → Partition into [] (less than 2) and [4, 3] (greater than 2)
        Combine: [] + [2] + [4, 3]
        Recursively sort [4, 3]:
            Pick pivot = 3. Partition into [] (less than 3) and [4] (greater than 3)
            Combine: [] + [3] + [4] → [3, 4].

    Final combination: [1] + [2] + [3, 4] → Sorted array: [1, 2, 3, 4].