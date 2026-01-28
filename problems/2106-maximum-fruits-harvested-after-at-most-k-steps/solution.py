"""
LeetCode 2106: Maximum Fruits Harvested After at Most K Steps
Difficulty: Hard
Topics: Array, Sliding Window
Link: https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        lowerBound = 0
        upperBound = 0
        curFruitCount = 0
        maxFruitCount = 0
        while lowerBound < len(fruits):
            pos, fruitNum = fruits[lowerBound]
            if lowerBound > 0:
                curFruitCount -= fruits[lowerBound - 1][1]

            while upperBound < len(fruits) and self.lessThanKSteps(
                fruits[lowerBound][0], fruits[upperBound][0], k, startPos
            ):
                curFruitCount += fruits[upperBound][1]
                upperBound += 1
            maxFruitCount = max(maxFruitCount, curFruitCount)
            lowerBound += 1
        return maxFruitCount

    def lessThanKSteps(self, left, right, k, cur):
        if left >= cur:
            return (right - cur) <= k
        if right <= cur:
            return (cur - left) <= k
        else:
            return (
                min((cur - left) * 2 + (right - cur), (right - cur) * 2 + (cur - left))
                <= k
            )
