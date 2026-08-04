class Solution(object):
    def twoSum(self, nums, target):
        # Store each number with its original index
        nums_index = [(num, i) for i, num in enumerate(nums)]

        # Sort based on the numbers
        nums_index.sort()

        # Two pointers
        left = 0
        right = len(nums_index) - 1

        while left < right:
            total = nums_index[left][0] + nums_index[right][0]

            if total == target:
                return [nums_index[left][1], nums_index[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1