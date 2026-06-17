import asyncio
from collections import deque

class Solution:
    async def orangesRotting(self, grid):
        q = deque()
        fresh = 0
        minutes = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            count = len(q)

            for _ in range(count):
                r, c = q.popleft()

                if r + 1 < rows and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    q.append((r + 1, c))

                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    q.append((r - 1, c))

                if c + 1 < cols and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    q.append((r, c + 1))

                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    q.append((r, c - 1))

            minutes += 1
            await asyncio.sleep(0)

        if fresh == 0:
            return minutes
        return -1


grid = [[2,1,1],[1,1,0],[0,1,1]]

obj = Solution()
print(asyncio.run(obj.orangesRotting(grid)))