# -*- coding: utf-8 -*-
"""algorithm2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GROFLfgzo9vgh-Nq5I2P_ERW_1VbHwW3
"""

import time

def fib_dynamic(n):
    if n == 0 or n == 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

for n in range(50, 101):
    start_time = time.time()
    fib_dynamic(n)
    elapsed_time = time.time() - start_time
    print(f"n={n}, time={elapsed_time:.6f}s")