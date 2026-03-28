class Solution:
    def longestValidWord(self, words):
        # code here 
        trie={}
        for word in words:
            node=trie
            for ch in word:
                if ch not in node:
                    node[ch]={}
                node=node[ch]
            node["#"]=True
        res=""
        def dfs(node,path):
            nonlocal res
            if len(path)>len(res) or (len(path)==len(res) and path<res):
                res=path
            for ch in sorted(node.keys()):
                if ch!="#" and "#" in node[ch]:
                    dfs(node[ch],path+ch)
        dfs(trie,"")
        return res
