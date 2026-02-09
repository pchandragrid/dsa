def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1

    return True


def main():
    s = input("Enter first string: ").strip()
    t = input("Enter second string: ").strip()

    if (is_anagram(s, t)):
        print("✅ The strings are anagrams.")
    else:
        print("❌ The strings are NOT anagrams.")


if __name__ == "__main__":
    main()
