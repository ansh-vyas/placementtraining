# Q5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(nums1, m, nums2, n):
  # initialize two pointers to the end of each array
  i = m - 1
  j = n - 1
  # initialize a pointer to the end of the merged array
  k = m + n - 1
  # loop until one of the pointers reaches the beginning
  while i >= 0 and j >= 0:
    # if the element in nums1 is larger, copy it to the merged array
    if nums1[i] > nums2[j]:
      nums1[k] = nums1[i]
      # decrement i and k
      i -= 1
      k -= 1
    # otherwise, copy the element in nums2 to the merged array
    else:
      nums1[k] = nums2[j]
      # decrement j and k
      j -= 1
      k -= 1
  # if there are remaining elements in nums2, copy them to the merged array
  while j >= 0:
    nums1[k] = nums2[j]
    # decrement j and k
    j -= 1
    k -= 1