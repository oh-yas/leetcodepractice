# 72. Edit Distance - Hard
    # Solution - using DP - still need to understand
    class Solution:
        def minDistance(self, word1: str, word2: str) -> int:
            m = len(word2) + 1
            n = len(word1) + 1
            arr = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(1,m):
                arr[i][0] = i
            for j in range(1,n):
                arr[0][j] = j
            for i in range(1,m):
                for j in range(1,n):
                    if word2[i-1] == word1[j-1]:
                        # keep the string same as previo
                        arr[i][j] = min(arr[i-1][j-1],arr[i-1][j]+1,arr[i][j-1]+1)
                    else:
                        arr[i][j] = min(arr[i-1][j-1]+1,arr[i-1][j]+1,arr[i][j-1]+1)
            return arr[m-1][n-1]
        
# 322. Coin Change
    # DP + tabulation
    class Solution:
        def coinChange(self, coins: List[int], amount: int) -> int:
            dp=[sys.maxsize] * (amount+1)
            dp[0]=0
            
            for coin in coins:
                for i in range(coin, amount+1):
                    if i-coin>=0:
                        dp[i]=min(dp[i], dp[i-coin]+1)
            
            return -1 if dp[-1]==sys.maxsize else dp[-1]

# 343. Integer Break
    # Solution with DP
    class Solution:
        def integerBreak(self, n: int) -> int:
            dp = [-1] * (n+1)
            #add dp-base!
            dp[1] = 1
        
            #this problem has only one state parameter: the given number to start decomposing           #from!
            #Bottom-Up
            for i in range(2, n+1, 1):
                upper_bound = (i // 2) + 1
                #iterate through all possible pairs!
                for j in range(1, upper_bound, 1):
                    #current pair (j, i-j), which we probably already solved its subproblems!
                    first = max(j, dp[j])
                    second = max(i-j, dp[i-j])
                    #get product for current pair!
                    sub_ans = first * second
                    #compare current pair's product against built up answer maximum!
                    dp[i] = max(dp[i], sub_ans)
        
            #then, once we are done, we can return dp[n]!
            return dp[n]

# 149. Max Points on a Line - Hard
    # My solution - calculate slopes from each point and hash them
    class Solution:
        def maxPoints(self, points: List[List[int]]) -> int:
            points.sort()
            maximum = 0
            n = len(points)
            for i in range(n):
                slopes = []
                for j in range(i+1,n):
                    if (points[j][0] - points[i][0]) == 0:
                        slopes.append("NO")
                    else:
                        slopes.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))
                if len(slopes) > 0:
                    test_list = Counter(slopes)
                    res = test_list.most_common(1)[0][1]
                    if res > maximum:
                        maximum = res
            return maximum +1