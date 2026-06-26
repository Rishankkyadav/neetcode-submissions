class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        ans = []
        final = []
        max_r = 0
        max_l = 0
        result = 0
        rev_height = height[::-1]
        left = len(height) - 1
        right_max = []
        left_max = []
        for i in range(len(height)):
            max_r = max(max_r , height[i])
            right_max.append(max_r)

        for j in range(len(rev_height)):
            max_l = max(max_l , rev_height[j])
            left_max.append(max_l)
        left_max = left_max[::-1]
        
        for k in range(len(right_max)):
            final.append(min(right_max[k] , left_max[k]))

        for l in range(len(final)):
            job = final[l] - height[l]
            if job > 0:
                ans.append(job)
            else:
                ans.append(0)
        
        for z in ans:
            result += z
        return result
    
        
        

                






        
        


        