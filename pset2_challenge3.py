def balance(A,B):
    m=len(A)
    n=len(B)
    i=0
    j=0
    count=0




    if is_even_len(m, n):
        medianpos1 = ((m + n) // 2) - 1
        medianpos2 = (m + n) // 2
        prev=None
        while i < m and j < n:
            if A[i] < B[j]:
                current = A[i]
                i += 1
            else:
                current = B[j]
                j += 1

                if count==medianpos1:
                    prev=current
                elif count==medianpos2:
                    return (prev+current)/2.0
                count += 1


    else:
        medianpos = (m + n) // 2
        while i < m and j < n:
            if A[i] < B[j]:
                current = A[i]
                i += 1
            else:
                current = B[j]
                j += 1

            if count==medianpos:
                return current
            count += 1




def is_even_len(m,n):
    if (m+n)%2==0:
        return True
    else:
        return False
array1=[1,3]
array2=[2]
print(array1)
print(array2)
print(f"median: {balance(array1,array2)}")
