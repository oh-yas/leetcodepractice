# 567. Permutation in String - Medium
    # My solution - O(n+j)
    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            temp = {}
            for c in s1:
                if c not in temp:
                    temp[c] = 1
                else:
                    temp[c] += 1
            
            for i,c in enumerate(s2):
                temp2 = temp.copy()
                if (len(s2)-i < len(s1)):
                    return False
                for j in range(len(s1)):
                    if s2[i+j] in temp2 and temp2[s2[i+j]] > 0:
                        temp2[s2[i+j]] -= 1
                    else:
                        break
                    if j == len(s1) - 1:
                        return True
            return False
    # Best Solution - using counters
    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            l1, l2 = len(s1), len(s2)
            if l1>l2: return False ## edge cases
            c1, c2 = Counter(s1), Counter(s2[:l1])
            for i in range(l2-l1):
                if c1==c2: return True
                char1, char2 = s2[i], s2[i+l1]
                c2[char1] -= 1 ## update counter c2
                if c2[char1]==0: 
                    del c2[char1]
                c2[char2] += 1
            return c1==c2

# 733. Flood Fill - Easy
    # My solution
    class Solution:
        def fill(self,image: List[List[int]], sr, sc, color, parent):
            if sr >= len(image) or sc >= len(image[0]) or sr < 0 or sc < 0:
                return
            if image[sr][sc] != parent: return
            image[sr][sc] = color
            self.fill(image,sr+1,sc,color,parent)
            self.fill(image,sr-1,sc,color,parent)
            self.fill(image,sr,sc+1,color,parent)
            self.fill(image,sr,sc-1,color,parent)

        def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            if (image[sr][sc] == color): return image
            self.fill(image,sr,sc,color,image[sr][sc])
            return image

# 695. Max Area of Island
    # My solution
    class Solution:
        def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            def dfs(row,col):
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) \
                    or grid[row][col] ==0:
                    return 
                grid[row][col] = 0
                a[0] += 1
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
                return a[0]
            maxarea = 0
            temparea = 0
            for i, row in enumerate(grid):
                for j,cell in enumerate(row):
                    if cell==1:
                        a = [0]
                        temparea = dfs(i,j)
                        if temparea > maxarea: maxarea = temparea
            return maxarea

# 617. Merge Two Binary Trees
    # My solution
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left,root2.left)
            root1.right = self.mergeTrees(root1.right,root2.right)
            return root1

# 116. Populating Next Right Pointers in Each Node - Medium
    # My solution BFS
    class Solution:
        def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
            if root is None: return root
            queue = [root]
            while queue:
                size = len(queue)
                for i in range(size):
                    currnode = queue.pop(0)
                    if (i < size - 1):
                        currnode.next = queue[0]
                    if currnode.left:
                        queue.append(currnode.left)
                    if currnode.right:
                        queue.append(currnode.right)
            return root
    # Best Solution - use next pointers for lower level
    class Solution:
        def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
            cur,nxt=root,root.left if root else None
            while cur and nxt:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                cur=cur.next
                if not cur:
                    cur=nxt
                    nxt=cur.left
            return root

# 542. 01 Matrix - Medium
    # My solution - using BFS and collections/queue
    class Solution:
        def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
            queue = deque()
            m = len(mat)
            n = len(mat[0])
            visited = [[0 for j in range(n)] for i in range(m)]
            distance = [[0 for j in range(n)] for i in range(m)]

            # find all 0s and add to queue
            for i,row in enumerate(mat):
                for j,cell in enumerate(mat[i]):
                    if cell==0:
                        visited[i][j] = 1
                        queue.append([i,j,0])
            
            while len(queue) != 0:
                a,b,dis = queue.popleft()
                for r,c in [(a,b-1),(a,b+1),(a-1,b),(a+1,b)]:
                    if 0<=r<m and 0<=c<n and visited[r][c]==0:
                        visited[r][c]=1
                        distance[r][c]=dis+1
                        queue.append([r,c,distance[r][c]])
            return distance