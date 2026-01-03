from shiboken6 import isValid


def parantheses(s):

    queue=[s]
    print("queue: ",queue)
    visited=set(s)
    print("visited: ",visited)
    found=False
    result=[]

    while queue and not found:
        next_level=[]
        for current in queue:
            print("current: ",current)
            for i in range(len(current)):
                if current[i] not in "()":
                    continue
                candidate=current[:i]+current[i+1:]
                print("candidate: ",candidate)
                if candidate not in visited:
                    visited.add(candidate)
                    if isValid(candidate):
                        found=True
                        result.append(candidate)
                    else:
                        next_level.append(candidate)
        if found:
            break
        queue=next_level
    if not result:
        return [""]
    return result

def isvalid(s):
    balance=0
    for c in s:
        if c=="(":
            balance+=1
        elif c==")":
            balance-=1
        if balance<0:
            return False
    return balance==0
print(parantheses("()())()"))