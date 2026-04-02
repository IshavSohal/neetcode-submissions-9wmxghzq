class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleets = []
        fleetStack = []

        for i in range(n):
            fleets.append([position[i], speed[i]])

        fleets = sorted(fleets, key=lambda d: d[0], reverse=True)
        print("fleets")
        print(fleets)


        for fleet in fleets:
            timeToDest = (target - fleet[0]) / fleet[1]

            if len(fleetStack) > 0 and fleetStack[-1]["timeToDest"] >= timeToDest:
                print('merge')
                fleetStack[-1]["cars"] += 1

            else:
                fleetStack.append({"position": fleet[0], "speed": fleet[1], "cars": 0, "timeToDest": timeToDest})

        return len(fleetStack)
            