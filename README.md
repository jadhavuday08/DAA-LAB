# Sorting Algorithms in C++

This repository contains implementations of the most commonly used **sorting algorithms** in **C++**. Each program accepts user input, sorts the array, displays the sorted output, and measures the execution time using the C++ `<chrono>` library.

## 📌 Algorithms Included

* Bubble Sort
* Insertion Sort
* Selection Sort
* Merge Sort
* Quick Sort

## 📂 Project Structure

```
Sorting-Algorithms/
│── bubblesort.cpp
│── insertionsort.cpp
│── selectionsort.cpp
│── mergesort.cpp
│── quicksort.cpp
└── README.md
```

## 🚀 Features

* Written in C++
* User input for array elements
* Displays sorted array
* Measures execution time in microseconds
* Shows the Best, Average, and Worst case time complexity for each algorithm

## 📊 Time Complexity

| Algorithm      | Best Case  | Average Case | Worst Case |
| -------------- | ---------- | ------------ | ---------- |
| Bubble Sort    | O(n²)      | O(n²)        | O(n²)      |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      |

## 🛠️ Requirements

* C++ Compiler (GCC, G++, MinGW, or MSVC)
* C++11 or later

## ▶️ How to Run

### Compile

```bash
g++ bubblesort.cpp -o bubble
```

### Execute

```bash
./bubble
```

Repeat the same steps for the other `.cpp` files.

## 📖 Learning Objectives

This project helps in understanding:

* Comparison-based sorting algorithms
* Algorithm analysis
* Time complexity
* Performance measurement using `<chrono>`
* Basic C++ programming concepts

## 📌 Technologies Used

* C++
* Standard Template Library (STL)
* Chrono Library
 
 ## 📷 Sample Output

```
Enter number of elements:
5

Enter elements:
5 2 8 1 3

Sorted Array:
1 2 3 5 8

Execution Time: 12 microseconds
```
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




# 🔍 Algorithms and Programs

## 1. Factorial

The factorial program calculates the factorial of a given number using an algorithmic approach.

### Example

```text
Input:
5

Output:
Factorial = 120
```

### Complexity

| Method    | Time Complexity | Space Complexity |
| --------- | --------------: | ---------------: |
| Iterative |            O(n) |             O(1) |
| Recursive |            O(n) |             O(n) |

---

## 2. Coin Change

The **Coin Change** problem is implemented using **Dynamic Programming**.

The objective is to determine the minimum number of coins required to make a given amount using a set of available denominations.

### Example

```text
Coins: 1 2 5
Amount: 11

Output:
Minimum coins = 3
```

One possible solution is:

```text
5 + 5 + 1 = 11
```

### Complexity

| Complexity |         Value |
| ---------- | ------------: |
| Time       | O(n × amount) |
| Space      |     O(amount) |

---

## 3. Matrix Chain Multiplication

**Matrix Chain Multiplication** is a Dynamic Programming problem used to determine the most efficient order for multiplying a sequence of matrices.

The objective is to minimize the total number of scalar multiplications.

### Example

For matrices:

```text
A × B × C
```

Different parenthesizations can require different numbers of operations.

The algorithm determines the optimal multiplication order.

### Complexity

| Complexity | Value |
| ---------- | ----: |
| Time       | O(n³) |
| Space      | O(n²) |

---

## 4. Heap Sort

**Heap Sort** is a comparison-based sorting algorithm that uses a binary heap data structure.

This repository includes an implementation using a **Max Heap**.

### Features

* Builds a Max Heap
* Repeatedly extracts the maximum element
* Produces the sorted array
* Demonstrates heap-based sorting

### Complexity

| Case    | Time Complexity |
| ------- | --------------: |
| Best    |      O(n log n) |
| Average |      O(n log n) |
| Worst   |      O(n log n) |

### Space Complexity

```text
O(1)
```

Heap Sort is an **in-place sorting algorithm**.

---

# 🔃 Sorting Algorithms

The repository also contains implementations of commonly used sorting algorithms.

### Algorithms

