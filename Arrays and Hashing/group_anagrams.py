from collections import defaultdict

# My Solution
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for character in string:
                count[ord(character) - ord('a')] += 1

            ans[tuple(count)].append(string)
        
        return list(ans.values())

# Time complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
# Space complexity: O(n * k) for the output list and the dictionary used to

def get_user_input():
    print("Enter strings separated by spaces (e.g., eat tea tan ate nat bat):")
    strs = input().split()
    return strs

# Accept input and run
strs = get_user_input()
sol = Solution()
result = sol.groupAnagrams(strs)

print("\nGrouped Anagrams:")
for group in result:
    print(group)
