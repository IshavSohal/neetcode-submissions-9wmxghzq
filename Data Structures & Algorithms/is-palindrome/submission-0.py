import re

class Solution:

    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^a-zA-Z0-9]','',s.lower().replace(" ", ""))
        front = 0
        back = len(new_s) - 1
        print(new_s)

        while front <= back:
            if new_s[front] != new_s[back]:
                return False
            front += 1
            back -= 1

        return True
        