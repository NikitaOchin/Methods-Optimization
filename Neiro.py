import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

L = [[0,1],
     [1,0],
     [0,0],
     [1,1]]

W = list()
er = 100
O1ideal = [1,1,0,1]


O1in = [0.0]*4
Olout = [0.0]*4
H1in = [0.0]*4
H1out = [0.0]*4
H2in = [0.0]*4
H2out = [0.0]*4
H3in = [0.0]*4
H3out = [0.0]*4

for i in range(20000):
    w = [random.uniform(-100.0,100.0) for i in range(9)]
    for j in range(4):
        H1in[j] = L[j][0]*w[0] + L[j][1]*w[1]
        H1out[j] = sigmoid(H1in[j])
        H2in[j] = L[j][0]*w[2] + L[j][1]*w[3]
        H2out[j] = sigmoid(H2in[j])
        H3in[j] = L[j][0]*w[4] + L[j][1]*w[5]
        H3out[j] = sigmoid(H3in[j])
        O1in[j] = H1out[j]*w[6] + H2out[j]*w[7] + H3out[j]*w[8]
        Olout[j] = sigmoid(O1in[j])
        j+=1
    
    Error = sum([(O1ideal[i]-Olout[i])**2 for i in range(4)])/4
    if Error < er:
        W = w
        er = Error
    i+=1

print('Проверка')

l1, l2 = 0, 1
def Test(l1,l2,W):
    H1in = l1*W[0] + l2*W[1]
    H1out = sigmoid(H1in)
    H2in = l1*W[2] + l2*W[3]
    H2out = sigmoid(H2in)
    H3in = l1*W[4] + l2*W[5]
    H3out = sigmoid(H3in)

    O1in = H1out*W[6] + H2out*W[7]+ H3out*W[8]
    O1out = sigmoid(O1in)
    print(round(O1out,4))


Test(0,0,W)
Test(0,1,W)
Test(1,0,W)
Test(1,1,W)
