def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    return []
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements separated by space: ").split()))
target = int(input("Enter the target sum: "))
result = twoSum(nums, target)
print("Indices of the two numbers are:", result)