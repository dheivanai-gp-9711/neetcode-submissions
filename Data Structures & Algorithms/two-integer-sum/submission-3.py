class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #assume the input is sorted. no it is not
        # nums=sorted(nums)
        # l=0
        # r=len(nums)-1
        # while l<r:
        #     if nums[l]+nums[r] == target:
        #         return [l,r]
        #     elif nums[l]+nums[r] < target:
        #         l+=1
        #     else:
        #         r-=1
        map={}
        for i,num in enumerate(nums):
            if num in map:
                return [map[num], i]
            else:
                map[target-num] = i
        

        