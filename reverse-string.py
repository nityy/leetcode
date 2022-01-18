from typing import List


def reverseString(s: List[str]) -> None:
    i = 0
    j = len(s) - 1

    while j > i:
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
        i += 1
        j -= 1

    print(s)


s = ["H", "a", "n", "n", "a", "h"]
reverseString(s)
