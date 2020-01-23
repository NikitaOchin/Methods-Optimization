def lcs(A,B):
    """Search for largest common subsequences between lists A and B"""
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i][j-1],F[i-1][j])
    ##print_2DM(T(F))
    return F[-1][-1]

def levenshtein(A,B):
    """Search for Levenshtein's distant between strings A and B"""
    F = [[i+j if j*i ==0 else 0 for j in range(len(B)+1)]
         for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i][j-1],F[i-1][j],F[i-1][j-1])
    print_2DM(F)
    return F[-1][-1]
         

def Generate_num(n, m, prefix = None, A = list()):
    """Generate sequnce of numbers where
       n - number system
       m - count of position"""
    prefix = prefix or []
    if m==0:
        A.append([x for x in prefix])
        return A
    for i in range(n):
        prefix.append(i)
        A = Generate_num(n,m-1,prefix,A)
        prefix.pop()
    return A

def print_2DM(A):
    return [print(A[i]) for i in range(len(A))]
def T(F):
    A = [[0]*len(F) for i in range(len(F[0]))]
    for i in range(len(F)):
        for j in range(len(F[i])):
            A[j][i] = F[i][j]
    return A

def lcs_T(A,B,F):
    C = [0]*F[-1][-1]
    for i in range(1,len(B)+1):
        for j in range(1,len(A)+1):
            if B[-i] == A[-j]:
                C[i] = (A[-j])
            elif F[-j][-i-1] > F[-j-1][-i]:
                i+=1
            else: j+=1
    return C

def lis(A):
    """Search for longest increasing subsequences between lists A and B"""
    F = [0 for i in range(len(A)+1)]
    for i in range(1,len(A)+1):
        m = 0
        for j in range(1,i):
            if A[i-1] > A[j-1] and F[j]>m:
                m = F[j]
        F[i] = m + 1
    return max(F)

def TEST():
    A = [9,2,3,8,5,6,5,3]
    B = [8,1,2,8,7,5,4,5,6,3,5,7,1]
    ##F = lcs(A,B)

    print('gis(A) = ', lis(A))
    s = 'aababa'
    s1 = 'bbacban'
    print(levenshtein(s,s1), max(len(s),len(s1)) - lcs(s,s1))
    A = Generate_num(4, 3, prefix = None)
    [print(A[i]) for i in range(15)]

if __name__ == '__main__':
    TEST()
