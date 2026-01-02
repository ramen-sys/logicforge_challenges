import heapq

def kthsmallest(matrix,k):
    n=len(matrix)
    min_heap=[]
    for row in range(n):
        heapq.heappush(min_heap,(matrix[row][0],row,0))
        print(min_heap)

    for _ in range(k-1):
        value,row,col=heapq.heappop(min_heap)

        if col+1<n:
            next=matrix[row][col+1]
            heapq.heappush(min_heap,(next,row,col+1))
    return heapq.heappop(min_heap)[0]
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthsmallest(matrix, k))