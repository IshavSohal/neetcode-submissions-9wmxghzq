class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sequences = {}
        start = 0
        end = 0
        seq_char = s[start]
        max_sequence = 0

        for i in range(1, len(s)):
            if s[i] == s[start]:
                end += 1
            else:
                # For each sequence corresponding to the letter of the current sequence
                # if there exists a sequence whose end index is at most <extension> characters
                # less than the current sequence's start index (where <extension> is the #
                # of extension characters left for that previous sequence), then we extend the 
                # previous sequence
                if seq_char not in sequences:
                    sequences[seq_char] = []
                for j, prev_seq in enumerate(sequences[seq_char]):
                    seq_gap = start - prev_seq[1] - 1 # gap between previous and current sequence
                    extension_chars = k - prev_seq[2]
                    if seq_gap <= extension_chars:
                        sequences[seq_char][j] = (prev_seq[0], end, prev_seq[2] + seq_gap)
            
                sequences[seq_char].append((start, end, 0)) # Add the current sequence by itself as well

                start = i
                end = i
                seq_char = s[start]

        # Checking the final sequence
        if seq_char not in sequences:
            sequences[seq_char] = []
        for j, prev_seq in enumerate(sequences[seq_char]):
            seq_gap = start - prev_seq[1] - 1 # gap between previous and current sequence
            extension_chars = k - prev_seq[2]
            if seq_gap <= extension_chars:
                sequences[seq_char][j] = (prev_seq[0], end, prev_seq[2] + seq_gap)

        sequences[seq_char].append((start, end, 0)) # Add the current sequence by itself as well

        # For each character, find its longest sequence. Return the length of the longest substring
        for char in sequences:
            for seq in sequences[char]:
                length = seq[1] - seq[0] + 1
                extension_chars = min(k - seq[2], len(s) - length)
                length += extension_chars
                
                if length > max_sequence:
                    max_sequence = length

        return max_sequence

        