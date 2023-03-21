def remove_element(nums, val):
    fast_index = 0
    slow_index = 0
    while(fast_index<=len(nums)):
        if(val!=nums[fast_index]):
            nums[slow_index++] = nums[fast_index]
        fast_index++
        
    return slow_index
