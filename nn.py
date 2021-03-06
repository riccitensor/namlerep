# Neural network

import numpy as np
import encoder as enc

img = enc.readImage("data/pic_small.jpg")
#print(img)

X = [[0,0,0]]
print("Before", X)
#for i in range(0,img[1]):
#    for j in range(0,img[2]):
for i in range(0,1):
    for j in range(0,2):
        tmp = [[img[0][i,j][0],img[0][i,j][1],img[0][i,j][2]]]
        print("Temp ", tmp)
        np.append(tmp,X,axis=0)

# TODO: Turn the Primax representation into the most unique color possible so that
# we can see the difference in space. We would not see the difference in color,
# so we need spatial exploration.

print("After ", X)

# simple network by http://iamtrask.github.io/2015/07/12/basic-python-network/
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1],[1,1,0] ])
y = np.array([[0,1,1,0,1]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in range(60000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print (l1)
