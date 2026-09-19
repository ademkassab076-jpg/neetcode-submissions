class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        test=True
        while test:
            test=False
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    test=True
        return nums