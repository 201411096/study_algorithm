# Longest Increasing Subsequence(최장 증가 부분 수열)
# O(n^2)

import sys

stdInput = sys.stdin.readline

def main():
    array = list(map(int, stdInput().strip().split()))

    dp = [1 for i in range(len(array))]

    for i in range(1, len(dp)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

if __name__ == "__main__":
    main()