# 167. Two Sum II - Input Array Is Sorted - Medium
    # My solution - binary search
    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            lngth = len(numbers)
            for i in range(lngth-1):
                target2 = target - numbers[i]
                if target2 == numbers[i]:
                    if (numbers[(i+1)%lngth] == target2):
                        return [i+1,i+2]
                # now binary search for target 2
                l = i+1
                r = lngth-1
                while (l<=r):
                    mid = (l+r)//2
                    if (numbers[mid] == target2):
                        return [i+1,mid+1]
                    elif (numbers[mid] > target2):
                        r = mid-1
                    elif (numbers[mid] < target2):
                        l = mid+1
            return [0,0]
    # Best Solution - hash table
    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            dic={}
            for key,val in enumerate(nums):
                if val in dic:
                    return dic[val],key
                else:
                    dic[target-val]=key



# 557. Reverse Words in a String III - Easy
    # My Solution - State machine
    class Solution:
        def reverseWords(self, s: str) -> str:
            temp = ""
            retstring = ""
            for c in s:
                if (c != ' '):
                    temp += c
                else:
                    temp = "".join(reversed(temp))
                    retstring += temp
                    retstring += ' '
                    temp = ""
            temp = "".join(reversed(temp))
            retstring += temp

            return retstring
    # Best Solution - split method
    class Solution:
        def reverseWords(self, s: str) -> str:
            new = s.split()
            for x, item in enumerate(new):
                new[x] = item[::-1]
            return ' '.join(new)

# 977. Squares of a Sorted Array - Easy
    # My solution - countingsort for O(n)
    class Solution:
        def sortedSquares(self, nums: List[int]) -> List[int]:

            count = max(max(nums),-min(nums))
            countingsort = [0]*(count+1)
            returnlist = []
            for n in nums:
                countingsort[abs(n)] += 1
            for i in range(count+1):
                while countingsort[i] != 0:
                    returnlist.append(i*i)
                    countingsort[i] -= 1
            return returnlist
        
# 283. Move Zeroes - Easy
    # My solution - two pointers
    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            for i in range(len(nums)):
                # i is in parent array, j finds next nonzero
                j = i
                if nums[i] == 0:
                    while j < len(nums) - 1 and nums[j] == 0 :
                        j+=1
                    nums[i],nums[j] = nums[j],nums[i]


# 876. Middle of the Linked List - Easy
    # My solution - iterate twice
    class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            temp = head
            length = 1
            while temp is not None:
                temp = temp.next
                length += 1
            temp = head
            for i in range(ceil(length/2)-1):
                temp = temp.next
            return temp
    # Best Solution - double pointer, one iteration
    class Solution(object):
        def middleNode(self, head):
            # We need two pointers, one is head with one step each iteration, and the other is tmp with two steps each iteration.
            temp = head
            while temp and temp.next:
                # In each iteration, we move head one node forward and we move temp two nodes forward...
                head = head.next
                temp = temp.next.next
            # When temp reaches the last node, head will be exactly at the middle point...
            return head

# 19. Remove Nth Node From End of List - Medium
    # My solution - 2 pointers - point to n spots ahead
    class Solution:
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            temp = head
            delnode = head
            temp2 = None
            for i in range(n-1):
                temp = temp.next
            while temp.next is not None:
                temp = temp.next
                temp2 = delnode
                delnode = delnode.next
            if temp2 is None:
                return head.next
            else:
                temp2.next = delnode.next
                delnode = None
            return head
        
# 3. Longest Substring Without Repeating Characters - Medium
    # My solution - hashmap of most recent index - TOP 20%!
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            temp = {}
            maxlen = 0
            currstring = 0
            for i,c in enumerate(s):
                # character in currentstring, check length and increment string
                if c in temp and temp[c] >= currstring:
                    if (i-currstring) > maxlen:
                        maxlen = i-currstring
                    currstring = temp[c] + 1
                temp[c] = i
            if (len(s)-currstring) > maxlen:
                maxlen = len(s)-currstring

            return maxlen