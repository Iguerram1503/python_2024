'''
002 Matrix
'''

'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''

#print(matrix)

matrix =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#print(matrix)

'''
print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[0][0])
print(matrix[1][1])
'''

for row in matrix:
    #print(row)
    for value in row:
        #print(value)
        if value == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
