def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    h = len(haystack)
    if n == 0:
        return 0
    elif n > h:
        return -1
    else:
        for i in range(h-n+1):
            if haystack[i] == needle[0]:
                for j in range(n):
                    if needle[j] == haystack[i+j]:
                        if j == n-1:
                            return i
                    else:
                        break
    return -1


haystack = "mississippi"
needle = "issipi"
print(strStr(haystack, needle))
