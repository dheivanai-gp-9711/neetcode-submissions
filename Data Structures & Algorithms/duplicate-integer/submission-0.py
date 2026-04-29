class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        l=0
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
            l+=1
        return l != len(map.keys())
        

        