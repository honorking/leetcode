def remove_element(list, num):
    fast_index = 0
    slow_index = 0
    while(fast_index<=len(list)-1):
        if(num!=list[fast_index]):
            list[slow_index++] = list[fast_index]
        fast_index++
        
    return slow_index
