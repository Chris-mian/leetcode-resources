"""
LeetCode 2411: Smallest Subarrays With Maximum Bitwise OR
Difficulty: Medium
Topics: Array, Bit Manipulation, Two Pointers
Link: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

Time Complexity: O(n * 32) ~ O(n)
Space Complexity: O(n * 32) ~ O(n)
"""

from collections import defaultdict
from copy import deepcopy


class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        countAtIndex = defaultdict(int)
        numsInBits = []

        for num in nums:
            reversedBits = self.getBits(num)
            numsInBits.append(reversedBits)
            for i in range(len(reversedBits)):
                countAtIndex[i] += reversedBits[i]
        maxCountAtIndex = deepcopy(countAtIndex)

        def canBeRemoved(x, d):
            bits = numsInBits[x]
            for i in range(len(bits)):
                if bits[i] == 1 and d[i] < 2:
                    return False
            return True

        def achievedMax(dynamicD, maxD):
            for i in range(len(maxD)):
                if maxD[i] > 0 and dynamicD[i] == 0:
                    return False
            return True

        def remove(x, d):
            bits = numsInBits[x]
            for i in range(len(bits)):
                d[i] -= bits[i]

        def add(x, d):
            bits = numsInBits[x]
            for i in range(len(bits)):
                d[i] += bits[i]

        right = len(nums) - 1
        ans = []
        for left in range(len(nums)):
            if left == 0:
                while right > left:
                    if canBeRemoved(right, countAtIndex):
                        remove(right, countAtIndex)
                        right -= 1
                    else:
                        break
                ans.append(right - left + 1)
            else:
                while right < left:
                    right += 1
                    add(right, countAtIndex)
                while right >= left and not achievedMax(countAtIndex, maxCountAtIndex):
                    right += 1
                    add(right, countAtIndex)
                ans.append(right - left + 1)
            remove(left, maxCountAtIndex)
            remove(left, countAtIndex)
        return ans

    def getBits(self, num: int) -> list[int]:
        ans = []
        if num == 0:
            return [0]
        while num > 0:
            ans.append(num % 2)
            num = num // 2
        return ans
