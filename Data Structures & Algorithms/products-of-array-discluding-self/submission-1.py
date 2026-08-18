class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        a = 1
        for k in nums:
            if k != 0:

                a *= k
       
        x = nums.count(0)

        for i in nums:
            if x == 0:
                res.append(a//i)
            elif x == 1 and i == 0:
                res.append(a)
            elif x == 1 and i != 0:
                res.append(0)
            else:
                res.append(0)
        return res
            
