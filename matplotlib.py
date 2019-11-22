def is_valid_board(board):
    import numpy as np
    if type(board)!=np.ndarray:
        raise TypeError("The input board must be a numpy array(ndarray).")
    elif len(board.shape)!=2:
        raise ValueError("The input board must be a 2-dimemsional numpy array.")
    elif any([i!=0.0 and i!=1.0 for i in np.unique(board)]):
        raise ValueError("All entries must be either 0.0 or 1.0")
    else:
        return True

    
def gol_step(board):
    import numpy as np
    # Error checking
    is_valid_board(board)
    
    m,n = board.shape
    
    # Generating a new_board that represents the next step and making an entry's value = 0 at default
    new_board = np.zeros(shape=(m,n))

    for i in range(m):
        for j in range(n):
            self = board[i,j]
            row_index,col_index = [-1,0,1], [-1,0,1]

            # To handle the edges and corners at right and bottom, we need to adjust the range of neighbors
            if i==m-1: row_index = [-1,0,1-m]
            if j==n-1: col_index = [-1,0,1-n]
            # Counting neighbors
            cnt = sum([board[i+h,j+k] for h in row_index for k in col_index]) - self

            # Defining the value of cells which should turn 0 into 1 following the game rules
            # Only defining the case which we can expect the change of value from 0 to 1 in the cell
            if cnt==3:
                new_board[i,j] = 1
            elif cnt==2 and self == 1:
                new_board[i,j] = 1
    return new_board

def draw_gol_board(board):

    cmap = plt.get_cmap('binary')
    plt.imshow(board, cmap=cmap, interpolation='nearest')
    plt.xticks([],[])
    plt.yticks([],[])
    _ = plt.show()
    
test = np.array([[0., 0., 0., 0., 0.],
                 [0., 0., 1., 0., 0.],
                 [0., 0., 0., 1., 0.],
                 [0., 1., 1., 1., 0.],
                 [0., 0., 0., 0., 0.]])

gameboard = np.zeros(shape=(20,20))
gameboard[:5,:5] = np.array([[0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0.],
                             [0., 0., 0., 1., 0.],
                             [0., 1., 1., 1., 0.],
                             [0., 0., 0., 0., 0.]])
plt.figure(figsize=(8,8))
draw_gol_board(gameboard)

step = gameboard
for i in range(511,516):
    plt.figure(figsize=(50,50))
    plt.subplot(i)
    draw_gol_board(step)
    next_step = gol_step(step)
    step = next_step
    plt.show()
