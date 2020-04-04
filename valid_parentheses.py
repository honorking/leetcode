#!/usr/env/bin python

class Solution:

    @classmethod
    def valid(cls, s):
        result = []
        kmap = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for x in s:
            if x in kmap:
                result.append(x)
            else:
                if len(result) != 0:
                    if x != kmap[result.pop()]:
                        return False
                    else:
                        continue
                else:
                    return False

        return len(result) == 0


if __name__ == '__main__':
    print Solution.valid("{[()]}")