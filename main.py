'''Main file for chess game'''
import pieces


def main():
    """main game loop"""
    pass


coord_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              '8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

board = [['  ', '  ', '  ', '  ', 'bp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'wp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', 'wp', 'wp', '  ', '  ', '  ', 'bp', 'wh'],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'bp', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', 'wp', '  ', '  ', '  ']
         ]

if __name__ == '__main__':
    sample = pieces.Piece('white', (4, 5), board)
    print(sample.location)
    print(sample.colour)
    sample_rook = pieces.Rook('white', (3, 4), board)
    print(sample_rook.print_board())
    print(sample_rook.possible_moves())
    print(sample_rook.possible_moves(True))
    print(sample_rook.move_piece((3, 6)))
    print(sample_rook.location)
    print(sample_rook.possible_moves())
    print(sample_rook.move_piece((6, 7)))
    print(sample_rook.location)
    print(sample_rook.possible_moves())