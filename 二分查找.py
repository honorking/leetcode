def solution(nums, val):
  left = 0
  right = len(nums)-1
  while(left <= right):
    middle = (left + right)//2
    if nums[middle] > val:
      right = middle - 1
    else if nums[middle] < val:
      left = middle + 1
    else
      return middle
