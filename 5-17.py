# 34. Find First and Last Position of Element in Sorted Array - Medium
    # My solution
    class Solution:
        def searchRange(self, nums: List[int], target: int) -> List[int]:
            l = 0
            r = len(nums) - 1
            toreturn = [-1,-1]

            # first occurence
            while (l<=r):
                m = (l+r)//2
                if nums[m] == target:
                    toreturn[0] = m
                    r = m-1
                elif nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
            # second occurence
            l = 0
            r = len(nums) - 1
            while (l<=r):
                m = (l+r)//2
                if nums[m] == target:
                    toreturn[1] = m
                    l = m+1
                elif nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
            return toreturn

# 33. Search in Rotated Sorted Array - Medium
    # My solution        
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            l = 0
            r = len(nums)-1
            while (l<=r):
                m = (l+r)//2
                if (nums[m] == target):
                    return m
                if nums[l] <= nums[m]:
                    if nums[l] <= target and nums[m] >= target:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[r] >= target and nums[m] <= target:
                        l = m + 1
                    else:
                        r = m - 1
            return -1
# 74. Search a 2D Matrix - Medium
    # My solution - treat 2D matrix like 1D matrix
    class Solution:
        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            numindices = len(matrix) * len(matrix[0])
            l = 0
            r = numindices - 1
            while (l<=r):
                mid = (l+r)//2
                midrow = mid//len(matrix[0])
                midcol = mid%len(matrix[0])
                if (matrix[midrow][midcol] == target):
                    return True
                elif (target > matrix[midrow][midcol]):
                    l = mid+1
                elif (target < matrix[midrow][midcol]):
                    r = mid-1
            return False
        
# 153. Find Minimum in Rotated Sorted Array - Medium
    # My solution
    class Solution:
        def findMin(self, nums: List[int]) -> int:
            l = 0
            r = len(nums)-1
            minval = sys.maxsize
            while (l<=r):
                m = (l+r)//2
                if nums[m] < minval:
                    minval = nums[m]
                # right is sorted
                if nums[m] <= nums[r]:
                    r = m-1
                # else left is sorted
                else:
                    l = m+1
            return minval

