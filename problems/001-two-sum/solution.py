"""
LeetCode 1: Two Sum
Difficulty: Easy
Topics: Array, Hash Table
Link: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
