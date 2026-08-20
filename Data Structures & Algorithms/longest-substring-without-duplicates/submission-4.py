class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        st = set()
        longest = 0
        while(j<len(s)):   
            while s[j] in st:
                st.discard(s[i])
                i+=1
            st.add(s[j])
            longest = max(longest,(j-i)+1)
            j+=1
        return longest


        