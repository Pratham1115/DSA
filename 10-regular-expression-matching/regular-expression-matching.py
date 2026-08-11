class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True

        m, n = len(s), len(p)

        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(1, n):
            if p[j] == "*" and dp[0][j - 1]:
                dp[0][j + 1] = True

        for i in range(m):
            for j in range(n):

                # Normal character or '.'
                if p[j] == "." or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]

                # '*'
                elif p[j] == "*":

                    # Zero occurrence
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]

                    # One or more occurrences
                    else:
                        dp[i + 1][j + 1] = (
                            dp[i + 1][j] or      # multiple occurrences
                            dp[i][j + 1] or      # consume one character
                            dp[i + 1][j - 1]     # zero occurrences
                        )

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("", ".*"))