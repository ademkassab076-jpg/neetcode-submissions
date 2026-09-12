class Solution:
    def isPalindrome(self, s: str) -> bool:
        table=str.maketrans("",""," !\"#$%&'()*+,-./ :;<=>?@[\]^_`{|}~")
        s=s.translate(table)
        test=True
        i=0
        while i<len(s)//2 and test:
            test=s[i].upper()==s[len(s)-1-i].upper()
            i+=1
        return test