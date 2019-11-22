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
