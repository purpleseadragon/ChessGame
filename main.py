'''Main file for chess game'''
import numpy as np
import pieces

def main():
    """main game loop"""
    pass

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
    print(sample_rook.move_piece((3, 6)))
    print(sample_rook.location)
    print(sample_rook.print_board())
    print(sample_rook.move_piece((6, 6)))
    print(sample_rook.location)
    print(sample_rook.print_board())