class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in count:
                count[key] = []

            count[key].append(i)

        return list(count.values())
            
           
              


        

            

        