def make_board():
    return [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

def print_board(board):
    print(
        f"
        {board[0][0]}, {board[0][1]}, {board[0][2]}
        {board[1][0]}, {board[1][1]}, {board[1][2]}
        {board[2][0]}, {board[2][1]}, {board[2][2]}
    )

def make_move(board):