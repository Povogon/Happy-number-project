# import math
# inp = int(input("inp "))
# target_sys = int(input("target_sys "))
# n = True
# out = []
# quo = 0
# while n:
#     quo =  math.floor(inp / target_sys)
#     if quo < 1:
#         n = False
#     out.insert(0, inp % target_sys)
#     inp = quo
# print(out)
#
from operator import index


def number(input):
    value = 0
    for m in range(len(input)):
        if not(m>len(input)):
            value += input[m]*(10**(len(input) - m-1))
    return value
