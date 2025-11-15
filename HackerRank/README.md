# HackerRank Solutions

This directory contains solutions to HackerRank problems.

## Structure

Solutions are organized by domain and problem name:
```
Algorithms/
├── Warmup/
│   └── Simple_Array_Sum.py
├── Sorting/
│   └── Bubble_Sort.java
```

## Categories

- Algorithms
- Data Structures
- Mathematics
- SQL
- Databases
- Regex
- And more...

## Solution Format

Each solution should include:
- Problem link in comments
- Problem description
- Constraints
- Clean, well-commented code

## Example

```python
# Problem: Simple Array Sum
# Link: https://www.hackerrank.com/challenges/simple-array-sum
# Domain: Algorithms > Warmup
# Difficulty: Easy

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    result = simpleArraySum(ar)
    print(result)
```
