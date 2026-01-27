# Sliding Window

Notes and reflections for sliding window problems.

---

## Problems

| #   | Title       | Link | Difficulty | Status | Attempts | Notes        |
| --- | ----------- | ---- | ---------- | ------ | -------- | ------------ |
| 837 | New 21 Game | [LC](https://leetcode.com/problems/new-21-game/) | Medium | ✅ | — | optimization: see below |

Problem list (sliding-window): [link](https://leetcode.com/problems/new-21-game/?envType=problem-list-v2&envId=sliding-window&roomId=ZdmwPu)

---

## New 21 Game: optimization (sliding window on DP)

The recurrence is `M[x] = (1/maxPts) * sum(M[x-1], …, M[x-maxPts])` (only for prior sums &lt; k). The inner sum is over a fixed window of size `maxPts`. Instead of recalculating it each time (O(maxPts) per state), keep a running sum. When moving from `x-1` to `x`, add `M[x-1]` and subtract `M[x-1-maxPts]` (if valid and &lt; k). That gives **O(1)** per state and **O(k + maxPts)** overall instead of **O((k + maxPts) · maxPts)**.

---

## New 21 Game: submission

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # alice's last draw would end up in a range from k ~ (k-1 + max)
        # if n >= (k-1 + max), then it's 1 def
        # if n < k then no but this is exlucded
        # now the problem is calculating the probablility of ending at each sum
        # we can build a bottom up DP to solve this problem
        # M[x] = sum over i from 1 to max // M[x-i]*1/max
        if n >= (k-1+maxPts):
            return 1
        if k == 0:
            return 1
        M = [0]*(k+maxPts)
        uniProb = 1/maxPts
        for i in range(1,maxPts+1):
            M[i] = uniProb
        for targetSum in range(2,k+maxPts):
            ptargetSum = 0
            for drawNumber in range(1, maxPts+1): #TODO edit boundary condition that whenever it meets k, it will stop
                if (targetSum-drawNumber) < 1:
                    break
                if (targetSum-drawNumber) >= k:# it would not continue to draw in this case
                    continue
                ptargetSum += M[targetSum-drawNumber]*uniProb
            M[targetSum] = ptargetSum + M[targetSum]
        ans = sum(M[k:n+1])
        # print(M)
        return ans
```

---

## New 21 Game: interview checklist

| Watch out for | Notes |
| -------------- | ----- |
| **State definition** | Say it explicitly: *M[i] = probability of ever reaching sum `i` before stopping (i.e. before reaching ≥ k).* |
| **Sliding-window optimization** | Recurrence needs a sum over the last `maxPts` values. Keep a running sum; each step is add new, drop oldest → O(1) per state. Draw the window on the board. |
| **Edge cases** | (1) `k == 0` → return 1. (2) `n >= (k - 1 + maxPts)` → return 1 (all possible end sums are ≤ n). (3) `n < k` → 0; your `M[k:n+1]` gives `sum([]) = 0` ✓. |
| **`M[targetSum] = ptargetSum + M[targetSum]`** | The `+ M[targetSum]` is the “direct draw” when `targetSum <= maxPts` (from your init). It works but is easy to miss; consider `if targetSum <= maxPts: ptargetSum += uniProb` for clarity. |
| **Loop structure** | Using both `break` (prev &lt; 1) and `continue` (prev ≥ k) is fine; an alternative is one loop over `d in range(1, min(maxPts, targetSum)+1)` and a single `if` for “prev in [1, k-1]”. |
| **Naming** | `ptargetSum` → e.g. `probFromPrev` or `probReach`; `drawNumber` = value of the card drawn. |
| **Problem label** | It’s DP; the “sliding window” part is the optimization on the recurrence. Saying that shows you see both the DP and the window. |
| **Array size** | `M` has length `k + maxPts`; valid indices `0..k+maxPts-1`. You early-return when `n >= k+maxPts-1`, so `M[k:n+1]` never goes out of bounds. |
