class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(n):
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10
            return rev

        return reverse(reverse(num)) == num