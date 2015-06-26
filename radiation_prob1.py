def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    sum = 0
    ptr = start
    while ptr<stop:
        sum = sum + f(ptr)*step
        ptr = ptr+ step
    return sum

print radiationExposure(0,5,1)