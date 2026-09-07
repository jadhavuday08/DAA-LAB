import time

# Iterative Method
def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


# Recursive Method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Input from user
n = int(input("Enter a non-negative number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # ---------------- ITERATIVE METHOD ----------------
    start_time = time.perf_counter()

    result_iterative = factorial_iterative(n)

    end_time = time.perf_counter()
    execution_time_iterative = end_time - start_time

    print("\n--- Iterative Method ---")
    print("Factorial =", result_iterative)
    print("Execution Time =", execution_time_iterative, "seconds")

    print("\nTime Complexity:")
    print("Best Case    : O(n)")
    print("Average Case : O(n)")
    print("Worst Case   : O(n)")
    print("Space Complexity: O(1)")


    # ---------------- RECURSIVE METHOD ----------------
    start_time = time.perf_counter()

    result_recursive = factorial_recursive(n)

    end_time = time.perf_counter()
    execution_time_recursive = end_time - start_time

    print("\n--- Recursive Method ---")
    print("Factorial =", result_recursive)
    print("Execution Time =", execution_time_recursive, "seconds")

    print("\nTime Complexity:")
    print("Best Case    : O(n)")
    print("Average Case : O(n)")
    print("Worst Case   : O(n)")
    print("Space Complexity: O(n)")