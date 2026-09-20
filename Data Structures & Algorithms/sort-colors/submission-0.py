class Solution:
    def nb(self, nums: list[int], color:int) -> int:
        count=0
        for x in nums:
            if x==color:count+=1
        return count
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]= [0] * self.nb(nums,0)+[1] * self.nb(nums,1)+[2] * self.nb(nums,2)
