class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        start=[]
        for num in numset:
            if num-1 not in numset:
                start.append(num)
        print(start)
        # return start[0]
        count=1
        maxi = 0
        for s in start:
            while s+count in numset:
                count+=1
            maxi=max(maxi, count)
            count=1
        return maxi