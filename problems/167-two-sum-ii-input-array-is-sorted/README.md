# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search

## Problem

[LeetCode Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed sorted array, find two numbers that add up to target. Return their indices (1-indexed). Must use constant extra space.

## My Initial Approach (Binary Search - O(n log n))

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def binarySearch(t: int, lo: int, hi: int) -> int | None:
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if numbers[mid] > t:
                hi = mid
            elif numbers[mid] < t:
                lo = mid
            else:
                return mid
        if numbers[lo] == t:
            return lo
        elif numbers[hi] == t:
            return hi
        return None

    for i in range(len(numbers) - 1):
        otherIdx = binarySearch(target - numbers[i], i + 1, len(numbers) - 1)
        if otherIdx is not None:
            return [i + 1, otherIdx + 1]
    return []
```

## Optimal Approach (Two Pointers - O(n))

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        curr_sum = numbers[lo] + numbers[hi]
        if curr_sum == target:
            return [lo + 1, hi + 1]
        elif curr_sum < target:
            lo += 1  # need bigger sum, move left pointer right
        else:
            hi -= 1  # need smaller sum, move right pointer left
    return []
```

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Binary Search | O(n log n) | O(1) |
| Two Pointers | O(n) | O(1) |

## Reflection: Why I Missed Two-Pointers

### What Happened

I saw "sorted array + find a value" and pattern-matched to binary search. This works but misses the optimal solution.

### The Mental Gap

**Binary Search Framing:** "For each element, search for its complement"
- Treats it as n independent search problems
- Each search is O(log n), total O(n log n)

**Two Pointers Framing:** "Eliminate invalid pairs by moving boundaries"
- Treats it as one narrowing problem
- Each step eliminates one index permanently, total O(n)

### The Key Insight I Missed

With sorted data and a sum constraint:
- If `nums[lo] + nums[hi] > target`: then `nums[lo] + nums[anything ≥ hi]` is ALSO too big
- Therefore, `hi` can **never** be part of any valid pair with current `lo` or anything to its left
- We can safely eliminate `hi` entirely (not just skip it for this iteration)

This is **monotonic elimination** — each decision permanently removes one candidate.

### Pattern Recognition Checklist

When to consider Two Pointers over Binary Search:

| Condition | Two Pointers | Binary Search |
|-----------|--------------|---------------|
| Sorted array | ✓ | ✓ |
| Finding pairs/sums | ✓✓ | ✓ |
| Can eliminate regions, not just values | ✓✓ | ✗ |
| Need O(n) | ✓ | ✗ |
| Relationship between elements matters | ✓✓ | ✗ |

### Questions to Ask Yourself

1. "Am I searching for a **specific value** or **narrowing down a range**?"
2. "If this pair doesn't work, can I **eliminate an entire region** (not just one element)?"
3. "Does the sorted property create a **monotonic relationship** I can exploit?"

## Key Learnings

- **Sorted + pairs/sums → always consider two-pointers from both ends**
- Binary search = find specific value; Two pointers = eliminate invalid regions
- Two pointers works when each comparison gives you information about an **entire region**, not just one element
- The "two pointers from ends" pattern is specifically for problems where sum/relationship constraints + sorted order create monotonic elimination
