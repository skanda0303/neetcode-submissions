class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end=0
        s1 = set()
        maxlen = 0
        while end < len(s):
            if s[end] in s1:
                while s[end] in s1:
                    s1.remove(s[start])
                    start+=1
                    
            s1.add(s[end])
            maxlen = max(maxlen,end-start+1)
            end+=1
        return maxlen
            
