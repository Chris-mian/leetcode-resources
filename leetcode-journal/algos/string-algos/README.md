# String Algorithms

Notes and reflections for string problems (palindromes, parsing, etc.).

---

## Problems

| #   | Title                              | Link | Difficulty | Status | Notes |
| --- | ---------------------------------- | ---- | ---------- | ------ | ----- |
| 5   | Longest Palindromic Substring      | [LC](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | ✅ | see below |
| 1650 | Lowest Common Ancestor of a Binary Tree III | [LC](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/submissions/1783709246/) | Medium | ✅ | first attempt forgot that only need to record 1 path; should not impact correctness |

---

## Notes: Longest Palindromic Substring

- dealing with boundaries can be simplified with adding end chars
- in palindrome case, it is easier to memorize left and right versus center and wing length (odd case and manipulation are prone to errors)
