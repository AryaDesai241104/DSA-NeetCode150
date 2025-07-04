# My Solution
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # Time complexity: O(nlogn + mlogm)
        # Space complexity: O(n + m) depending on sorting algorithm


# Most Optimal Solution
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  # For lowercase English letters
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


def main():
    print("Anagram Checker")
    s = input("Enter the first string: ").lower()
    t = input("Enter the second string: ").lower()

    print("\nUsing sorted() method (Solution1):")
    sol1 = Solution1()
    print("Are the strings anagrams?", sol1.isAnagram(s, t))

    print("\nUsing frequency count method (Solution2):")
    sol2 = Solution2()
    print("Are the strings anagrams?", sol2.isAnagram(s, t))


if __name__ == "__main__":
    main()
# Time complexity: O(n+m)
# Space complexity: O(1) since we have at most 26 different characters.