| Algorithm      |  Best Case | Average Case | Worst Case |
| -------------- | ---------: | -----------: | ---------: |
| Bubble Sort    |       O(n) |        O(n²) |      O(n²) |
| Insertion Sort |       O(n) |        O(n²) |      O(n²) |
| Selection Sort |      O(n²) |        O(n²) |      O(n²) |
| Merge Sort     | O(n log n) |   O(n log n) | O(n log n) |
| Quick Sort     | O(n log n) |   O(n log n) |      O(n²) |
| Heap Sort      | O(n log n) |   O(n log n) | O(n log n) |

---

# 🔎 Searching Algorithms

Searching algorithms are used to locate an element in a data structure.

Common algorithms covered in DAA include:

### Linear Search

Searches each element sequentially.

```text
Best Case    : O(1)
Average Case : O(n)
Worst Case   : O(n)
Space        : O(1)
```

### Binary Search

Works on a sorted array and repeatedly divides the search space into two halves.

```text
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)
Space        : O(1)
```

---

# 🧠 Algorithm Design Techniques

The programs in this repository demonstrate several important algorithm design techniques.

### 1. Brute Force

Solves a problem by trying possible solutions directly.

### 2. Divide and Conquer

Divides a problem into smaller subproblems, solves them, and combines the results.

Examples:

* Merge Sort
* Quick Sort
* Binary Search

### 3. Dynamic Programming

Breaks a problem into overlapping subproblems and stores previously calculated results.

Examples:

* Coin Change
* Matrix Chain Multiplication

### 4. Greedy Method

Makes the locally optimal choice at each step with the goal of obtaining an overall optimal solution.

### 5. Backtracking

Builds a solution incrementally and goes back when a choice cannot lead to a valid solution.

---

# ⏱️ Time Complexity

Understanding time complexity is an important part of this repository.

Common complexity classes include:

```text
O(1)          Constant
O(log n)      Logarithmic
O(n)          Linear
O(n log n)    Linearithmic
O(n²)         Quadratic
O(n³)         Cubic
O(2ⁿ)         Exponential
O(n!)         Factorial
```

The programs are designed to help understand how algorithm performance changes as the input size increases.

---

# ⚡ Execution Time

Some programs can measure their execution time to compare algorithm performance.

For Python, execution time can be measured using:

```python
import time

start = time.perf_counter()

# Algorithm

end = time.perf_counter()

execution_time = end - start

print("Execution Time:", execution_time, "seconds")
```

For C++, the `<chrono>` library can be used for high-resolution timing.

---

# 🛠️ Technologies Used

* 🐍 **Python**
* 💻 **C++**
* ⏱️ Python `time` module
* ⏱️ C++ `<chrono>` library
* 🧠 Data Structures and Algorithms
* 📊 Algorithm Analysis

---

# ▶️ How to Run

## Python Programs

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

Run a program:

```bash
python Factorial.py
```

For example:

```bash
python coinchange.py
```

or:

```bash
python chainmatrix.py
```

---

## C++ Programs

Install a C++ compiler such as:

* GCC
* G++
* MinGW
* MSVC

Compile a program:

```bash
g++ filename.cpp -o program
```

Run it:

### Windows

```bash
program.exe
```

### Linux / macOS

```bash
./program
```

---

# 🎯 Learning Objectives

This repository is designed to help understand:

* Algorithm design
* Algorithm implementation
* Data structures
* Problem-solving techniques
* Time complexity
* Space complexity
* Dynamic Programming
* Divide and Conquer
* Searching algorithms
* Sorting algorithms
* Recursion
* Performance analysis
* Execution-time measurement

---

# 📈 Complexity Comparison

