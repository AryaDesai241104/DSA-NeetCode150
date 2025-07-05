#My solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Time complexity: O(n)
# Space complexity: O(n)

def get_user_input():
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    return nums, target

# Accept input
nums, target = get_user_input()

# Create an instance and call the method
sol = Solution()
result = sol.twoSum(nums, target)

print(f"Indices of numbers that add up to {target}: {result}")