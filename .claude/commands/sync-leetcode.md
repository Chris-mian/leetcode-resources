# Sync LeetCode Solution

Sync a LeetCode solution to git and Notion tracking database.

## Input

The user will provide ONE of:
- A LeetCode problem URL (e.g. https://leetcode.com/problems/two-sum/)
- Problem details manually: problem number, name, difficulty, topics, and their solution code

## Steps

### 1. Gather Problem Info

Ask the user for any missing information:
- **Problem number** (e.g. 1)
- **Problem name** (e.g. "Two Sum")
- **Difficulty** (Easy / Medium / Hard)
- **Topics** (Array, String, Hash Table, Dynamic Programming, Math, Sorting, Greedy, DFS, BFS, Binary Search, Tree, Graph, Two Pointers, Stack, Heap, Linked List, Backtracking)
- **Solution code** (Python)
- **Time complexity** (e.g. O(n))
- **Space complexity** (e.g. O(n))
- **Confidence** (1-5 stars)
- **Key learnings** (optional notes)
- **Time taken in minutes** (optional)

### 2. Create Solution File in Git

Create the file at: `problems/{number}-{slug}/solution.py`

The slug is the problem name lowercased with hyphens (e.g. "two-sum").

The solution file should have a header comment:
```python
"""
LeetCode {number}: {name}
Difficulty: {difficulty}
Topics: {topics}
Link: https://leetcode.com/problems/{slug}/

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""
```
Followed by the user's solution code.

### 3. Create Problem README

Create `problems/{number}-{slug}/README.md` with:
```markdown
# {number}. {name}

**Difficulty:** {difficulty}
**Topics:** {topics}

## Problem

[LeetCode Link](https://leetcode.com/problems/{slug}/)

## Approach

{brief description of approach based on the code}

## Complexity

- **Time:** {time_complexity}
- **Space:** {space_complexity}

## Key Learnings

{key_learnings or "N/A"}
```

### 4. Update LeetCode Journal

For each topic in the problem's topics list, update `leetcode-journal/algos/{topic}/README.md`:

1. **If the topic directory doesn't exist**, create it with a new `README.md` following this template:
   ```markdown
   # {Topic Name}

   Notes and reflections for {topic} problems.

   ---

   ## Problems

   | Date       | #    | Title | Link | Difficulty | Status | Attempts | Notes |
   | ---------- | ---- | ----- | ---- | ---------- | ------ | -------- | ----- |
   | {date} | {number} | {name} | [LC]({url}) | {difficulty} | ✅ | {attempts} | see reflections below |

   ---

   ## Reflections

   - **{number} — {name}**: {key_learnings}

   ### {number} — Submission

   ```python
   {user's solution code}
   ```

   ---

   ### Interview style notes

   {analysis of code structure improvements for interview readability}
   ```
   Also add an entry to `leetcode-journal/README.md` index table.

2. **If the topic directory exists**, append a row to the Problems table and add a reflection entry. For secondary topics, add a row with a cross-reference to the primary topic's journal.

**Key learnings formatting rules:**
- Always rephrase the user's raw notes for better context and readability — be concise yet insightful.
- Always include an "Interview style notes" section analyzing how the code structure could be improved for interview coding expectations (naming, helper function usage, loop structure, etc.).

### 5. Git Commit and Push

```
git add problems/{number}-{slug}/ leetcode-journal/
git commit -m "Add solution: {number} - {name} ({difficulty})"
git push origin HEAD
```

### 6. Update Notion Database

Use the Notion MCP `notion-create-pages` tool to add an entry to the "LeetCode Interview Prep Tracker" database.

**Data source ID:** `ea4b8909-f2dd-440f-bf3f-7968f82aa597`

Create a page with these properties:
- `Problem Name`: "{number}. {name}"
- `Problem Number`: {number}
- `Difficulty`: "{difficulty}"
- `Topics`: JSON array of topic strings
- `Status`: "Solved"
- `date:Date Solved:start`: today's date (YYYY-MM-DD)
- `date:Date Solved:is_datetime`: 0
- `LeetCode Link`: "https://leetcode.com/problems/{slug}/"
- `Git Commit Link`: the GitHub commit URL after pushing
- `Time Complexity`: "{time_complexity}"
- `Space Complexity`: "{space_complexity}"
- `Confidence`: star emoji based on confidence (1="⭐", 2="⭐⭐", etc.)
- `Attempts`: 1 (or ask user)
- `Time Taken (min)`: {time_taken} if provided
- `Key Learnings`: "{key_learnings}" if provided
- `Need Review`: "__NO__" (or "__YES__" if confidence <= 2)

### 7. Confirm

Show the user a summary:
- File created: `problems/{number}-{slug}/solution.py`
- Git commit hash and link
- Notion page link
