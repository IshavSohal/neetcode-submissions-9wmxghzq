class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            alphabetArray = tuple(self.getAlphabetArray(s))
            if alphabetArray in anagrams:
                anagrams[alphabetArray].append(s)
            else:
                anagrams[alphabetArray] = [s]

        
        return list(anagrams.values())
            
    def getAlphabetArray(self, s):
        alphabet = [0] * 26

        for letter in s:
            index = ord(letter) - ord('a') - 1
            alphabet[index] += 1
        
        return alphabet