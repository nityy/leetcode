def firstUniqChar(s: str) -> int:
    ct = dict()
    for i, v in enumerate(s):
        if v in ct:
            ct[v] += 1
        else:
            ct[v] = 1
    for i, v in enumerate(s):
        if ct[v] == 1:
            return i
    return -1


s = "abracadabra"
print(firstUniqChar(s))
