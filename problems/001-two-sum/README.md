# 1. Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Table

## Problem

[LeetCode Link](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach

Use a hash map to store each number's index as we iterate. For each number, check if `target - num` exists in the map. Single pass through the array.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Key Learnings

Classic hash map pattern. Trade space for time by storing complements.
