# Sliding Window

Notes and reflections for sliding window problems.

---

## Problems

| #   | Title       | Link | Difficulty | Status | Attempts | Notes        |
| --- | ----------- | ---- | ---------- | ------ | -------- | ------------ |
| 837 | New 21 Game | [LC](https://leetcode.com/problems/new-21-game/) | Medium | ✅ | — | optimization: see below |
| 2106 | Maximum Fruits Harvested After at Most K Steps | [LC](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) | Hard | ✅ | 1 | see below |

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

---

## 2106 — Maximum Fruits Harvested After at Most K Steps

### Reflections

- Sliding window over the sorted fruit array indices (not raw positions). For each left boundary, expand right as far as reachable within `k` steps using the turn-once cost formula: `min(2 * leftDist + rightDist, 2 * rightDist + leftDist)`. Both pointers only advance, so total work is O(n).

### 2106 — Submission

```python
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # it only makes sense to turn direction once. if farthest reach is x steps to L and y steps to rigt,
        # then choose the min(x,y) to go first as the final will be 2x + y steps.
        # I can compute with each window, what's the max result i can get with it as leftmost position. O(max(pos)) this is infinite.
        # to improve time complexity, we can only look at positions where fruits are available.

        # As I was thinking about this last night, my problem with previous apoproach is that there is no O(1) access
        # but we actually, just need to loop through left to right, giving us sorted. For each one, consider it as the leftmost point, then decide what's the rightmost point we can reach.
        # Still, although this is very intuitive based on the data structure, this does not give us O(1) access as well. If we calculated the rightmost point we can reach, but there is no way for us to know at that point what's the total number of strawberries we can get with all of one time complexity.
        # So instead, we should look at the first one on the left. Then with o of n find its rightmost point. Then after each iteration, we move the left one to the next one. We know the rightmost one cannot be any more towards the left; it will be definitely more towards the right. That way, every check is O(1) on ave

        # lowerBound = fruits[0][0] #inclusive
        # upperBound = fruits[0][0] # inclusive
        lowerBound = 0 #inclusive
        upperBound = 0 # inclusive
        curFruitCount = 0
        maxFruitCount = 0
        while lowerBound < len(fruits):
            # cur min pos
            pos, fruitNum = fruits[lowerBound]
            if lowerBound > 0:
                curFruitCount -= fruits[lowerBound-1][1]
            # cur max pos, should start from prev

            while upperBound < len(fruits) and self.lessThanKSteps(fruits[lowerBound][0], fruits[upperBound][0], k, startPos):
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
            return min((cur-left) * 2 + (right-cur), (right-cur)*2 + (cur-left)) <= k
```

---

### 2106 — Thought process review

The inline comments reveal a clear multi-stage reasoning process:

- `# it only makes sense to turn direction once. if farthest reach is x steps to L and y steps to rigt, then choose the min(x,y) to go first as the final will be 2x + y steps.` — Correct and essential insight. This is the key observation that reduces the problem from exponential path search to a geometric constraint. In an interview, state this upfront as the first thing you write on the board — it's the "aha" that unlocks the problem.

- `# I can compute with each window, what's the max result i can get with it as leftmost position. O(max(pos)) this is infinite.` — Good instinct to think about windows, but correctly identified that iterating over all positions is unbounded. This shows you caught a pitfall early rather than coding a wrong approach.

- `# to improve time complexity, we can only look at positions where fruits are available.` — This is the pivot to the correct approach. In an interview, phrase it as: *"The fruit array is sparse and sorted, so I only need to consider fruit positions as window boundaries."*

- `# my problem with previous approach is that there is no O(1) access` — This is the crux of the `while` vs `for` / index vs position debate. You initially thought about using actual positions as pointers (commented-out `lowerBound = fruits[0][0]`), which would make random-access expensive. The realization that array *indices* give O(1) access to both position and count is what makes the sliding window work.

- `# we should look at the first one on the left. Then with O(n) find its rightmost point. Then after each iteration, we move the left one to the next one. We know the rightmost one cannot be any more towards the left` — This is the monotonicity argument that proves the two-pointer approach is O(n). In an interview, say exactly this: *"The right pointer never moves left because expanding the left boundary can only allow the right boundary to go further right."* This is the sentence interviewers want to hear.

- Commented-out lines `# lowerBound = fruits[0][0]` → `lowerBound = 0` — Shows you initially confused index vs position, then corrected. **Guidance**: when designing two-pointer solutions, decide upfront what your pointers represent and write it down. Here, both pointers are *indices into the fruit array*, and you derive positions via `fruits[i][0]`. Keeping that separation clear from the start avoids false starts.

---

### Interview style notes

- **`while` vs `for` for two pointers**: Use `while` when the right pointer persists across left-pointer iterations (as here — `upperBound` never resets). Use `for` for the outer pointer when every element is visited exactly once. Your choice of `while` for both is correct but a `for lowerBound in range(len(fruits))` outer loop would be more idiomatic and signal "I visit each left boundary exactly once."
- **Index vs position**: The commented-out `fruits[0][0]` lines show an initial attempt to use raw positions as pointers. Always use array indices for pointers and derive positions when needed — this guarantees O(1) access and avoids off-by-one confusion with gaps between positions.
- **Unused variable**: `pos, fruitNum = fruits[lowerBound]` unpacks but neither is used after. Remove dead code in interviews — it signals unfinished thinking.
- **Helper naming**: `lessThanKSteps` is descriptive but `is_reachable(left_pos, right_pos, k, start)` reads more naturally as a boolean predicate.
- **Three-case helper**: The `lessThanKSteps` method handles all-right, all-left, and turn cases cleanly. In an interview, briefly state the three cases before coding them — it shows structured thinking.
