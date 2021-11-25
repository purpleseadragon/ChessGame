"""Main file for chess game"""
import pieces
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


def main():
    """main game loop"""
    white_rook_1 = pieces.Rook('white', (coord_dict['1'], coord_dict['a']), board)
    white_rook_2 = pieces.Rook('white', (coord_dict['2'], coord_dict['b']), board)
    white_king = pieces.King('white', (coord_dict['1'], coord_dict['e']), board)
    black_king = pieces.King('black', (coord_dict['8'], coord_dict['f']), board)
    print(white_rook_1.print_board())
    print(white_king.possible_moves())
    print(white_king.possible_moves_notation())
    print(white_rook_1.possible_moves_notation())


if __name__ == '__main__':
    # sample = pieces.Piece('white', (4, 5), board)
    # print(sample.location)
    # print(sample.colour)
    # sample_rook = pieces.Rook('white', (3, 4), board)
    # print(sample_rook.print_board())
    # print(sample_rook.possible_moves())
    # print(sample_rook.possible_moves(True))
    # print(sample_rook.move_piece((3, 6)))
    # print(sample_rook.location)
    # print(sample_rook.possible_moves())
    # print(sample_rook.move_piece((6, 7)))
    # print(sample_rook.location)
    # print(sample_rook.print_board())
    main()
