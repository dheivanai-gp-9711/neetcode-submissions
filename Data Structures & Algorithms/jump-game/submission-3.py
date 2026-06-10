class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                # if maxi > i:
                #     continue
                # else:
                return False
            # for j in range(1, nums[i]+1):
            #     if i+j >= len(nums)-1:
            #         return True
            maxi=max(maxi, i+nums[i])
            print(maxi)
            # if maxi > len(nums)-1:
            #     return True
        return True

