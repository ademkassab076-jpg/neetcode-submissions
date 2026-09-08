class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=len(strs[0])
        b=0
        for i in range(1,len(strs)):
            if len(strs[i])<a:
                b=i
                a=len(strs[i])
        strs[0],strs[b]=strs[b],strs[0]
        ch=""
        for i in range (len(strs[0])):
            test=True 
            j=1
            while j<len(strs) and test :
                test=strs[0][i]==strs[j][i]
                j+=1
            if test:
                ch+=strs[0][i]
            else:
                break
        return ch 