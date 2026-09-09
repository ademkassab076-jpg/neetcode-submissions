class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ch=""
        a=0
        b=strs[0]
        for i in range(1,len(strs)):
            if len(b)>len(strs[i]):
                a=i
                b=strs[i]
        strs[a],strs[0]=strs[0],strs[a]
        for i in range(len(strs[0])):
            j=1
            test=True
            while j<len(strs) and test:
                if strs[0][i] != strs[j][i]:
                    test=False
                j+=1
            if test:
                ch+=strs[0][i]
            else:
                break
        return ch

