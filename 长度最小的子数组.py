def min_sub_array(nums, val):
    result = len(nums)+1
    sum = 0
    i = 0
    for j in range(len(nums)):
        sum += nums[j]
        while sum >= val:
          sub_len = j - i + 1
          result = min(result, sub_len)
          sum -= nums[i]
          i++
    
   return result
