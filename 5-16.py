# 994. Rotting Oranges - Medium
    # My solution - queue and BFS
    class Solution:
        def orangesRotting(self, grid: List[List[int]]) -> int:
            m,n=len(grid),len(grid[0])
            queue = deque()
            fresh = 0
            minutes = -1
            # go through all and add rotten to queue - minute 0
            for i,row in enumerate(grid):
                for j,cell in enumerate(grid[i]):
                    if cell == 1:
                        fresh += 1
                    elif cell == 2:
                        queue.append([i,j])
            # 
            while len(queue) > 0:
                size = len(queue)
                for i in range(size):
                    a,b = queue.popleft()
                    for r,c in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                        if (0<=r<m and 0<=c<n and grid[r][c]==1):
                            grid[r][c] = 2
                            fresh-=1
                            queue.append([r,c])
                minutes+=1
            if (fresh > 0): return -1
            if (minutes == -1): return 0
            return minutes
#21. Merge Two Sorted Lists
    # My solution
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # deal with nulls
            if list1 is None and list2 is None:
                return None
            elif list2 is None:
                return list1
            elif list1 is None:
                return list2
            
            if (list1.val < list2.val):
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            temp = head

            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            if list1:
                temp.next = list1
            else:
                temp.next = list2
            return head
        
# 206. Reverse Linked List
    # My solution - exlpicit stack - uses more space but less function calls
    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None: return None
            stack = deque()
            while head:
                stack.append(head)
                head = head.next
            
            newhead = stack.pop()
            temp = newhead
            while stack:
                temp.next = stack.pop()
                temp = temp.next
                temp.next = None
            return newhead
# 77. Combinations - Medium
    # My solution
    class Solution:
        def combine(self, n: int, k: int) -> List[List[int]]:
            # empty solution set
            sol = []
            def backtrack(remaining,currset,nextoption):
                if remaining==0:
                    sol.append(currset.copy())
                else:
                    for i in range(nextoption,n+1):
                        currset.append(i)
                        backtrack(remaining-1,currset,i+1)
                        currset.pop()

            backtrack(k,[],1)
            return sol
# 46. Permutations - Medium
    # My solution - using backtracking
    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            sols = []
            def backtrack(currset,remaining):
                if (len(remaining) == 0):
                    sols.append(currset.copy())
                else:
                    for i in range(len(remaining)):
                        currset.append(remaining.pop(i))
                        backtrack(currset,remaining)
                        remaining.insert(i,currset.pop())
            backtrack([],nums)
            return sols
# 784. Letter Case Permutation
    # My solution
    class Solution:
        def letterCasePermutation(self, s: str) -> List[str]:
            def backtrack(start,subset):
                if len(subset)==len(s):
                    res.append(subset[:])
                    return

                for i in range(start,len(s)):
                    if s[i].isdigit():
                        backtrack(i+1,subset+s[i])
                    else:
                        lower_subset = subset+s[i].lower()
                        backtrack(i+1,lower_subset)
                        upper_subset = subset+s[i].upper()
                        backtrack(i+1,upper_subset)
            res = []
            backtrack(0,"")
            return res

# 70. Climbing Stairs
    # My solution - dynamic programming
    class Solution:
        def climbStairs(self, n: int) -> int:
            if (n == 1): return 1
            elif (n==2): return 2
            lst = [0]*(n+1)
            lst[1] = 1
            lst[2] = 2
            for i in range(3,n+1):
                lst[i] = lst[i-1] + lst[i-2]
            return lst[n]

# 198. House Robber - Medium
    # My solution - dynamic programming
    class Solution:
        def rob(self, nums: List[int]) -> int:
            n = len(nums)
            if n == 1: return nums[0]
            elif n == 2: return max(nums)
            elif n == 3: return max(nums[2]+nums[0],nums[1])
            nums[2] += nums[0]
            for i in range(3,n):
                nums[i] += max(nums[i-2],nums[i-3])
            return max(nums[n-1],nums[n-2])
# 120. Triangle
    # My solution - pure genius
    class Solution:
        def minimumTotal(self, triangle: List[List[int]]) -> int:
            n = len(triangle)
            if (n == 1): return triangle[0][0]

            # start from second from bottom
            for i in range(n-2,-1,-1):
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            return triangle[0][0]