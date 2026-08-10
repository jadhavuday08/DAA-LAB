# Searching Algorithms in Python

This project contains two Python programs that demonstrate Linear Search and Binary Search. Both programs accept input from the user, search for a given element, display the result, and measure the search execution time in microseconds.

--------------------------------------------------
FILES INCLUDED
--------------------------------------------------

1. linearsearch.py
   - Implements Linear Search.
   - Searches elements sequentially.
   - Works on both sorted and unsorted data.

2. Binarysearch.py
   - Implements Binary Search.
   - Sorts the array before searching.
   - Faster than Linear Search for large datasets.

--------------------------------------------------
LINEAR SEARCH
--------------------------------------------------

Description:
Linear Search checks each element one by one until the target element is found or the end of the list is reached.

Algorithm:
1. Start from the first element.
2. Compare each element with the search key.
3. If found, return its position.
4. Otherwise continue searching.
5. If the end is reached, return "not found".

Time Complexity:
- Best Case    : O(1)
- Average Case : O(n)
- Worst Case   : O(n)

Advantages:
- Simple to implement.
- Works with unsorted data.

Disadvantages:
- Slow for large datasets.

Run Command:
python linearsearch.py

Example:

Enter number of elements: 5
Enter elements:
10 20 30 40 50
Enter element to search: 30

Search Result:
Element found at position: 3

--------------------------------------------------
BINARY SEARCH
--------------------------------------------------

Description:
Binary Search repeatedly divides the search space into two halves until the target element is found.

Note:
The array must be sorted before Binary Search is applied.

Algorithm:
1. Find the middle element.
2. Compare it with the search key.
3. If equal, return the position.
4. If the key is smaller, search the left half.
5. If the key is larger, search the right half.
6. Repeat until found or the search space becomes empty.

Time Complexity:
- Best Case    : O(1)
- Average Case : O(log n)
- Worst Case   : O(log n)

Space Complexity:
- O(1)

Advantages:
- Very fast for large sorted datasets.
- Efficient searching algorithm.

Disadvantages:
- Requires sorted data.

Run Command:
python Binarysearch.py

Example:

Enter number of elements: 5
Enter elements:
50 10 40 20 30

Sorted Array:
10 20 30 40 50

Enter element to search: 40

Search Result:
Element found at position: 4

--------------------------------------------------
COMPARISON
--------------------------------------------------

Feature              Linear Search     Binary Search
--------------------------------------------------
Data Required        Unsorted/Sorted   Sorted Only
Best Case            O(1)              O(1)
Average Case         O(n)              O(log n)
Worst Case           O(n)              O(log n)
Method               Sequential        Divide & Conquer
Efficiency           Lower             Higher

--------------------------------------------------
REQUIREMENTS
--------------------------------------------------

- Python 3.x
- Built-in time module

--------------------------------------------------
LEARNING OUTCOMES
--------------------------------------------------

After completing this project, you will be able to:

1. Understand Linear Search.
2. Understand Binary Search.
3. Compare O(n) and O(log n) algorithms.
4. Take user input in Python.
5. Measure execution time using time.perf_counter().
6. Analyze algorithm efficiency.

--------------------------------------------------
CONCLUSION
--------------------------------------------------

Linear Search is simple and suitable for small or unsorted datasets. Binary Search is much faster for large datasets but requires sorted data. Understanding both algorithms helps in choosing the most efficient searching technique for different situations.
