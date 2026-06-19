class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        l, r = 0 , len(arr) - 1
        i = -1
        valid = None

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                i = mid
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid - 1

        return "" if i == -1 else arr[i][1]
