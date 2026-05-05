class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # leftProd = [1]*len(nums)
        # rightProd = [1]*len(nums)
        res=[1]*len(nums)
        # count=0
        # if nums[0] == 0:
        #     count+=1
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
            # if nums[i-1] != 0:
                # leftProd[i] = leftProd[i-1]*nums[i-1]
            # if nums[i] == 0:
            #     count+=1
        # if count > 1:
        #     return [0]*len(nums)
        # print(leftProd)

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
            # if nums[i+1] != 0:
                # rightProd[i] = rightProd[i+1] * nums[i+1]
            # else:
            #     flag=True
        # print(rightProd)
        # res=[0]*len(nums)
        # # print(count)
        # for i in range(len(nums)):
        #     # if ((count>0 and nums[i] == 0) or (count == 0)):
        #         res[i]=leftProd[i]*rightProd[i]
        return res


            