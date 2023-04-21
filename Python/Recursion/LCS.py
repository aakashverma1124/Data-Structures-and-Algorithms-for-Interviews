def solve(s1, s2, m, n, dp):

    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]

    if dp[m][n] != -1:
        return dp[m][n]

    if s1[m - 1] == s2[n - 1]:
        dp[m][n] = 1 + solve(s1, s2, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(solve(s1, s2, m, n - 1, dp), solve(s1, s2, m - 1, n, dp))
    return dp[m][n]

def lcs(s1, s2):
    dp = [[-1 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    return solve(s1, s2, len(s1), len(s2), dp)

if __name__ == "__main__":
    s1 = "abc"
    s2 = "bca"
    print(lcs(s1, s2))