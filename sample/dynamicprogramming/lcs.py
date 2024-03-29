# Longest Common Subsequence(최장 공통 부분수열)

# 비교 - Longest Common Substring(최장 공통 문자열) ex) 5582


# Dynamic Programming implementation of LCS problem
def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # declaring the array for string dp values
    L = [ [None]*(n+1) for i in range(m+1) ]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"

print( lcs(X, Y) ) # 4