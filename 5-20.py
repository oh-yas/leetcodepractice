# 5. Longest Palindromic Substring
    # Solution 1 - faster
    def longestPalindrome(self, s: str) -> str:
            def lp(s,l,r):
                n=len(s)
                while l>=0 and r<n and s[l]==s[r]:
                    l-=1
                    r+=1
                return l+1,r
            start=end=0
            for i in range(len(s)):
                l,r=lp(s,i,i)
                if (r-l)>(end-start):
                    start=l
                    end=r
                l,r=lp(s,i,i+1)
                if (r-l)>(end-start):
                    start=l
                    end=r
            return s[start:end]
    # Solution 2 - slower
    def longestPalindrome(self, s):
            longest_palindrom = ''
            dp = [[0]*len(s) for _ in range(len(s))]
            #filling out the diagonal by 1
            for i in range(len(s)):
                dp[i][i] = True
                longest_palindrom = s[i]
                
            # filling the dp table
            for i in range(len(s)-1,-1,-1):
                    # j starts from the i location : to only work on the upper side of the diagonal 
                for j in range(i+1,len(s)):  
                    if s[i] == s[j]:  #if the chars mathces
                        # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                        #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                        if j-i ==1 or dp[i+1][j-1] is True:
                            dp[i][j] = True
                            # we also need to keep track of the maximum palindrom sequence 
                            if len(longest_palindrom) < len(s[i:j+1]):
                                longest_palindrom = s[i:j+1]
                    
            return longest_palindrom
    # My solution:
    class Solution:
        def longestPalindrome(self, s):
            start,end = 0,0
            l,r = 0,0
            n = len(s)
            def lp(l,r):
                while l>=0 and r<n and s[l]==s[r]:
                    l-=1
                    r+=1
                return l+1,r
            for i in range(n):
                l,r = lp(i,i)
                if r-l > end-start:
                    end = r
                    start = l
                l,r = lp(i,i+1)
                if r-l > end-start:
                    end = r
                    start = l
            return s[start:end] 

# 413. Arithmetic Slices
    # My solution - doesn't use dp
    class Solution:
        def numberOfArithmeticSlices(self, nums: List[int]) -> int:
            n = len(nums)
            queue=deque()
            commondiff = 0
            numsubarrays = 0
            for i in range(n):
                if not queue:
                    queue.append(nums[i])
                    commondiff = nums[i]
                elif (queue[-1]+commondiff) != nums[i]:
                    temp = queue[-1]
                    queue.clear()
                    queue.append(temp)
                    queue.append(nums[i])
                    commondiff = nums[i] - temp
                else:
                    queue.append(nums[i])
                if len(queue) >= 3:
                    numsubarrays += len(queue)-2
            return numsubarrays
    # Best solution: uses dp - checks previous two elements and adds to prev numbers
    class Solution:
        def numberOfArithmeticSlices(self, A: List[int]) -> int:
            le=len(A)
            l=[0]*(le)
            for i in range(2,le):
                if A[i]-A[i-1] == A[i-1]-A[i-2]:
                    l[i]=1+l[i-1]
            return sum(l)

# 91. Decode Ways
    # My solution - found fibinacci
    class Solution:
        def numDecodings(self, s: str) -> int:
            if s[0] == '0':
                return 0
            n = len(s)
            dp = [0 for _ in range(n + 1)]
            # base case
            dp[0] = 1
            for i in range(1, n + 1):
                if s[i - 1] != '0':
                    dp[i] = dp[i - 1]
                if i >= 2:
                    x = int(s[i - 2: i])
                    if 10 <= x <= 26:
                        dp[i] += dp[i - 2]
            return dp[n]

# 139. Word Break
    # My solution - takes too long to figure out false or not
    class Solution:
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            h = [0]
            heap = heapify(h)
            n = len(s)
            a = 0
            wordDict.sort(reverse=True,key=len)
            while h:
                i = -heappop(h)
                for word in wordDict:
                    a += 1
                    if a>10000: return False
                    nextindex = len(word) + i
                    if nextindex > n: continue
                    if s[i:nextindex] == word:
                        heappush(h,-nextindex)
                        if nextindex == n:
                            return True
            return False
    # Best solution - uses dynamic programming
    class Solution:
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(1, len(s) + 1):
                # check each word in wordDict rather than iterating from 0 to i
                for word in wordDict:
                    if len(word) > i:
                        continue
                    if s[i - len(word):i] == word and dp[i - len(word)]:
                        dp[i] = dp[i - len(word)]
                        break
            return dp[len(s)]  

# 300. Longest Increasing Subsequence
    # My solution - uses DP but n^2
    class Solution:
        def lengthOfLIS(self, nums: List[int]) -> int:
            n = len(nums)
            # count how many numbers before it are smaller
            lengths = [1]*n
            for i in range(1,n):
                for j in range(i-1,-1,-1):
                    if nums[i]>nums[j] and lengths[i]<=lengths[j]:
                        lengths[i] = lengths[j] + 1
            return max(lengths)
# 673. Number of Longest Increasing Subsequence
    # My solution
    class Solution:
        def findNumberOfLIS(self, nums: List[int]) -> int:
            if not nums: return 0
            n = len(nums)
            m, dp, cnt = 0, [1] * n, [1] * n
            for i in range(n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        if dp[i] < dp[j]+1: dp[i], cnt[i] = dp[j]+1, cnt[j]
                        elif dp[i] == dp[j]+1: cnt[i] += cnt[j]
                m = max(m, dp[i])                        
            return sum(c for l, c in zip(dp, cnt) if l == m)

#1143. Longest Common Subsequence
    # Solution, using dp and starting from back
    class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
            for i in range(len(text1)-1,-1,-1):
                for j in range(len(text2)-1,-1,-1):
                    if text1[i]==text2[j]:
                        dp[i][j]=1+dp[i+1][j+1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j+1])
            return dp[0][0]

# 583. Delete Operation for Two Strings
    # My solution
    class Solution:
        def minDistance(self, word1: str, word2: str) -> int:
            dp=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
            for i in range(len(word1)-1,-1,-1):
                for j in range(len(word2)-1,-1,-1):
                    if word1[i]==word2[j]:
                        dp[i][j]=1+dp[i+1][j+1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j+1])
            return len(word2) + len(word1) - dp[0][0]*2