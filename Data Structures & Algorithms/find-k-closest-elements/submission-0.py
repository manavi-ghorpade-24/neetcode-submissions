class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1

        while(r-l+1 >k): #entire array
            dt1 = abs(arr[l]-x)
            dt2 = abs(arr[r]-x)
            if dt1>dt2:
                l+= 1
            else: #for equal and dt1<st2
                r -= 1
        
        return arr[l:r+1]
                
