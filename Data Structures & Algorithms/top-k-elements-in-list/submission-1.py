class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        arr = [[] for i in range(len(nums)+1)]
        
        for n, f in freq.items():
            arr[f].append(n)

        ans = []
        for i in range(len(nums),-1,-1):
            for j in arr[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans