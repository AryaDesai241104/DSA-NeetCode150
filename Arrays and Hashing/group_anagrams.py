# My Solution
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = __dict__(list)

        for string in strs :
            count = [0]*26

            for character in string :
                count[ord(character) - ord('a')] += 1

            ans[tuple(count)].append(string)
        return list(ans.values())
# Time complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
# Space complexity: O(n * k) for the output list and the dictionary used to

        
        