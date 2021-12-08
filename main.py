"""Main file for chess game, run this to run the game"""
import pieces
from main_helper import move_converter, checkmate_checker, promotion
coord_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              '8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

board = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
         ]


def game_setup(num=0):
    """Sets up pieces for game"""
    if num == 1:
        # checkmate testing piece set
        # white_rook_1 = pieces.Rook('white', (coord_dict['1'], coord_dict['a']), board)
        white_bishop_1 = pieces.Bishop('white', (coord_dict['5'], coord_dict['d']), board)
        white_king = pieces.King('white', (coord_dict['1'], coord_dict['e']), board)
        black_king = pieces.King('black', (coord_dict['8'], coord_dict['f']), board)
        # black_pawn_1 = pieces.Pawn('black', (coord_dict['7'], coord_dict['b']), board)
        # black_bishop_1 = pieces.Bishop('black', (coord_dict['3'], coord_dict['c']), board)
        # black_knight_2 = pieces.Knight('black', (coord_dict['8'], coord_dict['g']), board)
        white_pieces = [white_bishop_1, white_king]
        black_pieces = [black_king]
    elif num == 2:
        # stalemate testing piece set
        white_rook_1 = pieces.Rook('white', (coord_dict['1'], coord_dict['e']), board)
        white_rook_2 = pieces.Rook('white', (coord_dict['2'], coord_dict['h']), board)
        white_king = pieces.King('white', (coord_dict['6'], coord_dict['f']), board)
        black_king = pieces.King('black', (coord_dict['8'], coord_dict['f']), board)
        white_pieces = [white_rook_1, white_rook_2, white_king]
        black_pieces = [black_king]
    else:
        # standard board
        # white pieces
        white_rook_1 = pieces.Rook('white', (coord_dict['1'], coord_dict['a']), board)
        white_knight_1 = pieces.Knight('white', (coord_dict['1'], coord_dict['b']), board)
        white_bishop_1 = pieces.Bishop('white', (coord_dict['1'], coord_dict['c']), board)
        white_queen = pieces.Queen('white', (coord_dict['1'], coord_dict['d']), board)
        white_king = pieces.King('white', (coord_dict['1'], coord_dict['e']), board)
        white_bishop_2 = pieces.Bishop('white', (coord_dict['1'], coord_dict['f']), board)
        white_knight_2 = pieces.Knight('white', (coord_dict['1'], coord_dict['g']), board)
        white_rook_2 = pieces.Rook('white', (coord_dict['1'], coord_dict['h']), board)

        # white pawns
        white_pawn_1 = pieces.Pawn('white', (coord_dict['2'], coord_dict['a']), board)
        white_pawn_2 = pieces.Pawn('white', (coord_dict['2'], coord_dict['b']), board)
        white_pawn_3 = pieces.Pawn('white', (coord_dict['2'], coord_dict['c']), board)
        white_pawn_4 = pieces.Pawn('white', (coord_dict['2'], coord_dict['d']), board)
        white_pawn_5 = pieces.Pawn('white', (coord_dict['2'], coord_dict['e']), board)
        white_pawn_6 = pieces.Pawn('white', (coord_dict['2'], coord_dict['f']), board)
        white_pawn_7 = pieces.Pawn('white', (coord_dict['2'], coord_dict['g']), board)
        white_pawn_8 = pieces.Pawn('white', (coord_dict['2'], coord_dict['h']), board)

        # black pieces
        black_rook_1 = pieces.Rook('black', (coord_dict['8'], coord_dict['a']), board)
        black_knight_1 = pieces.Knight('black', (coord_dict['8'], coord_dict['b']), board)
        black_bishop_1 = pieces.Bishop('black', (coord_dict['8'], coord_dict['c']), board)
        black_queen = pieces.Queen('black', (coord_dict['8'], coord_dict['d']), board)
        black_king = pieces.King('black', (coord_dict['8'], coord_dict['e']), board)
        black_bishop_2 = pieces.Bishop('black', (coord_dict['8'], coord_dict['f']), board)
        black_knight_2 = pieces.Knight('black', (coord_dict['8'], coord_dict['g']), board)
        black_rook_2 = pieces.Rook('black', (coord_dict['8'], coord_dict['h']), board)

        # black pawns
        black_pawn_1 = pieces.Pawn('black', (coord_dict['7'], coord_dict['a']), board)
        black_pawn_2 = pieces.Pawn('black', (coord_dict['7'], coord_dict['b']), board)
        black_pawn_3 = pieces.Pawn('black', (coord_dict['7'], coord_dict['c']), board)
        black_pawn_4 = pieces.Pawn('black', (coord_dict['7'], coord_dict['d']), board)
        black_pawn_5 = pieces.Pawn('black', (coord_dict['7'], coord_dict['e']), board)
        black_pawn_6 = pieces.Pawn('black', (coord_dict['7'], coord_dict['f']), board)
        black_pawn_7 = pieces.Pawn('black', (coord_dict['7'], coord_dict['g']), board)
        black_pawn_8 = pieces.Pawn('black', (coord_dict['7'], coord_dict['h']), board)

        white_pieces = [white_rook_1, white_knight_1, white_bishop_1, white_queen, white_king, white_bishop_2,
                        white_knight_2, white_rook_2, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
                        white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8]

        black_pieces = [black_rook_1, black_knight_1, black_bishop_1, black_queen, black_king, black_bishop_2,
                        black_knight_2, black_rook_2, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
                        black_pawn_5, black_pawn_6, black_pawn_7, black_pawn_8]

    return white_pieces, black_pieces


