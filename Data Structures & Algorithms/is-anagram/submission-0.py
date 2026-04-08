class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = {},{}
        for a in s:
            if a not in s1:
                s1[a] = 1
            else:
                s1[a]+=1
        for b in t:
            if b not in t1:
                t1[b] = 1
            else:
                t1[b]+=1
        return s1 == t1
    