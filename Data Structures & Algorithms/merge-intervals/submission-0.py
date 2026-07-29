class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0],x[1]))
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = res[-1]

            if curr[0] <= prev[1]:
                res[-1] = [min(prev[0],curr[0]), max(prev[1],curr[1])]
            else:
                res.append(curr)
        
        return res
