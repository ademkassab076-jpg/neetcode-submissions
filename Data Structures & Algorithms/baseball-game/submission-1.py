class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]#we define an empty list for all the operations 
        for x in operations:
            match x:#we will try all the cases
                case "+":
                    lst.append(lst[-2]+lst[-1])
                case "C":
                    lst.pop(-1)
                case "D":
                    lst.append((lst[-1])*2)
                case _:
                    lst.append(int(x))
        return sum(lst)
