# 2411. Smallest Subarrays With Maximum Bitwise OR

**Difficulty:** Medium
**Topics:** Array, Bit Manipulation, Two Pointers

## Problem

[LeetCode Link](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/)

For each index `i`, find the length of the smallest subarray starting at `i` whose bitwise OR equals the maximum possible OR of any subarray starting at `i`.

## Approach

Track per-bit contribution counts across the current window using a frequency map of each bit position. Use two pointers: for each `left`, expand or shrink `right` to find the smallest window where every bit present in the global max OR is still represented.

The first iteration starts from the full array and shrinks right inward. Subsequent iterations remove the left element from both the dynamic and max count maps, then expand right if the window no longer achieves the max OR.

## Complexity

- **Time:** O(n * 32) ~ O(n)
- **Space:** O(n * 32) ~ O(n)

## Key Learnings

- **Optimization**: Instead of pre-converting to bit arrays, track the *last index* where each bit position has a 1. For each `left`, the answer is `max(last[bit] - left + 1)` over all 32 bits. This eliminates the need for add/remove helpers and reduces the approach to a clean right-to-left sweep in O(n * 32).
- **Bit trick**: Use `(x >> i) & 1` to check bit `i` directly instead of manually building reversed bit arrays — cleaner and avoids extra allocations.
- **Interview style**: The current solution uses nested helper functions (`canBeRemoved`, `achievedMax`, `remove`, `add`) and a `deepcopy` — this adds cognitive overhead for an interviewer. Prefer a single-pass approach with a flat loop body. Keep state in a simple `last[32]` array rather than dictionaries. Name variables to match the problem domain (e.g. `last_seen_bit`, `window_end`) rather than generic names like `d` or `x`.
