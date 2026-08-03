class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = [(position[i],speed[i]) for i in range(len(position))]
        sorted_list.sort(key = lambda x: x[0], reverse=True)
        fleets = []
        for i, val in enumerate(sorted_list):
            time_to_end = (target-val[0])/val[1]
            if not fleets or ((target-fleets[-1][0]) / fleets[-1][1]) < time_to_end:
                fleets.append(val)
        return len(fleets) 