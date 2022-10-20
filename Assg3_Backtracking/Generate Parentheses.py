class Solution:
    def generateParenthesis(self, n):
        res = []
        stack = [("(",n-1,n)]
        
        while stack:
            item = stack.pop()
            
            s = item[0]
            o = item[1]
            c = item[2]
            
            if o == 0 and c == 0:
                res.append(s)
            else:
                if o != 0:
                    stack.append([s+"(",o-1,c])
                
                if o < c:
                    stack.append([s+")",o,c-1])

        return res