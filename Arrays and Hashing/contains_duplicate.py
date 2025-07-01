class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def main():
    # Taking input from user as a string and converting it to a list of integers
    input_str = input("Enter numbers separated by spaces: ")
    nums = list(map(int, input_str.split()))

    # Create object of Solution and call hasDuplicate
    solution = Solution()
    result = solution.hasDuplicate(nums)

    # Print the result
    if result:
        print("Duplicates found!")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()

