# Contributing Guidelines

Thank you for considering contributing to this repository! This guide will help you add your solutions properly.

## How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button at the top right of this page

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/data_structures-.git
   cd data_structures-
   ```

3. **Create a Branch**
   ```bash
   git checkout -b add-solution-name
   ```

4. **Add Your Solution**
   - Navigate to the appropriate platform directory
   - Follow the structure outlined in that directory's README
   - Add your solution with proper comments and documentation

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add [Platform] [Problem Name] solution"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin add-solution-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes

## Solution Guidelines

### Code Quality
- Write clean, readable code
- Add comments explaining complex logic
- Use meaningful variable names
- Follow language-specific conventions

### Documentation
Each solution should include:
- Problem link
- Problem description or summary
- Difficulty level
- Time complexity
- Space complexity
- Explanation of approach (if complex)

### File Organization
- Place solutions in the correct platform directory
- Use appropriate naming conventions
- Create subdirectories if needed for organization

### Languages
- Any programming language is welcome
- Multiple language solutions for the same problem are encouraged
- Name files with appropriate extensions (.py, .java, .cpp, etc.)

## Example Solution Structure

### Python Example
```python
"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Description:
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a hash map to store seen numbers and their indices.
For each number, check if its complement exists in the map.
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### C++ Example
```cpp
/*
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
*/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
```

## Code Review

All submissions will be reviewed for:
- Correctness
- Code quality
- Documentation completeness
- Proper organization

## Questions?

If you have any questions, please:
- Open an issue
- Check existing issues for similar questions
- Review the README files in each directory

Happy coding!
