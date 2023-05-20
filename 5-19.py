# 78. Subsets
    # My solution    
    class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            sols = []
            n = len(nums)
            current = []
            def backtrack(curr,start):
                sols.append(curr.copy())
                if (start == n):
                    return
                for i in range(start,n):
                    curr.append(nums[i])
                    backtrack(curr,i+1)
                    curr.pop()
            backtrack(current,0)
            return sols
# 90. Subsets II
    # My solution - not efficient could be done with hash map
    class Solution:
        def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            sols = []
            n = len(nums)
            current = []
            def backtrack(curr,start):
                if (curr in sols): return
                sols.append(curr.copy())
                if (start == n):
                    return
                for i in range(start,n):
                    curr.append(nums[i])
                    backtrack(curr,i+1)
                    curr.pop()
            backtrack(current,0)
            return sols

# 47. Permutations II
    # My solution
    class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            n = len(nums)
            sols = []
            freqs = Counter(nums)
            def backtrack(curr):
                if (len(curr) == n):
                    sols.append(curr.copy())
                    return
                for key in freqs:
                    if freqs[key]:
                        freqs[key]-=1
                        backtrack(curr + [key])
                        freqs[key]+=1
            backtrack([])
            return sols

# 39. Combination Sum
    # My solution
    class Solution:
        def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
            res=[]
            def backtracking(curr: List[int],i:int):
                s=sum(curr)
                if s==target:
                    res.append(curr)
                elif s<target:
                    for j in range(i,len(can)):
                        backtracking(curr+[can[j]],j)
            backtracking([],0)
            return res

# 40. Combination Sum II
    # My solution
    class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            def backtrack(start, path, target):
                if target == 0:
                    res.append(path)
                    return
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    if candidates[i] > target:
                        break
                    backtrack(i + 1, path + [candidates[i]], target - candidates[i])

            candidates.sort()
            res = []
            backtrack(0, [], target)
            return res

# 17. Letter Combinations of a Phone Number
    # My solution - easy to understand - maybe review?
    class Solution:
        def letterCombinations(self, digits: str) -> List[str]:
            mappings = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
            n = len(digits)
            if n==0: return []
            sols = []
            def backtrack(curr):
                # ex: 0
                l = len(curr)
                if (l == n):
                    sols.append(curr[:])
                else:
                    for c in mappings[digits[l]]:
                        backtrack(curr+c)

            backtrack("")
            return sols

# 22. Generate Parentheses
    # My solution
    class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            sols = []
            if n == 0: return sols
            def backtrack(curr,opened,closed):
                if (closed == n):
                    sols.append(curr[:])
                else:
                    if opened<n:
                        backtrack(curr+'(',opened+1,closed)
                    if closed<opened:
                        backtrack(curr+')',opened,closed+1)
            backtrack("",0,0)
            return sols
        
# 79. Word Search
    # My solution - potential project idea?
    class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            m = len(board)
            n = len(board[0])
            l = len(word)
            def dfs(i,j,nextindex):
                if (nextindex == l):
                    return True
                tmp = board[i][j]
                board[i][j] = -1
                for (a,b) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if a>=0 and a<m and b>=0 and b<n:
                        if board[a][b]==word[nextindex]:
                            if dfs(a,b,nextindex+1) == True: return True
                board[i][j] = tmp
                return False
            for y in range(m):
                for x in range(n):
                    if board[y][x] == word[0]:
                        if dfs(y,x,1) == True: return True
            return False

# 213. House Robber II
    # My solution
    class Solution:
        def rob(self, nums: List[int]) -> int:
            n = len(nums)
            if n==1: return nums[0]
            elif n==2 or n==3: return max(nums)

            def rob(l,r):
                oneback = 0
                twoback = 0
                for i in range(l,r+1):
                    temp = oneback
                    oneback = max(oneback,twoback+nums[i])
                    twoback = temp
                return oneback
            
            return max(rob(0,n-2),rob(1,n-1))
        
# 55. Jump Game
    # My solution
    class Solution:
        def canJump(self, nums):
            # Take curr variable to keep the current maximum jump...
            curr = nums[0]
            # Traverse all the elements through loop...
            for i in range(1,len(nums)):
                if curr == 0:
                    return False
                curr -= 1
                curr = max(curr, nums[i])
            return True
# 45. Jump Game II
    # My solution
    class Solution:
        def jump(self, nums: List[int]) -> int:
            n = len(nums)
            distance = [0 for j in range(n)]
            for i in range(n):
                maxreach = min(i+nums[i],n-1)
                for j in range(maxreach,0,-1):
                    if distance[j] != 0 and distance[j] < distance[i]+1:
                        break
                    distance[j] = distance[i]+1
            return distance[n-1]

# 62. Unique Paths    
    # My solution - beats 90+%!!
    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            arr = [[0 for _ in range(n)] for _ in range(m)]
            arr[0][0] = 1
            for i in range(m):
                for j in range(n):
                    # add above and left
                    if i!=0:
                        arr[i][j]+=arr[i-1][j]
                    if j!=0:
                        arr[i][j]+=arr[i][j-1]
            return arr[m-1][n-1]

