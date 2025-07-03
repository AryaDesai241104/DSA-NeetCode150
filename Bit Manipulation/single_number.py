# my soltuion
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans^num
        return ans
# Time complexity: O(n)
# Space complexity: O(1)

