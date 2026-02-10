def max_subarray(nums):
    maxSum = float('-inf')
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum
def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print(max_subarray(nums))
if __name__ == "__main__":
    main()
