# My Solution
class Solution:
    
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

# Time complexity:
#   encode: O(n) where n is the total number of characters in all strings
#   decode: O(n) where n is the length of the encoded string
# Space complexity:
#   encode: O(n) for the result string
#   decode: O(n) for the list of decoded strings

def get_user_input():
    strs = input("Enter strings separated by spaces: ").split()
    return strs

# Run
sol = Solution()
original = get_user_input()
encoded = sol.encode(original)
decoded = sol.decode(encoded)

print(f"\nEncoded string: {encoded}")
print(f"Decoded list: {decoded}")
