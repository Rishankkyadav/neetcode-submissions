# so after replacing k characters , i have to return the len of max str that has at max k different chracters , so apparntly i was wrong and gpt corrected me i have to start a window and window len  


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = {}
        vroski = 0
        vro = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r] , 0 ) + 1
            diff = (r-l + 1) - max(count.values())
            if diff > k:
                count[s[l]] -= 1
                l += 1
            vroski = r - l + 1
            vro = max(vro , vroski)
        return vro


            
            
        