class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_rate = 1 #(sum(piles) + h - 1) // h
        high_rate = max(piles)
        best_rate = None

        while low_rate <= high_rate:
            mid_rate = (high_rate + low_rate) // 2
            hours_passed = 0
            piles_completed = 0

            # Determine if we can eat all bananas within h hours, using an 
            # eating rate of `mid_rate`
            for pile in piles:
                
                # For each pile, we compute the number of hours it would take to complete it
                # using an eating rate of `mid_rate`
                hours_passed += (pile + mid_rate - 1) // mid_rate  # need to use ceil div

                # If we have exceeded `h` hours, we do not count the current pile as completed
                # because it was not eaten within `h` hours. We also exit the loop, so that we
                # do not process any more piles
                if hours_passed > h:
                    break

                piles_completed += 1


            # Check if all bananas were eaten using `mid_rate`. If so, we set `high_rate` to the 
            # eating rate below `mid_rate`. If not, then we set `low_rate` to the eating rate
            # above `mid_rate`
            if piles_completed == len(piles):
                best_rate = mid_rate
                high_rate = mid_rate - 1
            else:
                low_rate = mid_rate + 1

        # print(high_rate)
        # print(low_rate)
        # print(mid_rate)
        # print(best_rate)
        return best_rate

        


                    


        