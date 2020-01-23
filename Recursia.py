import random

def sort_sliyanie(A):
    if len(A) == 1:
        return A
    n = len(A)
    A1 = sort_sliyanie(A[:n//2:])
    A2 = sort_sliyanie(A[n//2::])
    A = list();
    while len(A1)!= 0 and len(A2)!=0:
        A.append(A1.pop(0) if A1[0] <= A2[0] else A2.pop(0))
    return A + A1 + A2

def sort_of_toni_horn(A):
    if len(list(set(A))) <= 1:
        return A
    A1,A2,A3 = [],[],[]
    for i in range(len(A)):
        if A[0]> A[i]:
            A1.append(A[i])
        elif A[0] < A[i]:
            A3.append(A[i])
        else:
            A2.append(A[i])
    return sort_of_toni_horn(A1) + A2 + sort_of_toni_horn(A3)


A = [random.randint(0,10) for i in range(1000)]
print(sort_of_toni_horn(A))
print(sort_sliyanie(A))

