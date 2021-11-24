"""File that contains additional funcfions"""

def rook_move_helper_column(moves_range, colour_letter, board, column):
    # helps with creating possible moves
    possible_moves_list = []
    for num in moves_range:
        if board[num][column] == '  ':
            possible_moves_list.append((num, column))
        elif board[num][column][0] != colour_letter:
            possible_moves_list.append((num, column))
            break
        else:
            break
    return possible_moves_list


def rook_move_helper_row(moves_range, colour_letter, board, row):
    # helps with creating possible moves
    possible_moves_list = []
    for num in moves_range:
        if board[row][num] == '  ':
            possible_moves_list.append((row, num))
        elif board[row][num][0] != colour_letter:
            possible_moves_list.append((row, num))
            break
        else:
            break
    return possible_moves_list
