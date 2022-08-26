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
        num_list = []
        swich = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if (nums[i] + nums[j]) == target:
                    swich = 1
                    num_list.append(i)
                    num_list.append(j)
                    break
            if swich == 1:
                break
        return num_list


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
