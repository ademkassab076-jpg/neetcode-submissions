class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        table=str.maketrans("",""," !\"#$%&'()*+,-./ :;<=>?@[\]^_`{|}~")
        s=s.translate(table)
        test=True
        i=0
        while i<len(s)//2 and test:
            test=s[i].upper()==s[len(s)-1-i].upper()
            i+=1
        return test
        """ 
        # let's try the two pointers approach 
        i,j=0,len(s)-1
        while i<j :
            while i<j and  not s[i].isalnum():
                i+=1
            while i<j and  not s[j].isalnum():
                j-=1
            if s[i].upper()!=s[j].upper():
                return False
            i+=1
            j-=1
        return True