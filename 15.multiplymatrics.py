# Program to multiply two matrices using nested loops


# 3x2 matrix
X = [[2, 4], [4, 6], [6, 8]]
# 2x3 matrix
Y = [[8, 6, 4], [6, 4, 8]]

# resultant matrix
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

my_list = []
# iterating rows of X matrix
for i in range(len(X)):
    # iterating columns of Y matrix
    for j in range(len(Y[0])):
        # iterating rows of Y matrix
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)