| Algorithm / Problem         | Technique             |    Time Complexity |
| --------------------------- | --------------------- | -----------------: |
| Linear Search               | Brute Force           |               O(n) |
| Binary Search               | Divide & Conquer      |           O(log n) |
| Bubble Sort                 | Comparison            |              O(n²) |
| Insertion Sort              | Incremental           |              O(n²) |
| Selection Sort              | Comparison            |              O(n²) |
| Merge Sort                  | Divide & Conquer      |         O(n log n) |
| Quick Sort                  | Divide & Conquer      | O(n log n) average |
| Heap Sort                   | Heap                  |         O(n log n) |
| Factorial                   | Iteration / Recursion |               O(n) |
| Coin Change                 | Dynamic Programming   |      O(n × amount) |
| Matrix Chain Multiplication | Dynamic Programming   |              O(n³) |

---

# 📖 Why This Repository?

The main purpose of this repository is to maintain a collection of **DAA laboratory programs and algorithm implementations** in one place.

It can be useful for:

* 📚 College practicals
* 📝 Lab examinations
* 🎓 DAA exam preparation
* 💻 Algorithm practice
* 🧠 Understanding time complexity
* 🚀 Improving problem-solving skills
* 🔬 Comparing algorithm performance

# 0/1 Knapsack Problem Using Dynamic Programming

## 📌 Description

This project implements the **0/1 Knapsack Problem using Dynamic Programming in Python**.

The 0/1 Knapsack problem is an optimization problem where we have a set of items, each with a specific **weight** and **value**. The goal is to select items such that the total weight does not exceed the knapsack's capacity while maximizing the total value.

In the **0/1 Knapsack**, each item can either be:

* ✅ Selected (1)
* ❌ Not selected (0)

An item cannot be selected more than once.

---

## 🧠 Algorithm

The program uses **Dynamic Programming (DP)** to solve the problem.

### Steps

1. Read the number of items.
2. Read the weight and value of each item.
3. Read the maximum capacity of the knapsack.
4. Create a DP table.
5. For every item and capacity:

   * If the item's weight is less than or equal to the current capacity, choose the maximum of:

     * Including the item.
     * Excluding the item.
   * Otherwise, exclude the item.
6. The final DP table value gives the maximum possible value.
7. Calculate and display the program's execution time.

---

## 💻 Technologies Used

* **Python 3**
* Dynamic Programming
* `time` module for measuring execution time

---

## 📂 Program Structure

```text
Knapsack/
│
├── knapsack.py
└── README.md
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Run the Program

Open the terminal in the project directory and run:

```bash
python knapsack.py
```

---

## 📝 Example Input

```text
0/1 Knapsack Problem using Dynamic Programming

Enter number of items: 4

Enter weight of item 1: 1
Enter value of item 1: 15

Enter weight of item 2: 3
Enter value of item 2: 20

Enter weight of item 3: 4
Enter value of item 3: 30

Enter weight of item 4: 5
Enter value of item 4: 40

Enter maximum capacity of knapsack: 7
```

## 📤 Example Output

```text
Maximum value that can be obtained: 55

Time Complexity Analysis:
Best Case    : O(n × W)
Average Case : O(n × W)
Worst Case   : O(n × W)

Space Complexity:
Space        : O(n × W)

Execution Time:
0.000012300 seconds
```

---

## ⏱️ Complexity Analysis

Let:

* `n` = Number of items
* `W` = Maximum capacity of the knapsack

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n × W)        |
| Average Case | O(n × W)        |
| Worst Case   | O(n × W)        |

### Space Complexity

The program uses a 2D DP table of size `(n + 1) × (W + 1)`.

```text
Space Complexity = O(n × W)
```

---

## ⏱️ Execution Time

The program uses Python's `time.perf_counter()` function to measure the execution time of the Knapsack algorithm.

```python
start_time = time.perf_counter()

max_value = knapsack(weights, values, capacity)

end_time = time.perf_counter()

