"""Helper functions for python main file"""
import pieces

coord_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
              '8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}


def move_converter(move_in_notation, pieces_list):
    """Converts move to coordinates for piece if valid
    If invalid returns a string specifying the error"""
    # unpacking of location part of notation: eg 'e5' to 3, 4
    if 'x' in move_in_notation:
        move_in_notation = move_in_notation.replace('x', '')
    move_coord = (coord_dict[move_in_notation[-1]], coord_dict[move_in_notation[-2]])
    notation_length = len(move_in_notation)
    piece_index, count = move_converter_helper(notation_length, move_in_notation,
                                               pieces_list, move_coord)

    if count != 1:
        # catches if two pieces can move to same square or move invalid
        if count == 2:
            return "Pls specify which piece should move, eg. Rfe5 instead of Re5"
        else:
            return "pls pick a valid move this time, don't be a muppet"

    return move_coord, piece_index


def move_converter_helper(notation_length, move_in_notation, pieces_list, move_coord):
    """Function that assists with converting chess notation to a piece and coordinate"""
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

    # Length of 4 case in case of multiple possible moves
    if notation_length == 4:
        specifier_original = move_in_notation[1]
        for index, piece in enumerate(pieces_list):
            # making sure specifier is valid
            if specifier_original in row_coords_list or specifier_original in column_coords_list:
                if specifier_original in row_coords_list:
                    specifier = coord_dict[specifier_original]
                    specifier_index = 0
                if specifier_original in column_coords_list:
                    specifier = coord_dict[specifier_original]
                    specifier_index = 1

                if piece_letter in letters_list:
                    if isinstance(piece, letter_dict[piece_letter]) and \
                            piece.location[specifier_index] == specifier:

                        if move_coord in piece.possible_moves():
                            piece_index = index
                            count += 1

    return piece_index, count


def checkmate_checker(current_turn_pieces, next_turn_pieces):
    check = False
    checkmate = True
    stalemate = True
    for piece in current_turn_pieces:
        if isinstance(piece, pieces.King):
            king_location = piece.location

    all_possible_moves = []
    for piece in next_turn_pieces:
        all_possible_moves += piece.possible_moves(True)

    if king_location in all_possible_moves:
        check = True
        stalemate = False
        # need to check for checkmate
        for piece in current_turn_pieces:
            piece_location = piece.location
            for move in piece.possible_moves():
                all_possible_moves_new = []
                original_piece = current_turn_pieces[0].board[move[0]][move[1]]
                piece.move_piece(move)
                for piece_king in current_turn_pieces:
                    # in case it was king that was moved
                    if isinstance(piece_king, pieces.King):
                        king_location_new = piece_king.location
                for piece_new in next_turn_pieces:
                    all_possible_moves_new += piece_new.possible_moves(True)
                if king_location_new not in all_possible_moves_new:
                    checkmate = False
                    piece.move_piece(piece_location)
                    current_turn_pieces[0].board[move[0]][move[1]] = original_piece
                    break
                piece.move_piece(piece_location)
                current_turn_pieces[0].board[move[0]][move[1]] = original_piece


    else:
        checkmate = False
        for piece in current_turn_pieces:
            piece_location = piece.location
            for move in piece.possible_moves():
                all_possible_moves_new = []
                original_piece = current_turn_pieces[0].board[move[0]][move[1]]
                piece.move_piece(move)
                for piece_king in current_turn_pieces:
                    # in case it was king that was moved
                    if isinstance(piece_king, pieces.King):
                        king_location_new = piece_king.location
                for piece_new in next_turn_pieces:
                    all_possible_moves_new += piece_new.possible_moves(True)
                if king_location_new not in all_possible_moves_new:
                    stalemate = False
                    piece.move_piece(piece_location)
                    current_turn_pieces[0].board[move[0]][move[1]] = original_piece
                    break
                piece.move_piece(piece_location)
                current_turn_pieces[0].board[move[0]][move[1]] = original_piece

    return check, checkmate, stalemate
