class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set(nums)

        if len(nums) == len(nums1):
            return False
        else:
            return True

        