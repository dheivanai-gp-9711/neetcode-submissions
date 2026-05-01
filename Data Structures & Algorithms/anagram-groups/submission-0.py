class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for s in strs:
            key=sorted(s)
            # print(key)
            key=''.join(key)
            # print(key)
            # print(s)
            if key not in map:
                li=list()
                li.append(s)
                map[key]=li
            else:
                li=map[key]
                li.append(s)
                map[key]=li
        result=[]
        for li in map.values():
            result.append(li)
        return result

