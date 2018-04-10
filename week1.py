#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    from functools import reduce
    result = reduce(lambda x,y : x + y, ar)
    return result
    
    # OR
    # result = 0
    # while len(ar):
    #     result += ar[0]
    #     ar = ar[1:]
    # 
    # return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
