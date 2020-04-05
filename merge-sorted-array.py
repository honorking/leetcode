#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    @classmethod
    def merge(cls, s1, m, s2, n):
        """
        给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

        说明:

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        示例:

        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]
        :param s1:
        :param s2:
        :return:
        """

        if len(s1) == 0:
            return s2

        if len(s2) == 0:
            return s1

        while m > 0 and n > 0:
            if s1[m-1] > s2[n-1]:
                s1[m+n-1] = s1[m-1]
                m = m - 1
            else:
                s1[m+n-1] = s2[n-1]
                n = n - 1

        if m == 0:
            s1[:n-1] = s2[:n-1]

        return s1


if __name__ == '__main__':
    print Solution.merge([1, 2, 3, 7, 0, 0, 0], 4, [2, 5, 6], 3)