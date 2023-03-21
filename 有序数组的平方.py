def sortedSquare(nums):
  left = 0
  right = len(nums)-1
  ans = [-1] * len(nums)
  k = len(ans) - 1
  while(left < right):
    if nums[left]*nums[left] < nums[right]*nums[right]:
      ans[k] = nums[right]*nums[right]
      right--
    else:
      ans[k] = nums[left]*nums[left]
      left++
    k--
    
  return ans
  
