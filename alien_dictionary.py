class Solution:
    def findOrder(self, words):
        # code here
        adj={}
        indegree={}
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch]=[]
                if ch not in indegree:
                    indegree[ch]=0
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            ml=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:ml]==w2[:ml]:
                return ""
            for j in range(ml):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        indegree[w2[j]]+=1
                    break
        q=[]
        for c in indegree:
            if indegree[c]==0:
                q.append(c)
        res=[]
        f=0
        while f<len(q):
            char=q[f]
            f+=1
            res.append(char)
            for nei in adj[char]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(res)!=len(indegree):
            return ""
        return "".join(res)
