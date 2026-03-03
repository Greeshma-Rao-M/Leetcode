class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left,right=0,0
        mpp=[-1]*256  #S.C:-O(N)
        maxLen=0
        while(right<n):  #T.C:-O(N)
          #shrink
            if(mpp[ord(s[right])]!=-1 and mpp[ord(s[right])]>=left):
                left=mpp[ord(s[right])]+1
            maxLen=max(maxLen,right-left+1)
            mpp[ord(s[right])]=right
            right+=1
        return maxLen