execution_time = end_time - start_time
```

The execution time depends on the computer, number of items, and knapsack capacity.

---

## 🎯 Objective

The main objective of this practical is to:

* Understand the **0/1 Knapsack Problem**.
* Implement **Dynamic Programming**.
* Understand optimization using DP.
* Analyze **time and space complexity**.
* Measure the actual **execution time** of the algorithm.

---

## 🔍 Key Concept

The main recurrence relation used is:

```text
DP[i][w] = max(
    value[i-1] + DP[i-1][w-weight[i-1]],
    DP[i-1][w]
)
```

If the current item's weight is greater than the available capacity:

```text
DP[i][w] = DP[i-1][w]
```

---

## 📚 Learning Outcome

After completing this practical, you should be able to:

1. Explain the 0/1 Knapsack problem.
2. Implement a Dynamic Programming solution in Python.
3. Understand overlapping subproblems and optimal substructure.
4. Analyze algorithm complexity.
5. Measure program execution time.
   

# DFS and BFS Graph Traversal in Python

This project implements **Depth First Search (DFS)** and **Breadth First Search (BFS)** for traversing an undirected graph using Python.

The program also measures and displays the **execution time** of both DFS and BFS in nanoseconds.

## 📌 Features

* Create an undirected graph using an adjacency list.
* Add vertices and edges using user input.
* Perform **DFS traversal**.
* Perform **BFS traversal**.
* Measure DFS execution time.
* Measure BFS execution time.
* Display traversal results and execution times.

## 🛠️ Technologies Used

* **Python 3**
* `collections.deque` for BFS queue
* `time.perf_counter_ns()` for execution-time measurement

## 📂 Algorithm

### 1. Depth First Search (DFS)

DFS explores a graph by going as deep as possible along each branch before backtracking.

**Steps:**

1. Start from the given vertex.
2. Mark the vertex as visited.
3. Print the vertex.
4. Visit each unvisited adjacent vertex recursively.
5. Continue until all reachable vertices are visited.

### 2. Breadth First Search (BFS)

BFS explores the graph level by level using a queue.

**Steps:**

1. Start from the given vertex.
2. Mark the vertex as visited.
3. Insert it into a queue.
4. Remove a vertex from the queue.
5. Visit all its unvisited adjacent vertices.
6. Add the newly visited vertices to the queue.
7. Continue until the queue becomes empty.

## ⏱️ Time Complexity

For a graph represented using an adjacency list:

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
| --------- | --------- | ------------ | ---------- | ---------------- |
| DFS       | O(V + E)  | O(V + E)     | O(V + E)   | O(V)             |
| BFS       | O(V + E)  | O(V + E)     | O(V + E)   | O(V)             |

Where:

* **V** = Number of vertices
* **E** = Number of edges

## 💻 How to Run

Make sure Python 3 is installed.

Run the program using:

```bash
python dfs_bfs.py
```

## 📥 Input

The program asks for:

1. Number of vertices
2. Number of edges
3. Edges connecting the vertices
4. Starting vertex

### Example Input

```text
Enter number of vertices: 6
Enter number of edges: 7
Enter edges (u v):
0 1
0 2
1 3
1 4
2 4
3 5
4 5
Enter starting vertex: 0
```

## 📤 Output

Example output:

```text
DFS Traversal: 0 1 3 5 4 2

BFS Traversal: 0 1 2 3 4 5

Execution Time:
DFS: 8500 ns
BFS: 6200 ns
```

> Execution time will vary depending on the computer, Python version, graph size, and system load.

## 📊 DFS vs BFS

| Feature          | DFS                                    | BFS                                |
| ---------------- | -------------------------------------- | ---------------------------------- |
| Data Structure   | Stack / Recursion                      | Queue                              |
| Traversal        | Depth-wise                             | Level-wise                         |
| Implementation   | Recursive in this program              | `deque`                            |
| Time Complexity  | O(V + E)                               | O(V + E)                           |
| Space Complexity | O(V)                                   | O(V)                               |
| Useful For       | Path exploration, connected components | Shortest path in unweighted graphs |

## 📁 Project Structure

```text
DFS-BFS/
│
├── dfs_bfs.py
└── README.md
```

## 🎯 Applications

### DFS Applications

* Finding connected components
* Detecting cycles
* Maze solving
* Topological sorting
* Path finding

### BFS Applications

* Finding the shortest path in an unweighted graph
* Level-order traversal
* Social-network connections
* Web crawling
* Network broadcasting

## 📝 Conclusion

This project demonstrates the implementation of two fundamental graph traversal algorithms: **DFS and BFS**. Both algorithms have a time complexity of **O(V + E)** when an adjacency list is used. DFS explores vertices deeply using recursion, while BFS explores vertices level by level using a queue.

The program also demonstrates how to measure the actual execution time of algorithms using Python's `time.perf_counter_ns()` function.

## 📚 References

* Python Documentation — `time` module: https://docs.python.org/3/library/time.html
* Python Documentation — `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque
* CP-Algorithms — Breadth First Search: https://cp-algorithms.com/graph/breadth-first-search.html
* CP-Algorithms — Depth First Search: https://cp-algorithms.com/graph/depth-first-search.html

