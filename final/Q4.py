class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # time complexity: O(m * n)
        # space complexity: O(m * n)

        # currentPaths = topPaths + leftPaths 
        # Set the location to 0 to block path from top and left
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0]*n for elem in range(m)]

        # If source is blocked then no paths available else 1 for source
        if(obstacleGrid[0][0] == 1):
            return 0
        else:
            memo[0][0] = 1

        # If i == 0 and j == 0 continue for not setting up memo[i][j] to 0
        # If obstacle presents then remains the current position as 0 else curr = left + top
        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    continue
                if(obstacleGrid[i][j] != 1):
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return(memo[-1][-1])