from typing import List

# space : O(n), time : O(n)


def rotate(nums: List[int], k: int) -> None:
    l = len(nums)
    new = [None] * l
    for i, v in enumerate(nums):
        j = (i+k) % l
        new[j] = v
    nums = [v for v in new]
    print(nums)


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(arr, k)
