class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            i1 = ''.join(sorted(i))

            res[i1].append(i)
        
        return list(res.values())

        
        