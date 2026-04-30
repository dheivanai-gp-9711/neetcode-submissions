from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(s)
        # t=sorted(t)
        # return s==t
        # set1=set(s)
        # for c in t:
        #     if c not in set1:
        #         return False
        # return True
        map1=Counter(s)
        for c in t:
            if c in map1:
                # map1[c]-=1
                # if map1[c] == 0:
                #     del map1[c]
                if map1[c] == 1:
                    del map1[c]
                else:
                    map1[c]-=1
            else:
                return False
        # return len(map1) == 0
        print(map)
        return not map1
        # if len(s) != len(t):
        #     return False
        # map1=Counter(s)
        # map2=Counter(t)
        # if len(map1.keys()) != len(map2.keys()):
        #     return False
        # return map1 == map2