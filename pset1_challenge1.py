import math
def team(contributions):
    impact=[]
    for i in range(len(contributions)):
        result1=math.prod(contributions[:i])
        result2=math.prod(contributions[i+1:])
        impact.append(result1*result2)
    return impact
print(team([-1,1,0,-3,3]))





