class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_ct = 0
        max_ct = 0

        for num in nums:
            if num == 1:
                curr_ct += 1

                if curr_ct > max_ct:
                    max_ct = curr_ct
            else:
                curr_ct = 0
                
        return max_ct
            
