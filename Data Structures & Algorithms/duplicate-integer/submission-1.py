class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums) # converts to set containing only unquie elements
        return len(sett) != len(nums) # this will match the lenths of both