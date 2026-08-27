class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        return False if len(test) == len(nums) else True
        