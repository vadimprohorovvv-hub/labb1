def permutations(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        current_char = s[i]
        remaining = s[:i] + s[i + 1:]
        for perm in permutations(remaining):
            result.append(current_char + perm)

    return result
if __name__ == "__main__":
    print(permutations("abc"))