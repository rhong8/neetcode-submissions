class TimeMap:

    class Inner:
        def __init__(self):
            self.timestamps = []
            self.val_map = defaultdict(str) #key: timestamp value: value


    def __init__(self):
        self.structures = defaultdict(TimeMap.Inner)#key: name value: innerstructure

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structures[key].timestamps.append(timestamp) #timestamps are guranteed to increase
        self.structures[key].val_map[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        
        
        print(f"Attempting to find {timestamp}")
        #binary search, converge on the closest value then walk the pointer backwards until it finds a value less than it
        inner = self.structures[key]


        l, r = 0, len(inner.timestamps) - 1
        if r == -1: #then the structure doesn't exist
            return '' 

        mid = 0
        found: int = -1 
        while l <= r:

            mid = (l + r) // 2
            if inner.timestamps[mid] == timestamp: #found the exact timestamp in the nums array
                found = inner.timestamps[mid]
                break
            elif inner.timestamps[mid] > timestamp: #split left
                r = mid - 1
            else:
                l = mid + 1
        
        print(f"mid: {mid} timestamps: {inner.timestamps}")
        print(f"full val_map: {inner.val_map.items()}")

        if found == -1: #iterate the pointer back until it finds the appropiate value
            t = inner.timestamps[r]

            if t <= timestamp:
                return inner.val_map[inner.timestamps[r]]
            else:
                return '' #no timestamp before that was found
        

        print(f"found it: {inner.val_map[found]} at {found}")
        return inner.val_map[found]
        
