class Solution:
    def test(self , lst):
        nb=0
        for i in range(len(lst)):
            if lst[i]!=0:
                nb+=1
            if nb>=2:
                return False
        return nb==1
    def lastStoneWeight(self, stones: List[int]) -> int:
        while not self.test(stones) and sum(stones)>0:
            a=max(stones)
            for i in range(len(stones)):
                if stones[i]==a:
                    stones[i]=0
                    break
            b=max(stones)
            for j in range(len(stones)):
                if stones[j]==b:
                    break
            if a>b:
                a=a-b
                b=0
            elif a==b:
                a=b=0
            else:
                b=b-a
                a=0
            stones[i]=a
            stones[j]=b
        return sum(stones)