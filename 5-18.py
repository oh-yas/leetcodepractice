# 11. Container With Most Water - Medium
    # My solution - BEATS 95%!!!!
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            n = len(height)
            i = 0
            j = n-1
            maxarea = 0

            while (i<j):
                if (height[i]<height[j]):
                    minindex,maxindex = i,j
                elif (height[i]>height[j]):
                    minindex,maxindex = j,i
                elif (height[i+1]>height[j-1]):
                    minindex,maxindex = j,i
                else:
                    minindex,maxindex = i,j
                
                temparea = height[minindex]*(j-i)
                maxarea = temparea if temparea>maxarea else maxarea
                if minindex == i: i+=1
                else: j -= 1
            
            return maxarea
# 438. Find All Anagrams in a String - Medium
    # My solution - counters and dict compare
    class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            string = Counter(p)
            sols = []
            for i in range(len(s)-len(p)+1):
                temp = Counter(s[i:i+len(p)])
                if string == temp:
                    sols.append(i)
            return sols

# 209. Minimum Size Subarray Sum
    # My solution - sliding window
    class Solution:
        def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            n = len(nums)
            if n == 0: return 0
            elif target == 0: return 1
            sum = 0
            j = 0
            toreturn = n+1
            for i in range(n):
                sum += nums[i]
                while (sum >= target):
                    if (i-j+1) < toreturn: toreturn = (i-j+1)
                    sum -= nums[j]
                    j += 1
            if toreturn == n+1: return 0
            return toreturn

# 200. Number of Islands
    # My solution - DFS and O(1) space        
    class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            m,n= len(grid),len(grid[0])
            numislands = 0

            def DFS(i,j):
                if i < 0 or i >= m or j < 0 or j >= n: return
                elif grid[i][j] != "1": return
                grid[i][j] = "0"
                for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    DFS(a,b)
                return

            for i in range(m):
                for j,cell in enumerate(grid[i]):
                    if (cell == "1"):
                        DFS(i,j)
                        numislands += 1
            
            return numislands
# 117. Populating Next Right Pointers in Each Node II
    # My solution - BFS and queue
    class Solution:
        def connect(self, root: 'Node') -> 'Node':
            if root is None: return None
            queue = deque()
            queue.append(root)
            while queue:
                size = len(queue)       
                for i in range(size):
                    temp = queue.popleft()
                    temp.next = queue[0] if i<size-1 else None
                    if temp.left: queue.append(temp.left)
                    if temp.right: queue.append(temp.right)
            return root

# 1091. Shortest Path in Binary Matrix - Medium
    # My solution - beats 93%!!
    class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0: return -1
        grid[0][0] = -1
        queue = deque()
        queue.append([0,0])
        while queue:
            size = len(queue)
            for i in range(size):
                a,b = queue.popleft()
                for c,d in [(a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b+1)]:
                    if c>=0 and c<n and d>=0 and d<n:
                        if grid[c][d] == 0:
                            grid[c][d] = grid[a][b] - 1
                            queue.append([c,d])
        if grid[n-1][n-1] == 0: return -1
        return -grid[n-1][n-1]

# 130. Surrounded Regions
# My solution - "Unique approach" - not cache efficient
    class Solution:
        def solve(self, board: List[List[str]]) -> None:
            """
            Do not return anything, modify board in-place instead.
            """
            m = len(board)
            n = len(board[0])

            def dfs(i,j):
                if i<0 or i>=m or j<0 or j>=n:
                    return
                if visited[i][j] == 1: return
                if board[i][j] != 'O': return
                visited[i][j] = 1
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    dfs(a,b)

            visited = [[0 for j in range(n)] for i in range(m)]
            # we need to go around edges - BFS on edge pieces - set visited = 1
            # top
            for i,cell in enumerate(board[0]):
                if cell == 'O' and visited[0][i] == 0:
                    dfs(0,i)
            # bottom
            for i,cell in enumerate(board[m-1]):
                if cell == 'O' and visited[m-1][i] == 0:
                    dfs(m-1,i)
            # left
            for i in range(m):
                if board[i][0] == 'O' and visited[i][0] == 0:
                    dfs(i,0)
            # right
            for i in range(m):
                if board[i][n-1] == 'O' and visited[i][n-1] == 0:
                    dfs(i,n-1)
            
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O' and visited[i][j] == 0:
                        board[i][j] = 'X'

# 797. All Paths From Source to Target
# My solution - over complicated, but efficient
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sols = []
        n = len(graph)
        remaining = [1 for j in range(n)]
        zero = [0 for j in range(n)]
        def backtrack(curr,rem):
            if curr[-1] == n-1:
                sols.append(curr.copy())
            elif rem != 0:
                for i in range(len(graph[curr[-1]])):
                    nextindex = graph[curr[-1]][i]
                    if rem[nextindex] == 1:
                        curr.append(nextindex)
                        rem[nextindex] = 0
                        backtrack(curr,rem)
                        rem[nextindex] = 1
                        curr.pop()
            return
        current = [0]
        remaining[0] = 0
        backtrack(current,remaining)
        return sols
    # Best solution - same logic but simplified
    class Solution:
        def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            target = len(graph) - 1
            paths, targets = [[0]], []
            while paths:
                path = paths.pop(0)
                edges = graph[path[-1]]
                if not edges: 
                    continue
                for edge in edges:
                    if edge==target:
                        targets.append(path+[edge])
                    else:
                        paths = [path+[edge]] + paths
            return targets  