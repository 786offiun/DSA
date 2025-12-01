class Solution(object):
    def countNegatives(self, grid):
        counter=0
        for i in grid:
            for j in i:
                if j<0:
                    counter+=1
        return counter

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        