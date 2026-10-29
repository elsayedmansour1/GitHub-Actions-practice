def removeDuplicateLetters(s: str):
    Str = ""

    for it in range(len(s)):
        if s[it] in Str:
            continue

        for rev_char in Str[::-1]:
            if s[it] < rev_char and rev_char in s[it + 1:]:
                Str = Str[:-1]
            else:
                break

        Str = Str + s[it]

    return Str

# s = "bcabc"
s = "cbacdcbc"
print(removeDuplicateLetters(s))