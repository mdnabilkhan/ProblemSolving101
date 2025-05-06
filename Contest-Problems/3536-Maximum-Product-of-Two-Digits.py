class Solution:
    def maxProduct(self, n: int) -> int:
        ans=1
        maxx=0
        lst=list(map(int,str(n)))
        lst.sort()
        return lst[len(lst)-1]*lst[len(lst)-2]
        