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

---

# 👨‍💻 Author

**Jadhav Uday**

🎓 B.Tech – Computer Science & Engineering (AI & ML)
🏫 Marwadi University

GitHub:
https://github.com/jadhavuday08

---

# ⭐ Repository

You can find the complete collection of programs here:

**DAA-LAB**
https://github.com/jadhavuday08/DAA-LAB

If you find this repository useful, consider giving it a ⭐.

---

## 📌 Note

This repository is intended for **educational and academic purposes**. The programs may be modified and improved as additional DAA practicals and algorithms are completed.

---

## 📜 License

This project is intended primarily for educational use. You are welcome to study, modify, and use the code for learning purposes.




