def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print(product_except_self(nums))


if __name__ == "__main__":
    main()
