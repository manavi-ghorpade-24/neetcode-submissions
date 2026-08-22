class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        mp = {}
        k = len(s1)
        uniqele = 0
        for i in range(k):
            mp[s1[i]] = mp.get(s1[i],0)
            if mp[s1[i]] == 0:
                uniqele += 1
            mp[s1[i]] += 1
        
        #slidinh window on s2
        i = 0
        j = 0
        while(j<len(s2)):
            if s2[j] in mp:
                mp[s2[j]] -= 1
                if mp[s2[j]] ==0:
                    uniqele -= 1

            if j-i+1 < k: #not window
                j += 1

            if j-i+1 ==k: # window

                if uniqele == 0:
                    return True
                    break
                
                if s2[i] in mp:
                    mp[s2[i]] += 1
                    if mp[s2[i]] == 1:
                        uniqele += 1
                j += 1
                i += 1
        return False



