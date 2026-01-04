def towerofhanoi(num,first,middle,last):
    assert num>0
    if num==1:
        print(f"move disk from: {first} to {last}")
        return
    towerofhanoi(num-1,first,last,middle)
    towerofhanoi(1,first,middle,last)
    towerofhanoi(num-1,middle,first,last)
print(towerofhanoi(3,"A","B","C"))