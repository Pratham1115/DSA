class Solution:
    def combinationSum(self, candidates, target):
        # Sort candidates to avoid duplicate combinations
        candidates.sort()

        # dp[i] stores all combinations that sum to i
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # One way to make sum 0: []

        for i in range(1, target + 1):
            for num in candidates:
                if num > i:
                    break

                # Get all combinations that make (i - num)
                for comb in dp[i - num]:
                    # Skip duplicates by maintaining non-decreasing order
                    if comb and comb[-1] > num:
                        continue

                    # Add current number to the combination
                    dp[i].append(comb + [num])

        return dp[target]


# Driver code
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([8, 7, 4, 3], 11))