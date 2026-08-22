class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        mp = {}
        unique = 0
        res = [-1,-1]
        reslen = float('inf')
        for i in range(len(t)):
            mp[t[i]] = mp.get(t[i],0)+1
            if mp[t[i]] == 1:
                unique += 1

        i=0
        j=0   
        while(j<len(s)):
            if s[j] in mp:
                mp[s[j]] -= 1 #reduce count coz we found it
                if mp[s[j]] == 0: #basically we got all count
                    unique -= 1 #reduce because 1 element is found in substr
            
            while unique == 0: #found all ele , make window short
                if j-i+1<reslen: #new short sub
                    res = [i,j]
                    reslen = j-i+1
                if s[i] in mp: #if char is in mp/t
                    mp[s[i]] += 1
                    if mp[s[i]] == 1:
                        unique +=1
                i+=1
            j += 1
        if reslen != float('inf'):
            return s[res[0]:res[1]+1]
        return ""
        
