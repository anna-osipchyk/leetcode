from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_in_list = {}
        for i, el in enumerate(nums):
            remaining = target - el
            if remaining in already_in_list:
                return [already_in_list[remaining], i]
            already_in_list[el] = i


# Runtime: 52 ms, faster than 97.52% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 55.62% of Python3 online submissions for Two Sum.
ret = Solution().twoSum([2, 1, 9, 4, 4, 56, 90, 3], 8)
print(ret)
