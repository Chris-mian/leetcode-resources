# Two Pointers

Notes and reflections for two pointers problems.

---

## Core Insight

Two pointers works when you can **eliminate entire regions** based on a single comparison. This requires:
1. **Sorted or ordered data** — so relationships are predictable
2. **Monotonic elimination** — if a pair fails, you know one element can't work with ANY remaining candidates

### When to Use Two Pointers vs Binary Search

| Scenario | Two Pointers | Binary Search |
|----------|--------------|---------------|
| Find specific value | ✗ | ✓ |
| Find pair with sum constraint | ✓✓ | ✓ (slower) |
| Eliminate regions, not just values | ✓✓ | ✗ |
| O(n) required | ✓ | ✗ |

### Key Question to Ask

> "If this pair doesn't work, can I eliminate an **entire region** (not just skip one element)?"

If yes → Two pointers. If no → Binary search or hash map.

---

## Problems

| Date | # | Title | Link | Difficulty | Status | Attempts | Notes |
| ---- | --- | ----- | ---- | ---------- | ------ | -------- | ----- |
| 2026-01-27 | 2411 | Smallest Subarrays With Maximum Bitwise OR | [LC](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) | Medium | ✅ | 1 | bit-freq window; see [bit-manipulation](../bit-manipulation/README.md) |
| 2026-02-06 | 167 | Two Sum II - Input Array Is Sorted | [LC](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | ✅ | 1 | Initially used binary search O(n log n); optimal is two-pointers O(n). Key: sorted + sum → monotonic elimination |
