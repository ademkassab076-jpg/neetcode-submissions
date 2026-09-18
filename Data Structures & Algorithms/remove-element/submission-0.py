class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nb=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[nb]=nums[i]
                nb+=1
        return nb  