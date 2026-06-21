class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        ans1 = 1
        ans = 1
        for i in range(len(nums)):
            ans1 = 1
            ans = 1
            arr_r = nums[:i]
            arr_l = nums[i+1:]

            for j in arr_r:
                ans *= j
                
            
            for k in arr_l:
                ans1 *= k
               
            
            res.append(ans * ans1)
        return res

            




            
         
        
        
        