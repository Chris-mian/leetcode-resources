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

### 2411 — Submission

```python
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
```

---

### 2411 — Thought process review

The inline comments in the original submission reveal the reasoning:

- `# for initial round, start at max and shrink. then proceedingly, remove prev and check if any went from non-zero to zero, in that case, expand to right` — This captures the core two-pointer invariant correctly: start with the full suffix, shrink to minimal, then as `left` advances, expand `right` only when the window loses a required bit. The insight is solid, but the implementation splits into two branches (`left == 0` vs else) rather than encoding this as one unified loop. In an interview, state this invariant explicitly upfront: *"I maintain a window where every bit in the global OR is still represented."*
- `# print("left", left, ans, maxCountAtIndex)` / `# print("right:", right, countAtIndex)` — Debug prints suggest the shrink-then-expand logic was tricky to get right. This is a sign the state tracking (`countAtIndex` vs `maxCountAtIndex` vs `numsInBits`) has too many moving parts. The sweep-line approach (tracking `last[bit]`) sidesteps this entirely — no add/remove, no debug prints needed.
- The `canBeRemoved` check (`d[i] < 2`) is a clever way to ask "is this element the *only* contributor of some bit?" — but it's non-obvious at a glance. In an interview, prefer naming it `is_sole_contributor` or just comment the invariant: "safe to remove if every bit it contributes still has another source in the window."

---

### Interview style notes

- Avoid `deepcopy` and nested helper functions (`canBeRemoved`, `achievedMax`, `remove`, `add`) — they add cognitive overhead for the interviewer. A single flat loop with a `last[32]` array is easier to follow and debug.
- Name variables to match the problem domain: `last_seen_bit`, `window_end` instead of `d`, `x`.
- The two-pointer logic has separate handling for `left == 0` vs subsequent iterations. Unify into one loop body to reduce edge-case reasoning.
