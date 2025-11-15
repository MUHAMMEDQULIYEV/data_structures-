# LeetCode Solutions

This directory contains solutions to LeetCode problems.

## Structure

Solutions are organized by problem number and name:
```
001_Two_Sum/
├── solution.py
├── solution.java
└── README.md
```

## Naming Convention

- Use problem number followed by problem name
- Separate words with underscores
- Example: `001_Two_Sum`, `002_Add_Two_Numbers`

## Solution Format

Each solution should include:
- Problem link in comments
- Problem description
- Time and space complexity
- Clean, well-commented code

## Example

```python
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
