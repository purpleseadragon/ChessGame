"""Main file for chess game, run this to run the game"""
import pieces
from main_helper import move_converter
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


def game_setup():
    """Sets up pieces for game"""
    white_rook_1 = pieces.Rook('white', (coord_dict['1'], coord_dict['a']), board)
    white_rook_2 = pieces.Rook('white', (coord_dict['2'], coord_dict['b']), board)
    white_king = pieces.King('white', (coord_dict['1'], coord_dict['e']), board)
    black_king = pieces.King('black', (coord_dict['8'], coord_dict['f']), board)
    white_pieces = [white_rook_1, white_rook_2, white_king]
    black_pieces = [black_king]
    return white_pieces, black_pieces


def main():
    """main game loop"""
    white_pieces, black_pieces = game_setup()
    current_turn, next_turn = 'white', 'black'
    turn_dict = {'white': white_pieces, 'black': black_pieces}
    turn_count = 0
    white_pieces[0].print_board(current_turn)
    while True:
        # prints board
        # check if current turn player is in check / checkmate
        for piece in turn_dict[current_turn]:
            if isinstance(piece, pieces.King):
                king_location = piece.location

        all_possible_moves = []
        for piece in turn_dict[next_turn]:
            all_possible_moves += piece.possible_moves(True)
        if king_location in all_possible_moves:
            # need to check for checkmate
            pass

        # if in check must block
        error_message = ''
        while True:
            # while loop to get valid move
            print(f"It is currently {current_turn}'s turn, where would you like to move?")
            print(f'{error_message}')
            if king_location in all_possible_moves:
                print('Your king is in check, pls move out of check')
            move = input(f"Please answer in the form of chess notation, eg Re5: ")

            if not isinstance(move_converter(move, turn_dict[current_turn]), str):
                # making sure the move made is valid
                move_coord, piece_index = move_converter(move, turn_dict[current_turn])
                original_coord = turn_dict[current_turn][piece_index].location
                # performs the move
                turn_dict[current_turn][piece_index].move_piece(move_coord)
                # making sure the king is not in check
                for piece in turn_dict[current_turn]:
                    if isinstance(piece, pieces.King):
                        king_location = piece.location
                all_possible_moves = []
                for piece in turn_dict[next_turn]:
                    all_possible_moves += piece.possible_moves(True)
                if king_location not in all_possible_moves:
                    break
                # resets if move results in check
                turn_dict[current_turn][piece_index].move_piece(original_coord)

            error_message = move_converter(move, turn_dict[current_turn])

        turn_count += 1
        current_turn, next_turn = next_turn, current_turn
        white_pieces[0].print_board(current_turn)

        # early break
        if turn_count > 2:
            break


if __name__ == '__main__':
    main()
