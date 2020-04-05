#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    非递归实现版本
    递归版本比较简单，哪个顺序在前就先打印，其他递归即可
    """
    @classmethod
    def preorder(cls, root):
        """
        根->左->右
        :param root:
        :return:
        """
        pnode = root
        ret = []
        stack = []
        while pnode or len(stack) != 0:
            if pnode:
                ret.append(pnode.val)
                stack.append(pnode)
                pnode = pnode.left
            else:
                node = stack.pop()
                pnode = node.right

        return ret

    @classmethod
    def middleorder(cls, root):
        """
        左->根->右
        :param root:
        :return:
        """

        pnode = root
        ret = []
        stack = []
        while pnode or len(stack) != 0:
            if pnode:
                stack.append(pnode)
                pnode = pnode.left
            else:
                node = stack.pop()
                ret.append(pnode.val)
                pnode = node.right

        return ret


    @classmethod
    def postorder(cls, root):
        """
        左->右->根
        :param root:
        :return:
        """

    @classmethod
    def leveltraverse(cls, root):
        """
        层次遍历
        :param root:
        :return:
        """
        queue = Queue()
        queue.push(root)
        ret = []
        while not queue:
            node = queue.pop()
            ret.append(node.val)
            if not node.left:
                queue.push(node.left)

            if not node.right:
                queue.push(node.right)
