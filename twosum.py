def twoSum(nums, target):
    # First pass: store number -> index
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    # Second pass: find complement
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]

    return []

# Taking user input
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements separated by space: ").split()))
target = int(input("Enter the target sum: "))

result = twoSum(nums, target)
print("Indices of the two numbers are:", result)