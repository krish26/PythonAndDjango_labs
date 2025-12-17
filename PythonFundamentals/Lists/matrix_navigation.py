l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
matrix =[l1,l2,l3]


#row1,col2
print('row 1 col2 : ' ,matrix[0][1])

#second row
print('second row : ' ,matrix[1])

#diagonal
print('diagonal: ' ,matrix[0][0],matrix[1][1],matrix[2][2])

#first col elements using index 

print('first col : ' ,matrix[0][0], matrix[1][0],matrix[2][0])

first_col = [row[0] for row in matrix]
print(first_col)


#
