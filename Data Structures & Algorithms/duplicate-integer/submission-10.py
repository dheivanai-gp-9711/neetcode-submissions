from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map=Counter(nums)
        return not all(count == 1 for count in map.values())
        # return any(count > 1 for count in map.values())
        # seen=set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        # map={}
        # l=0
        # for num in nums:
        #     if num in map:
        #         return True
        #         # map[num]+=1
        #     else:
        #         map[num]=1;
        #     l+=1
        # return False
        # nums=sorted(nums)
        # nums.sort()
        # l=0
        # r=1
        # while r<len(nums):
        #     if nums[l] != nums[r]:
        #         l+=1
        #         r+=1
        #     else:
        #         return True
        # return False
        # return len(nums) != len(set(nums))
        

        