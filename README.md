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

## 👨‍💻 Author

**Jadhav Uday**

B.Tech – Computer Science & Engineering (AI & ML)

Marwadi University


