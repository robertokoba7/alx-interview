import math

def minOPerations(n):
    """
    Given:
        number: n
        Returns: minimum number of operations
                Otherwise 0, if impossible to generate n H char
    """
    # Initialize the dynamic programming array with a high value for all elems
    lst = [math.inf] * (n+1)

    # Base case:it takes 0 operations to generate 1 H character
    lst[1] = 0

    # Iterate over every possible values of num1, from 2 to n
    for num1 in range(2, n+1):
        # iterate over all possible value of num2, from 1 to (num2-1)
        for num2 in range(1, num2):
            # Check if num2 can generate a sequence of H char
            if num1 % num2 == 0:
                # Calc the number of operations required to generate num2 H char that can be pasted to generate num1 H characters)
                lst[num1] = min(lst[num1], lst[num2] + (num1 // num2))

    # if impossible to generate n H char return 0
    if lst[n] == math.inf:
        return 0
    # Otherwise, return mininumber of operations
    return lst[n]







import math

def minOperations(n: int) -> int:
    dp = [math.inf] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return 0 if dp[n] == math.inf else dp[n]
