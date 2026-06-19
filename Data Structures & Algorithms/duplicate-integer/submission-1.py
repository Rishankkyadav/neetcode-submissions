class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False
