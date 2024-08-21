def find_longest_common_substring(strings):
    n = len(strings)
    longest_substring = ""

    def is_substring_in_both(s, t):
        return s in t or s in t[::-1]

    for i in range(n):
        current_string = strings[i]
        length = len(current_string)

        for start in range(length):
            for end in range(start + 1, length + 1):
                substring = current_string[start:end]
                
                if len(substring) > len(longest_substring) and all(is_substring_in_both(substring, strings[j]) for j in range(n) if j != i):
                    longest_substring = substring

    return longest_substring

n = int(input())
strings = [input().strip() for _ in range(n)]

result = find_longest_common_substring(strings)

print(result)
