def is_valid_parentheses(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        # If closing bracket
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(ch)

    return len(stack) == 0


def main():
    s = input("Enter parentheses string: ").strip()
    print(is_valid_parentheses(s))


if __name__ == "__main__":
    main()
