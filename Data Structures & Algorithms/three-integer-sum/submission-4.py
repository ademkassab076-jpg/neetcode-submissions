class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[j]+nums[k]<-nums[i]:
                    j+=1
                elif nums[j]+nums[k]==-nums[i] and [nums[i],nums[j],0-nums[i]-nums[j]] not in lst:
                    lst.append([nums[i],nums[j],nums[k]])
                else:
                    k-=1
        return lst