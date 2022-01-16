from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    l = len(nums)
    d = {}
    for i in range(l):
        comp = target-nums[i]
        if comp in d:
            return [i, d[comp]]
        d[nums[i]] = i

        # Slower
        # l = len(nums)
        # for i, ni in enumerate(nums):
        #     for j in range(i+1, l):
        #         if (ni + nums[j] == target):
        #             return [i, j]
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