# Prim's Algorithm in Python

## 📌 Introduction

This project implements **Prim's Algorithm** in Python to find the **Minimum Spanning Tree (MST)** of a connected, weighted, undirected graph.

The program takes the graph as an **adjacency matrix** from the user and displays the edges selected for the Minimum Spanning Tree along with the total cost.

## 🎯 Objective

To implement **Prim's Algorithm** for finding the Minimum Spanning Tree of a weighted undirected graph.

## 🛠️ Technologies Used

* Python 3
* Adjacency Matrix
* Prim's Algorithm

## 🔍 What is Prim's Algorithm?

Prim's Algorithm is a **greedy algorithm** used to find a Minimum Spanning Tree of a weighted, connected, undirected graph.

It starts from a selected vertex and repeatedly chooses the **minimum-weight edge** that connects a selected vertex to an unselected vertex.

### Basic Steps

1. Start with any vertex.
2. Mark the vertex as selected.
3. Find the minimum-weight edge connecting a selected vertex to an unselected vertex.
4. Add that edge to the Minimum Spanning Tree.
5. Mark the newly connected vertex as selected.
6. Repeat until all vertices are selected.
7. Display the selected edges and total MST cost.

## 💻 Python Code

```python
def prim(graph, vertices):
    selected = [False] * vertices
    selected[0] = True

    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    for _ in range(vertices - 1):
        minimum = float('inf')
        x = 0
        y = 0

        # Find the minimum weight edge
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        selected[y] = True
        total_cost += minimum

        print(f"{x} -- {y}  Weight = {minimum}")

    print("\nMinimum Spanning Tree Cost:", total_cost)


# Main Program
vertices = int(input("Enter number of vertices: "))

graph = []

print("\nEnter the adjacency matrix:")
print("Enter 0 if there is no edge.")

for i in range(vertices):
    row = list(map(int, input(f"Row {i}: ").split()))
    graph.append(row)

prim(graph, vertices)
```

## 📥 Sample Input

```text
Enter number of vertices: 5

Enter the adjacency matrix:
Enter 0 if there is no edge.
Row 0: 0 2 0 6 0
Row 1: 2 0 3 8 5
Row 2: 0 3 0 0 7
Row 3: 6 8 0 0 9
Row 4: 0 5 7 9 0
```

## 📤 Sample Output

```text
Edges in Minimum Spanning Tree:
0 -- 1  Weight = 2
1 -- 2  Weight = 3
1 -- 4  Weight = 5
0 -- 3  Weight = 6

Minimum Spanning Tree Cost: 16
```

## 📊 Example Graph

The above input represents the following weighted graph:

```text
       2
  0 -------- 1
  |          |\
 6|         3| \5
  |          |  \
  3          2   4
   \          |  /
    \         |7
     \        |/
       ------- 
```

## 📁 Project Structure

```text
Prim-Algorithm/
│
├── prim.py
└── README.md
```

## ▶️ How to Run

Make sure **Python 3** is installed on your computer.

Run the program using:

```bash
python prim.py
```

Then enter the number of vertices and the adjacency matrix when prompted.

## 🌟 Applications

Prim's Algorithm can be used in:

* Computer network design
* Road network planning
* Electrical grid design
* Telecommunication networks
* Minimum-cost connection problems
* Network infrastructure planning

## 📝 Conclusion

