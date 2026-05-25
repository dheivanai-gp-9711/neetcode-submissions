class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stringbuilder=[]
        # for c in s:
        #     if c.isalnum():
        #         stringbuilder.append(c.lower())
        s=''.join(c.lower() for c in s if c.isalnum())
        # print(''.join(stringbuilder))
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True


