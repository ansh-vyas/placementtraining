# Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

def search_insert(nums, target):
  # initialize low and high pointers
  low = 0
  high = len(nums) - 1
  # loop until low and high cross
  while low <= high:
    # find the middle index
    mid = (low + high) // 2
    # if the target is found, return the index
    if nums[mid] == target:
      return mid
    # if the target is smaller, move the high pointer to the left
    elif nums[mid] > target:
      high = mid - 1
    # if the target is larger, move the low pointer to the right
    else:
      low = mid + 1
  # if the target is not found, return the low pointer as the insertion index
  return low