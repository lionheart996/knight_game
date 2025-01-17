def get_board_size():
    while True:
        board_size = input("Please mark the size of the board you want to play in: ")
        if board_size.isdigit() and int(board_size) > 0:
            return int(board_size)
        print("Please enter a positive integer for the board size!")

def initialize_board(board_size):
    board = []
    knights = {}
    for row in range(board_size):
        line = input(f"Enter row {row + 1} of the board: ")
        board.append(list(line))
        for col in range(len(line)):
            if line[col].upper() == "K":
                knights[(row, col)] = 0
    return board, knights

def calculate_conflicts(board, knights, board_size, possible_moves):
    for (row, col) in knights:
        for move in possible_moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                if board[new_row][new_col] == "K":
                    knights[(row, col)] += 1

def remove_knights(board, knights):
    removed_knights = 0
    while knights:
        # Find the knight with the maximum conflicts
        knight_to_remove = max(knights, key=knights.get)
        if knights[knight_to_remove] == 0:
            break
        # Remove the knight
        del knights[knight_to_remove]
        board[knight_to_remove[0]][knight_to_remove[1]] = "0"
        removed_knights += 1
        # Update conflicts
        update_conflicts(board, knight_to_remove, knights)
    return removed_knights

def update_conflicts(board, knight_to_remove, knights):
    possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    row, col = knight_to_remove
    for move in possible_moves:
        new_row, new_col = row + move[0], col + move[1]
        if (new_row, new_col) in knights:
            knights[(new_row, new_col)] -= 1

def print_board(board):
    print("Updated Chess Board:")
    for row in board:
        print("".join(row))

def main():
    board_size = get_board_size()
    board, knights = initialize_board(board_size)
    possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    calculate_conflicts(board, knights, board_size, possible_moves)
    removed_knights = remove_knights(board, knights)
    print(f"The number of knights removed from the board is: {removed_knights}")
    print_board(board)

if __name__ == "__main__":
    main()
