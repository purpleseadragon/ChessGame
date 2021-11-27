"""Helper functions for python main file"""
import pieces

coord_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              '8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}


def move_converter_helper(notation_length, move_in_notation, pieces_list, move_coord):
    """Function that assist with converting chess notation to a piece and coordinate"""
    letter_dict = {'R': pieces.Rook, 'K': pieces.King, 'Q': pieces.Queen, 'B': pieces.Bishop,
                   'N': pieces.Knight}
    letters_list = letter_dict.keys()
    row_coords_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    column_coords_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    piece_letter = move_in_notation[0]
    count = 0
    piece_index = None
    # pawn case
    if notation_length == 2:
        for index, piece in enumerate(pieces_list):
            if isinstance(piece, pieces.Pawn):
                if move_coord in piece.possible_moves():
                    piece_index = index
                    count += 1

    # length of 3 case, includes most moves plus pawn moves with specific pawn specified
    if notation_length == 3:
        for index, piece in enumerate(pieces_list):
            if piece_letter in letters_list:
                if isinstance(piece, letter_dict[piece_letter]):
                    if move_coord in piece.possible_moves():
                        piece_index = index
                        count += 1

            elif piece_letter in row_coords_list or piece_letter in column_coords_list:
                if piece_letter in row_coords_list:
                    specifier = coord_dict[piece_letter]
                    specifier_index = 0
                elif piece_letter in column_coords_list:
                    specifier = coord_dict[piece_letter]
                    specifier_index = 1

                if isinstance(piece, pieces.Pawn) and piece.location[specifier_index] == specifier:
                    if move_coord in piece.possible_moves():
                        piece_index = index
                        count += 1

    if notation_length == 4:
        specifier_original = move_in_notation[1]
        print(specifier_original)
        for index, piece in enumerate(pieces_list):
            # making sure specifier is valid
            if specifier_original in row_coords_list or specifier_original in column_coords_list:
                if specifier_original in row_coords_list:
                    specifier = coord_dict[specifier_original]
                    specifier_index = 0
                if specifier_original in column_coords_list:
                    specifier = coord_dict[specifier_original]
                    specifier_index = 1
                print(specifier, specifier_index)
                if piece_letter in letters_list:
                    if isinstance(piece, letter_dict[piece_letter]) and \
                            piece.location[specifier_index] == specifier:

                        if move_coord in piece.possible_moves():
                            piece_index = index
                            count += 1

    return piece_index, count
