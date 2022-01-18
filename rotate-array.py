from typing import List


def rotate1(nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:]+nums[:-k]
    print(nums)
    # space : O(n), time : O(n)


def rotate2(nums: List[int], k: int) -> None:
    l = len(nums)
    new = [None] * l
    for i, v in enumerate(nums):
        j = (i+k) % l
        new[j] = v
    nums[:] = new
    print(nums)
    # space : O(n), time : O(n)


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate1(arr, k)
arr = [1, 2, 3, 4, 5, 6, 7]
rotate2(arr, k)
