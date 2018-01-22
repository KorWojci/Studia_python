import numpy

w1 = input()
w2 = input()

w = int(len(w1))
k = int(len(w2))

w1 = " " + w1
w2 = " " + w2

matrix1 = numpy.zeros((w+1, k+1))

for i in range(0, w+1):
    matrix1[i][0] = i

for j in range(0, k+1):
    matrix1[0][j] = j

for j in range(1, k+1):
    for i in range(1, w+1):
        if w1[i] == w2[j]:
            cost = 0
        else:
            cost = 1
        matrix1[i][j] = min(matrix1[i-1][j]+1, matrix1[i][j-1]+1, matrix1[i-1][j-1]+cost)


print(int(matrix1[w][k]))

#print(matrix1)