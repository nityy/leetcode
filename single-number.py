from typing import List


def singleNumber(nums: List[int]) -> int:
    ct = {}
    for v in nums:
        ct[v] = ct.get(v, 0) + 1
        if ct[v] == 2:
            del ct[v]
    return list(ct)[0]


print(singleNumber([2, 2, 1, 1, 3, 4, 4, 5, 6, 55, 55, 6, 5]))