Prim's Algorithm provides an efficient greedy approach for constructing a **Minimum Spanning Tree**. The program demonstrates how to select the minimum-weight edges while ensuring that all vertices become connected without forming cycles.

## 📚 References

* [CP-Algorithms — Minimum Spanning Tree (Prim's Algorithm)](https://cp-algorithms.com/graph/mst_prim.html?utm_source=chatgpt.com)
* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)


# Kruskal's Algorithm in Python

## 📌 Introduction

This project implements **Kruskal's Algorithm** in Python to find the **Minimum Spanning Tree (MST)** of a connected, weighted, undirected graph.

The program takes the vertices and weighted edges as input, sorts the edges by weight, and selects the minimum-weight edges while avoiding cycles.

## 🎯 Objective

To implement **Kruskal's Algorithm** for finding the Minimum Spanning Tree of a weighted undirected graph.

## 🛠️ Technologies Used

* Python 3
* Kruskal's Algorithm
* Union-Find / Disjoint Set data structure

## 🔍 What is Kruskal's Algorithm?

Kruskal's Algorithm is a **greedy algorithm** used to find the Minimum Spanning Tree of a weighted, connected, undirected graph.

The algorithm selects edges in increasing order of their weights and adds an edge to the MST only if it does not create a cycle.

## ⚙️ Algorithm Steps

1. Start with an empty Minimum Spanning Tree.
2. Sort all edges in increasing order of their weights.
3. Select the edge with the smallest weight.
4. Check whether adding the edge creates a cycle.
5. If it does not create a cycle, add the edge to the MST.
6. If it creates a cycle, discard the edge.
7. Repeat until `V - 1` edges are selected.
8. Display the selected edges and total cost.

## 💻 Python Code

```python
# Kruskal's Algorithm in Python

# Find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])


# Join two sets
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(vertices, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total_cost = 0

    # Select edges
    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # Add edge if it does not create a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, u, v)

            # MST contains V-1 edges
            if len(mst) == vertices - 1:
                break

    print("\nEdges in Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(f"{u} -- {v}  Weight = {weight}")

    print("\nMinimum Spanning Tree Cost:", total_cost)


# Main Program
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("\nEnter edges (u v weight):")

for i in range(edges_count):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

kruskal(vertices, edges)
```

## 📥 Sample Input

```text
Enter number of vertices: 5
Enter number of edges: 7

Enter edges (u v weight):
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9
```

## 📤 Sample Output

```text
Edges in Minimum Spanning Tree:
0 -- 1  Weight = 2
1 -- 2  Weight = 3
1 -- 4  Weight = 5
0 -- 3  Weight = 6

Minimum Spanning Tree Cost: 16
```

## 🧠 Union-Find

The program uses the **Union-Find (Disjoint Set Union)** technique to determine whether adding an edge will create a cycle.

### Find

The `find()` function determines the representative or root of a vertex.

```python
def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])
```

### Union

The `union()` function joins two different sets.

```python
def union(parent, rank, u, v):
    ...
```

This allows Kruskal's Algorithm to avoid adding edges that would create cycles.

## 📁 Project Structure

```text
Kruskal-Algorithm/
│
├── kruskal.py
└── README.md
```

## ▶️ How to Run

Make sure **Python 3** is installed.

Run the program using:

```bash
python kruskal.py
```

Then enter the number of vertices, number of edges, and the weighted edges.

## 🌟 Applications

Kruskal's Algorithm can be used in:

* Computer network design
* Road network planning
* Electrical grid design
* Telecommunication networks
* Network infrastructure planning
* Minimum-cost connection problems

## 📝 Conclusion

Kruskal's Algorithm is a greedy approach for finding the **Minimum Spanning Tree** of a weighted undirected graph. By sorting the edges according to their weights and using the Union-Find technique to avoid cycles, the algorithm efficiently constructs an MST with the minimum possible total edge weight.

## 📚 References

* [CP-Algorithms — Kruskal's Algorithm](https://cp-algorithms.com/graph/mst_kruskal.html?utm_source=chatgpt.com)
* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)


## 👨‍💻 Author

**Uday Jadhav**