def main():
    """main game loop"""
    white_pieces, black_pieces = game_setup()
    current_turn, next_turn = 'white', 'black'
    turn_dict = {'white': white_pieces, 'black': black_pieces}
    turn_count = 0
    white_pieces[0].print_board(current_turn)
    complete_movelist = []
    # game loop
    while True:
        # Calls function that checks for check, checkmate and stalemate
        check, checkmate, stalemate = checkmate_checker(turn_dict[current_turn], turn_dict[next_turn])
        if checkmate:
            print(f'Congratulations {next_turn}, you won the game by checkmate!')
            break
        if stalemate:
            print(f'The game ended in stalemate')
            break
        error_message = ''

        while True:
            # while loop to get valid move
            print(f"It is currently {current_turn}'s turn, where would you like to move?")
            if isinstance(error_message, str) and error_message != '':
                print(f'{error_message}')
            if check:
                print('Your king is in check, pls move out of check')
            move = input(f"Please answer in the form of chess notation, eg Re5: ")
            if not isinstance(move_converter(move, turn_dict[current_turn]), str):
                # making sure the move made is valid
                move_coord, piece_index = move_converter(move, turn_dict[current_turn])

                # turn_dict[current_turn][piece_index] is current piece being moved
                current_piece = turn_dict[current_turn][piece_index]
                original_coord = current_piece.location
                original_piece = white_pieces[0].board[move_coord[0]][move_coord[1]]

                # performs the move
                current_piece.move_piece(move_coord)

                # checks whether moved yet in the case a reset is needed
                moved_or_not = current_piece.has_moved
                current_piece.has_moved = True
                # making sure the king is not in check
                for piece in turn_dict[current_turn]:
                    if isinstance(piece, pieces.King):
                        king_location = piece.location
                all_possible_moves = []
                for piece in turn_dict[next_turn]:
                    all_possible_moves += piece.possible_moves(True)
                if king_location not in all_possible_moves:
                    complete_movelist.append(move)
                    if original_piece != '  ':
                        for count, piece in enumerate(turn_dict[next_turn]):
                            if piece.location == move_coord:
                                turn_dict[next_turn].pop(count)
                                # dealing with pawn promotion
                                if not isinstance(current_piece, pieces.Pawn) or current_piece.location[0] != 7 and \
                                        current_piece.location[0] != 0:
                                    pass
                                else:
                                    turn_dict[current_turn] = \
                                        promotion(current_piece, piece_index, turn_dict[current_turn])
                                break
                    break
                # resets if move results in check
                current_piece.location = original_coord
                if not moved_or_not:
                    current_piece.has_moved = False
                white_pieces[0].board[move_coord[0]][move_coord[1]] = original_piece

            error_message = move_converter(move, turn_dict[current_turn])

        turn_count += 1
        current_turn, next_turn = next_turn, current_turn
        white_pieces[0].print_board(current_turn)


if __name__ == '__main__':
    main()
