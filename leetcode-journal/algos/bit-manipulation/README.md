# Bit Manipulation

Notes and reflections for bit manipulation problems.

---

## Problems

| Date       | #    | Title                                          | Link | Difficulty | Status | Attempts | Notes |
| ---------- | ---- | ---------------------------------------------- | ---- | ---------- | ------ | -------- | ----- |
| 2026-01-27 | 2411 | Smallest Subarrays With Maximum Bitwise OR     | [LC](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) | Medium | ✅ | 1 | see reflections below |

---

## Reflections

- **2411 — Smallest Subarrays With Maximum Bitwise OR**: Current solution tracks per-bit frequency counts with add/remove helpers over a two-pointer window. A cleaner approach: for each bit position, record the *last index* where that bit is 1, then sweep right-to-left — `ans[i] = max(last[bit] - i + 1)` over all 32 bits. This eliminates the helper functions entirely. Use `(x >> i) & 1` instead of manually building reversed bit arrays.

### Interview style notes

- Avoid `deepcopy` and nested helper functions (`canBeRemoved`, `achievedMax`, `remove`, `add`) — they add cognitive overhead for the interviewer. A single flat loop with a `last[32]` array is easier to follow and debug.
- Name variables to match the problem domain: `last_seen_bit`, `window_end` instead of `d`, `x`.
- The two-pointer logic has separate handling for `left == 0` vs subsequent iterations. Unify into one loop body to reduce edge-case reasoning.
