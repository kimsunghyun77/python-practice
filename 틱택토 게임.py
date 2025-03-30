def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        try:
            row, col = map(int, input(f"{player}의 차례 (행 열 입력, 0-2): ").split())
            if board[row][col] != " ":
                print("이미 선택된 위치입니다. 다시 입력하세요.")
                continue
        except (ValueError, IndexError):
            print("올바른 좌표를 입력하세요 (0-2 사이).")
            continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"{player} 승리!")
            break
        
        if is_full(board):
            print_board(board)
            print("무승부!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()