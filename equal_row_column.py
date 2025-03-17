class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column = []
        inside = []
        first = 0
        length = len(grid[first])
        count = 0
        copy = []
        j = 0
        i = 0
        walker = grid[0]
        while(i < length):
            inside.append(walker[i])
            j+=1
            if j == len(grid) and len(inside) == length :
                i+=1
                j = 0
                copy = inside[:]
                column.append(copy)
                inside[:] = ''
            walker = grid[j]
        for i in column:
            for j in grid:
                if i == j:
                    count+=1
        return count