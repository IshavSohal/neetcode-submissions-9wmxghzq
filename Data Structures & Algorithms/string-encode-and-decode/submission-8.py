class Solution:
    

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "é"
        return "é".join(strs)

    def decode(self, s: str) -> List[str]:
        if (s == 'é'):
            return []
        return s.split("é")