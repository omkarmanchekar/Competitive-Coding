# import sys


# s=sys.stdin.readlines()
#     # print(i,end=" ")

# print(s)

# # [1,2,2,3,3,3]/n
# # [23,3]/n
# # (1,2)/n

import fileinput
import sys

for line in fileinput.input():
    # print(line,end=" ")
    first = line.rstrip("[]'")
    second=first.lstrip("[]'")
    print(second)