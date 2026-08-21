class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #basically going to change the less frequent element
        # l = 0
        # maxf = 0
        # hashmap = {}
        # res  = 0
        # for r in range(len(s)):
        #     hashmap[s[r]] = 1 + hashmap.get(s[r],0) #add element update count
        #     maxf = max(maxf, hashmap[s[r]]) #check if its maximum frequency

        #     if (r-l+1 - maxf <= k): # length - max freq <= k -> then we can change
        #         res = max(res, r-l+1)
            
        #     while(r-l+1 - maxf > k): #until we get normal string
        #         hashmap[s[l]] -= 1
        #         l+=1
        #     res = max(res, r-l+1)
        # return res
        
        # for r in range(len(s)):
        #     hashmap[s[r]] = 1+hashmap.get(s[r],0)
        #     while(r-l+1 - max(hashmap.values()) >k):
        #         hashmap[s[l]] -=1
        #         l+=1
        #     res = max(res, r-l+1)
        # return res

        l = 0
        r = 0
        maxf = 0
        mp ={}
        res = 0
        while(r<len(s)):
            mp[s[r]] = mp.get(s[r],0) + 1
            maxf = max(maxf, mp[s[r]])

            if (r-l+1 - maxf <= k): #valid window
                res = max(res, r-l+1)
            
            while(r-l+1-maxf > k):
                mp[s[l]] -=1
                l+=1
            res =max(res, r-l+1)
            r += 1
        return res



#AAABABAAAAA
        