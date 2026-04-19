class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        i = 0  # child pointer
        
        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                i += 1  # child satisfied
        
        return i