from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups={}
        # for s in strs:
        #     key=''.join(sorted(s))
        #     groups.setdefault(key,[]).append(s)
        # return list(groups.values())
        # result=defaultdict(list)
        # for s in strs:
        #     count=[0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')] +=1
        #     result[tuple(count)].append(s)
        # return list(result.values())

        result={}
        for s in strs:
            count=Counter(sorted(s))
            print(count)
            key=tuple(count.items())
            print(key)
            result.setdefault(key,[]).append(s)
        
        return list(result.values())


