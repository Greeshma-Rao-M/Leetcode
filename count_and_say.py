class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prev="1"
        for _ in range(2,n+1):
            res=""
            count=1
            for i in range(1,len(prev)):
                if prev[i]==prev[i-1]:
                    count+=1
                else:
                    res+=str(count)+prev[i-1]
                    count=1
            res+=str(count)+prev[-1]
            prev=res
        return prev

#using recursion
def rec(arr,idx=0):
    if idx==len(arr-1):
        return arr[idx],arr[idx]
    min1,max1=rec(arr,idx+1)
    curr=arr[idx]
    return min(curr,min1),max(curr,max)
min,max=rec(arr)
