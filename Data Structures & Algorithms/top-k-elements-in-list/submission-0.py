from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for x in nums:
            d[x]+=1
        lst=[]
        for i in range(k):
            s=max(d, key=d.get)#retourne la clé
            lst.append(s)
            d[s]=0

        return lst

            
        