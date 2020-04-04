#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Solution:

    @classmethod
    def max_sum(cls, arr):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        Example:

        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Follow up:

        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
        """
        if len(arr) == 0:
            return 0

        curr_max = global_max = arr[0]
        for i in arr:
            curr_max = max(curr_max + i, i)
            global_max = max(global_max, curr_max)

        return global_max

    @classmethod
    def max_continues_seq(cls, arr):
        """
        示例 1:

        输入: [1,3,5,4,7]
        输出: 3
        解释: 最长连续递增序列是 [1,3,5], 长度为3。
        尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
        示例 2:

        输入: [2,2,2,2,2]
        输出: 1
        解释: 最长连续递增序列是 [2], 长度为1。
        注意：数组长度不会超过10000。
        :param arr:
        :return:
        """

        curr_len = max_len = 1
        for i in (0, len(arr)-2):
            if arr[i+1] > arr[i]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1

        max_len = max(max_len, curr_len)
        return max_len

    @classmethod
    def max_seq(cls, arr):
        size = len(arr)
        if size <= 1:
            return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if arr[i] > arr[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i], dp[j] + 1)
        # 最后要全部走一遍，看最大值
        return max(dp)


if __name__ == '__main__':
    print Solution.max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print Solution.max_continues_seq([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print Solution.max_seq([-2, 1, -3, 4, -1, 2, 1, -5, 4])