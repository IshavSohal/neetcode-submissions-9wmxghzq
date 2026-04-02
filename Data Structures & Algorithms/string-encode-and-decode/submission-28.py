class Solution:

    def encode(self, strs: List[str]) -> str:

        if (len(strs) == 0):
            return 'NA'

        res = ""

        for str in strs:
            res += f"{len(str)}#{str}"

        print('encoded')
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        if (s == 'NA'):
            return []
        res = []
        length_index_start = 0
        length_index_end = s.find('#', length_index_start, len(s)) - 1
        word_index = length_index_end + 2


        while(0 <= length_index_start < len(s) and 0 <= length_index_end < len(s) and 0 < word_index < len(s)):
            print('length index start')
            print(length_index_start)
            print('length index end')
            print(length_index_end)
            print('word index')
            print(word_index)
            if(length_index_start == length_index_end):
                word_len = int(s[length_index_start])
            else:
                word_len = int(s[length_index_start:length_index_end+1])
            res.append(s[word_index: word_index+word_len])
            length_index_start = word_index+word_len
            length_index_end = s.find('#', length_index_start, len(s)-1) - 1
            word_index = length_index_end + 2

        print('test2')
        if (len(res) == 0):
            return [""]
        return res



        
            