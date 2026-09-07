import time

def coin_change(coins, amount):
    # DP array
    dp = [float('inf')] * (amount + 1)

    # Base case
    dp[0] = 0

    # Fill the DP array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# User Input
coins = list(map(int, input("Enter coin values separated by spaces: ").split()))
amount = int(input("Enter the amount: "))

# Execution time
start_time = time.perf_counter()

result = coin_change(coins, amount)

end_time = time.perf_counter()


# Output
if result == -1:
    print("\nIt is not possible to make the amount using the given coins.")
else:
    print("\nMinimum number of coins required:", result)

print("\nTime Complexity: O(amount × number of coins)")
print("Space Complexity: O(amount)")
print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")
