"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Time Complexity: O(n) - We iterate through the array once
Space Complexity: O(n) - Hash map stores up to n elements

Approach:
We use a hash map to store numbers we've seen and their indices.
For each number, we calculate its complement (target - number).
If the complement exists in our hash map, we've found our answer.
Otherwise, we add the current number to the hash map and continue.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers
        """
        seen = {}  # Dictionary to store {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # Should never reach here based on problem constraints
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")
