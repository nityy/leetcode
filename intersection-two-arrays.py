def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    d1 = {}
    d2 = {}
    ans = []

    for v1 in nums1:
        d1[v1] = d1.get(v1, 0) + 1

    for v2 in nums2:
        d2[v2] = d2.get(v2, 0) + 1

    for k, v1 in d1.items():
        v2 = d2.get(k, 0)
        ans += [k] * min(v1, v2)

    return ans


# a = [int(item) for item in input("Enter the first list items : ").split()]
# b = [int(item) for item in input("Enter the second list items : ").split()]

a = [1, 2, 3, 4, 44, 5, 66, 55, 2]
b = [47, 55, 2, 2, 2, 66]
print(intersect(a, b))
