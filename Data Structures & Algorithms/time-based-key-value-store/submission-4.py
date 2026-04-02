class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))
        print(self.map)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        # Check if the timestamp is greater than (or equal to) the most recent timestamp 
        # for this key
        values = self.map[key]
        latest_val = values[-1]
        if timestamp >= latest_val[0]:
            return latest_val[1]
        
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (high + low) // 2
            curr_timestamp = values[mid][0]

            if timestamp == curr_timestamp:
                return values[mid][1]
            elif timestamp > curr_timestamp:
                low = mid + 1
            else:
                high = mid - 1

        # If `timestamp` is greater than the `mid` timestamp, we return the value corresponding
        # to the mid timestamp. Otherwise, we return ""
        if high >= 0 and values[high][0] < timestamp:
            return values[high][1]
        return "" 

