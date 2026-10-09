class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s=0
        i=0
        j=len(heights)-1
        while i<j :
            s=max(s,(j-i)*min(heights[i], heights[j]))
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return s
