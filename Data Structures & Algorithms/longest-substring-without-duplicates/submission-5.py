class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
            max_len = max(max_len , len(seen))

        return max_len



    

        