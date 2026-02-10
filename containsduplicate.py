def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements separated by space: ").split()))

if containsDuplicate(nums):
    print("Duplicate exists in the array.")
else:
    print("No duplicates found in the array.")