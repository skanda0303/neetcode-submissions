class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        count = 0
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1

            while (i-start+1)- max(freq.values()) > k:
                freq[s[start]]-=1
                start+=1
                
            count = max(count,i-start+1)

        return count
