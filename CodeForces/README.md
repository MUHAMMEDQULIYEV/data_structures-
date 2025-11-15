# CodeForces Solutions

This directory contains solutions to CodeForces problems.

## Structure

Solutions are organized by contest number and problem letter:
```
Contest_1234/
├── A_Problem_Name.py
├── B_Problem_Name.cpp
└── README.md
```

## Naming Convention

- Use contest number followed by problem letter and name
- Example: `Contest_1234`, `A_Problem_Name.py`

## Solution Format

Each solution should include:
- Problem link in comments
- Problem statement summary
- Input/Output format
- Time and space complexity
- Clean, well-commented code

## Example

```python
# Problem: A - Problem Name
# Contest: 1234
# Link: https://codeforces.com/contest/1234/problem/A
# Difficulty: 800
# Time Complexity: O(n)

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Solution logic here
    print(result)

if __name__ == "__main__":
    solve()
```
