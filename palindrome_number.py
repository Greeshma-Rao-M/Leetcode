class Solution:
    def isPalindrome(self, n: int) -> bool:
        s=0
        t=n
        while n>0:
            d=n%10
            s=s*10+d
            n=n//10
        if t==s:
            return True
        else:
            return False
