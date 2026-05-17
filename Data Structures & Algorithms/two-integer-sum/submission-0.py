class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store numbers and their indices
    
        for i, num in enumerate(nums):
            complement = target - num  # Find the number needed to reach target
            
            if complement in num_map:  # Check if it's already in the dictionary
                return [num_map[complement], i]  # Return indices
            
            num_map[num] = i  # Store the number with its index