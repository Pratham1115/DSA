class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # First reversal
        l = list(str(num))
        num2 = l[::-1]

        # Remove leading zeros after first reversal
        while len(num2) > 1 and num2[0] == "0":
            num2.pop(0)

        # Second reversal
        num3 = num2[::-1]

        # Convert back to integer and compare
        return int("".join(num3)) == num