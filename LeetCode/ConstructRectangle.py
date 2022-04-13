'''
Construct Rectangle

https://leetcode.com/problems/construct-the-rectangle/

-> Find the largest Factors
-> If prime return 1 and the area

'''

import math


def constructRectangleBrute(area):
    i = area - 1
    fact1 = area
    fact2 = 1
    diff = fact1 - fact2

    while(i>=2):
        if area % i == 0:
            f1 = area // i
            d = abs(f1-i)
            if d < diff:
                diff = d
                if i>f1:
                    fact1 = i
                    fact2 = f1
                else:
                    fact1 = f1
                    fact2 = i
        i-=1
    return [fact1,fact2]

# print(constructRectangleBrute(10000000))


def constructRectangle(area):
    
    fact1 = area
    fact2 = 1
    diff = fact1 - fact2
    
    for i in range(1, int(area ** 0.5) + 1):
        div, mod = divmod(area, i)
        if mod == 0:
            d = abs(div-i)
            if d < diff:
                diff = d
                if i>div:
                    fact1 = i
                    fact2 = div
                else:
                    fact1 = div
                    fact2 = i
    return [fact1,fact2]

# print(constructRectangle(10000000))


from Measure import measure
measure(constructRectangleBrute,10000000)
measure(constructRectangle,10000000)