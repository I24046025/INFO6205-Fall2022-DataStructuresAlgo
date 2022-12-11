class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time complexity: O(n)
        # space complexity: O(n)

        # create a stack to store the index of invalid "(" and ")"
        stack = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
            
        for j in stack:
            s[j] = ""

        return "".join(s)