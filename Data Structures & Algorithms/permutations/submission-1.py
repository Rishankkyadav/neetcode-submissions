class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for permutation in perms:
            for i in range(len(permutation) + 1):
                permutation_copy = permutation.copy()
                permutation_copy.insert(i , nums[0])
                res.append(permutation_copy)
        return res
        