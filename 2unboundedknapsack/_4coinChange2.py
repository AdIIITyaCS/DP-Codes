def coinChange(wt, W, n):
  # Use a clear variable for your "impossible" value
  impossible_val = float('inf') - 1
  
  t = [[impossible_val for _ in range(W + 1)] for _ in range(n + 1)]

  # Base case: 0 coins needed to make sum 0
  for i in range(n + 1):
    t[i][0] = 0

  # Initialize the first row (using only the first coin)
  for j in range(1, W + 1):
    if j % wt[0] == 0:
      t[1][j] = j // wt[0]
    # No need for 'else', it's already set to impossible_val

  # Fill the rest of the DP table
  for i in range(2, n + 1):
    for j in range(1, W + 1):
      if wt[i - 1] <= j:
        # min( (1 + use_current_coin), (dont_use_current_coin) )
        t[i][j] = min(1 + t[i][j - wt[i - 1]], t[i - 1][j])
      else:
        # Can't use the coin, so copy the value from the row above
        t[i][j] = t[i - 1][j]
  
  # Print the table to debug (optional)


  # Check against the correct "impossible" value
  return t[n][W] if t[n][W] != impossible_val else -1

# --- Your Test Cases ---

# Test Case 1
coin = [1, 2, 3]
n = len(coin)
s = 5
print(f"Min coins for sum {s} with {coin}: {coinChange(coin, s, n)}")

# Test Case 2 (The one you were running)
c1 = [2, 5, 7, 12, 15, 16]
n1 = len(c1)
s1 = 1
print(f"Min coins for sum {s1} with {c1}: {coinChange(c1, s1, n1)}")