class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1

        sorted_freq = sorted(freq.items() , key = lambda x : x[1] , reverse = True )


        for i,l in sorted_freq:
            ans.append(i)
        return ans[:k]
            