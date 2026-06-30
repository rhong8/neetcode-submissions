class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)#key: key value: list[timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        print(f"appending {(timestamp, value)}")
        self.store[key].append((timestamp, value))
        
        #assuming there aren't multiple set methods of the same value

    def get(self, key: str, timestamp: int) -> str:
        result = "" #initialize it to empty string


        
        if key in self.store:
            store = self.store[key]
            print(f"store: {store}")

            l, r = 0, len(store) - 1

            while l <= r:
                mid = (l + r)  // 2
                
                #this is valid  so we can store the value
                if store[mid][0] <= timestamp:
                    result = store[mid][1] #store the value
                    l = mid + 1 #keep looking
                else:
                    r = mid - 1
        
        return result
