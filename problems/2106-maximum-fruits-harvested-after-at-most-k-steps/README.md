# 2106. Maximum Fruits Harvested After at Most K Steps

**Difficulty:** Hard
**Topics:** Array, Sliding Window

## Problem

[LeetCode Link](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/)

Given a 0-indexed 2D array `fruits` where `fruits[i] = [position_i, amount_i]` (sorted by position), a `startPos`, and an integer `k`, return the maximum total fruits you can harvest by walking at most `k` steps.

## Approach

Key insight: it only makes sense to change direction at most once. If you go `x` steps left and `y` steps right, total steps are `min(2x + y, 2y + x)`. Use a sliding window over fruit indices — for each left boundary, expand right as far as reachable within `k` steps. Since both pointers only move forward, this is O(n).

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Key Learnings

Iterate over fruit array indices (not positions) for O(1) access. The `lessThanKSteps` helper encodes the turn-once cost formula for three cases: all right, all left, or both directions.
