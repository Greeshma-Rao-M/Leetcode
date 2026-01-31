class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l = 0
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        count = 0
        ml = float('inf')
        start = -1
        
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    count += 1
                freq[s[r]] -= 1
            
            while count == len(t):
                if r - l + 1 < ml:
                    ml = r - l + 1
                    start = l
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        count -= 1
                l += 1
        
        return s[start:start+ml] if ml != float('inf') else ""
