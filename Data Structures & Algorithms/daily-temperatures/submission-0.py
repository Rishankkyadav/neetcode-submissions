class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            for j in range( i + 1 , len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    break
            else:
                res.append(0)
                
        return res
                    
                
                




        