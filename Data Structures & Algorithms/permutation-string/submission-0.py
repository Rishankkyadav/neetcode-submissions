class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = l + len(s1)
        checker = {}
        count = {}
        for i in range(len(s1)):
            checker[s1[i]] = checker.get(s1[i] , 0) + 1
        
        if len(s1) > len(s2):
            return False
        else:
            for i in range(l , r ):
                count[s2[i]] = count.get(s2[i] , 0) + 1

        if count == checker:
            return True
        
        while r < len(s2):
            count[s2[l]] -= 1
            if count[s2[l]] == 0:
                del count[s2[l]]

            count[s2[r]]  =  count.get(s2[r] , 0) + 1

            if count == checker:
                return True
            r += 1
            l += 1
        return False
        
                


        

         
        

        