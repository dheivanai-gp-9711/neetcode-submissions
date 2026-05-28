class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l < r:
                sumo=nums[i]+nums[l]+nums[r]
                if sumo == 0:
                    if [nums[i],nums[l],nums[r]] not in result:
                        result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif sumo < 0:
                    l+=1
                else:
                    r-=1
        return result
        


        