class Solution:
    # def __init__(self):
    #     self.mini=float('inf')
    def jump(self, nums: List[int]) -> int:
        # dp=[[-1]*len(nums)]*len(nums)
        # dp=[-1]*len(nums)
        # return self.recurse(nums, 0, dp)
        
        
    # # self.mini=float('inf')
    # def recurse(self, nums: List[int], i: int, dp: List[int]):
    #     if i>= len(nums)-1:
    #         return 0
    #     if dp[i] != -1:
    #         return dp[i]
    #     mini=float('inf')
    #     for j in range(1, nums[i]+1):
    #         mini = min(mini, 1+self.recurse(nums, i+j, dp))
    #     dp[i] = mini
    #     # print(dp)
    #     return dp[i]
        dp=[float('inf')]*len(nums)
        dp[0]=0
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    dp[i+j]=min(dp[i]+1, dp[i+j])
        return dp[len(nums)-1]