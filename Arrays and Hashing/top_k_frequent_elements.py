from typing import List

# My Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        sorted_items = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

        result = [ans[0] for ans in sorted_items[:k]]
        return result

# Time complexity: O(n log n) — due to sorting the frequency dictionary
# Space complexity: O(n) — for the frequency dictionary and result list

def get_user_input():
    nums = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    k = int(input("Enter the value of k: "))
    return nums, k

# Accept input and run
nums, k = get_user_input()
sol = Solution()
result = sol.topKFrequent(nums, k)

print(f"\nTop {k} frequent elements: {result}")
