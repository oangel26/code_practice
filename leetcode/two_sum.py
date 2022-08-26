#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

(LeetCode - Two sum)
"""
class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i, v in enumerate(nums):
            if target - v in dict:
                return([dict[target-v], i])
            else:
                dict[v] = i

"""
    * Solution 49% optimal

    len_nums = len(nums)
    for i in range(0, len_nums - 1):
        for j in range(i + 1, len_nums):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return []

 --------------------------


    * Solution 51% optimal

    for i in range(len(nums)):
        try:
            j = nums.index(target - nums[i], i + 1)
            return [i, j]
        except:
    continue
"""

if __name__ == "__main__":
    nums1 = [3, 3]
    target1 = 6

    nums2 = [3,2,4]
    target2 = 6

    nums3 = [3,3]
    target3 = 6

    solution = Solution()
    print(solution.two_sum(nums1, target1))
    print(solution.two_sum(nums2, target2))
    print(solution.two_sum(nums3, target3))
