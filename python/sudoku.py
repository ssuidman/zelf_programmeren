import numpy as np

sudoku0 = np.array([
    [8,0,6,9,0,0,0,7,1],
    [0,3,0,0,0,0,0,0,6],
    [2,0,0,8,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,0],
    [0,0,0,0,1,0,4,8,0],
    [7,0,2,0,0,9,0,5,0],
    [3,0,8,0,9,0,0,0,7],
    [5,0,0,0,0,7,0,0,0],
    [0,2,0,0,0,0,5,0,0]
    ])

sudoku1 = np.array([
    [6,0,0,0,0,4,0,8,0],
    [1,0,0,9,0,5,6,0,7],
    [0,8,5,0,0,0,1,2,0],
    [0,0,0,0,0,0,8,5,9],
    [0,4,0,0,5,0,0,0,0],
    [0,0,9,3,6,0,0,0,2],
    [2,0,0,4,1,0,0,9,0],
    [4,0,3,5,0,0,0,0,0],
    [0,9,0,0,7,6,0,1,0],
])

sudoku2 = np.array([
    [0,0,0,3,9,6,5,0,0],
    [3,9,0,0,8,7,0,0,0],
    [5,0,0,2,4,1,3,9,6],
    [4,0,3,1,6,9,8,0,5],
    [1,0,0,0,0,0,4,2,3],
    [8,0,0,0,0,3,0,0,0],
    [9,1,2,6,3,0,7,0,0],
    [0,0,0,7,5,8,9,0,2],
    [7,5,0,9,0,2,0,0,0],
]
)
sudoku = sudoku0.copy()


def sudoku_columns(sudoku):
    return np.transpose(sudoku)

def coordinates_columns(i,j): # these coordinates can be filled in for a sudoku_columns
    return j,i

def sudoku_squares(sudoku):
    sudoku_squares = np.zeros([9,9],dtype=int)
    for i in range(9):
        for j in range(9):
            a = i-i%3 + int((j-j%3)/3)
            b = i%3*3 + j%3
            sudoku_squares[a][b] = sudoku[i][j]
    return sudoku_squares

def coordinates_squares(i,j): # these coordinates can be filled in for a sudoku_squares
    a = i-i%3 + int((j-j%3)/3)
    b = i%3*3 + j%3
    return a,b

def coordinates_concatenated(i,j): #returns the single(!) coordinate of the concatenated array
    return i*9+j

def init():
    possible_values = np.zeros([9,9,9],dtype=int)
    for i in range(9):
        for j in range(9):
            for k in range(0,9):
                possible_values[i][j][k] = k+1
    return possible_values

def check_values(sudoku,possible_values): # check which values are possible for coordinates
    # print("check values")
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                possible_values[i][j] = np.zeros(9,dtype=int)
                possible_values[i][j][sudoku[i][j]-1] = sudoku[i][j]
            for k in range(1,10):
                l = coordinates_squares(i,j)[0]
                column_sudoku = sudoku_columns(sudoku)
                square_sudoku = sudoku_squares(sudoku)

                if k in sudoku[i] or k in column_sudoku[j] or k in square_sudoku[l]:
                    if k!=sudoku[i][j]:
                        possible_values[i][j][k-1] = 0

def fill_in_values(sudoku,possible_values): # fill in values, then check and fill in again, etc (only for values that are the only option for a coordinate)
    # print("fill in values")
    sudoku_check = np.zeros([9,9],dtype=int)
    possible_values_check = np.zeros([9,9,9],dtype=int)
    check_values(sudoku,possible_values)
    while np.all(np.concatenate(sudoku) == np.concatenate(sudoku_check)) == False or np.all(np.concatenate(possible_values) == np.concatenate(possible_values_check)) == False:
        sudoku_check = sudoku.copy()
        possible_values_check = possible_values.copy()
        for i in range(9):
            for j in range(9):
                options = np.nonzero(possible_values[i][j])[0]
                if options.size == 1 and sudoku[i][j] != possible_values[i][j][options[0]]:
                    sudoku[i][j] = possible_values[i][j][options[0]]
                    check_values(sudoku,possible_values)
    if np.sum(np.concatenate(sudoku)) == 405:
        return True
    else: 
        return False

def possible_amount(possible_values): # look how many values are possible for every coordinate
    amount_matrix = np.array([[np.nonzero(possible_values[i][j])[0].size for j in range(9)] for i in range(9)])
    return amount_matrix

def try_values(sudoku,possible_values): # try if there are only two possible numbers for coordinate
    print("try values")
    #step 1 
    amount = possible_amount(possible_values)
    for i in range(9):
        for j in range(9):
            if amount[i][j] == 2: # check if there are 2 possible numbers 
                for k in np.nonzero(possible_values[i][j])[0]: # look at possible options
                    test_sudoku = sudoku.copy() #create test sudoku
                    test_possible_values = possible_values.copy() #create test possible values                    
                    test_sudoku[i][j] = k
                    check = fill_in_values(test_sudoku,test_possible_values)

def pick_one_choice(sudoku,possible_values,n): #pick one options and look if it leads to inconsistency
    #step 2
    # print("pick one choice")
    print(n)
    print(possible_amount(possible_values))
    check = fill_in_values(sudoku,possible_values)
    amount = possible_amount(possible_values)
    if n == 5:
        print(sudoku)
        print(amount)
    if check:
        return check 
    for i in range(9):
        for j in range(9):
            if amount[i][j] == 2: # check if there are 2 possible numbers 
                # if n==18:
                    # print(i,j)
                    # print(possible_amount(possible_values))
                for l in np.nonzero(possible_values[i][j])[0]: # look at possible options
                    k = possible_values[i][j][l]
                    print('n=',n,'i=',i,'j=',j,'k=',k)    
                    test_sudoku = sudoku.copy() #create test sudoku
                    test_possible_values = possible_values.copy() #create test possible values
                    test_sudoku[i][j] = k
                    test_possible_values[i][j] = np.zeros(9,dtype=int)
                    test_possible_values[i][j][k-1] = k
                    check_values(test_sudoku,test_possible_values)
                    check = pick_one_choice(test_sudoku,test_possible_values,n+1)
                    if check:
                        sudoku = test_sudoku
                        possible_values = test_possible_values
                        break
                    if np.any(possible_amount(test_possible_values)==0):
                        possible_values[i][j][k] = 0
                        print('hoihoi')
                if check:
                    break
            if check:
                break
        if check:
            break
    return check 

possible_values = init() # fill for every number for possible coordinate i,j in if it is possible. If not change it to 0
# fill_in_values(sudoku,possible_values)
# print(possible_amount(possible_values))

# print(sudoku1)
# print('\n')
# print(sudoku)
# try_values(sudoku,possible_values)
print(sudoku)
pick_one_choice(sudoku,possible_values,0)
print(sudoku)
# print(possible_amount(possible_values))



# print(sudoku0)
# print('\n')
# print(sudoku)