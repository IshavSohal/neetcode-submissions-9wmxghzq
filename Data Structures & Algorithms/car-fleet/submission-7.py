class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleets = []
        num_fleets = 0
        cars_arrived = 0

        # Populate the stack of fleets, ordered from closest to furthest (from target)
        for i in range(n):
            fleets.append({"position": position[i], "speed": speed[i], "cars": 1, "timeElapsed": 0})

        fleets = sorted(fleets, key=lambda d: d['position'])


        # use a while loop to increment <hour> until all cars/fleets have arrived '
        # at destination
        while cars_arrived < n:
            print("")
            if len(fleets) == 0:
                break

            for i in range(len(fleets)-1,-1,-1):
                print(" ")
                print('current fleet')
                print(fleets[i])

                
                # If fleet i catches up to fleet i+1, and fleet i+1 hasnt reached the destination, we can just merge them (without considering timeElapsed)
                # If the fleet ahead of fleet i+1 has reached the destination within the hour, we need to determine whether fleet i catches up to
                # fleet i+1 before (or exactly when) it arrives at the destination
                if i < len(fleets) - 1 and fleets[i]["position"] + fleets[i]["speed"] >= fleets[i+1]["position"] and \
                (fleets[i+1]["position"] != target or (fleets[i+1]["position"] == target and \
                                                        (fleets[i]["timeElapsed"] + ((target - fleets[i]["position"])/fleets[i]["speed"])) <= fleets[i+1]["timeElapsed"])):
                        print('fleets merged')
                        print(fleets[i])
                        print(fleets[i+1])
                        print(" ")
                        fleets[i]["cars"] += fleets[i+1]["cars"]
                        fleets[i]["position"] = fleets[i+1]["position"]
                        fleets[i]["speed"] = fleets[i+1]["speed"]
                        fleets[i]["timeElapsed"] = fleets[i+1]["timeElapsed"]

                        fleets[i+1]["position"] = 0
                        fleets[i+1]["speed"] = 0
                        fleets[i+1]["cars"] = 0
                else:
                    print('case 2')
                    # Need to update the position and timeElapsed for fleet i when it has not merged with the fleet in front of it
                    # (or if there is no fleet in front of it)
                    if fleets[i]["position"] + fleets[i]["speed"] > target:
                        print('case 2.1')
                        fleets[i]["timeElapsed"] += (target - fleets[i]["position"])/fleets[i]["speed"]
                        fleets[i]["position"] = target
                    else:
                        print('case 2.2')
                        fleets[i]["position"] += fleets[i]["speed"]
                        fleets[i]["timeElapsed"] += 1


                    
            temp_fleets = []
            for fleet in fleets:
                if fleet["speed"] > 0:
                    temp_fleets.append(fleet)
                else:
                    print('empty fleet removed')

            fleets = temp_fleets

            while len(fleets) > 0 and fleets[-1]["position"] == target:
                print('fleet arrived')
                print(fleets[-1])
                cars_arrived += fleets[-1]["cars"]
                num_fleets += 1
                fleets.pop()

        return num_fleets
            