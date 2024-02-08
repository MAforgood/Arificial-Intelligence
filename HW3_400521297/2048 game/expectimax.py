import numpy as np

import evaluation
import game_functions as gf


class Expectimax:
    def __init__(self, board):
        self.DEPTH_BASE_PARAM = 3 # You may change this parameter to scale the depth to which the agent searches.
        self.SCALER_PARAM = 400 # You may change this parameter to scale depth to which the agent searches.
        self.board = board

    def get_depth(self, move_number):
        """
        Returns the depth to which the agent should search for the given move number.
        ...
        :type move_number: int
        :param move_number: The current move number.
        :return: The depth to which the agent should search for the given move number.
        """
        # TODO: Complete get_depth function to return the depth to which the agent should search for the given move number.
        # Hint: You may need to use the DEPTH_BASE_PARAM constant.
        # empty_cells = np.count_nonzero(self.board == 0)
        # if(empty_cells >13):
        #     return 6
        base_depth = self.DEPTH_BASE_PARAM
        increased_depth = base_depth + int(move_number / self.SCALER_PARAM)
        return increased_depth

    def ai_move(self, board, move_number):
        depth = self.get_depth(move_number)
        score, action = self.expectimax(board, depth, 1)
        return action

    def expectimax(self, board: np.ndarray, depth: int, turn: int):
        """
        Returns the best move for the given board state and turn.
        ...
        :type turn: int
        :type depth: int
        :type board: np.ndarray
        :param board: The board state for which the best move is to be found.
        :param depth: Depth to which agent takes actions for each move
        :param turn: The turn of the agent. 1 for AI, 0 for computer.
        :return: Returns the best move and score we can obtain by taking it, for the given board state and turn.
        """
        
        # TODO: Complete expectimax function to return the best move and score for the given board state and turn.
        # Hint: You may need to implement minimizer_node and maximizer_node functions.
        # Hint: You may need to use the evaluation.evaluate_state function to score leaf nodes.
        # Hint: You may need to use the gf.terminal_state function to check if the game is over.
        
        if gf.terminal_state(board) or depth == 0:
            return evaluation.evaluate_state(board), None

        if turn == 1:  # Maximizing player (AI)
            return self.maximizer_node(board, depth)
        else:  # Minimizing player (Computer)
            return self.chance_node(board, depth)


    def maximizer_node(self, board: np.ndarray, depth: int):
        """
        Returns the best move for the given board state and turn.
        ...
        :type depth: int
        :type board: np.ndarray
        :param board: The board state for which the best move is to be found.
        :param depth: Depth to which agent takes actions for each move
        :return: Returns the move with highest score, for the given board state.
        """
        
        # TODO: Complete maximizer_node function to return the move with highest score, for the given board state.
        # Hint: You may need to use the gf.get_moves function to get all possible moves.
        # Hint: You may need to use the gf.add_new_tile function to add a new tile to the board.
        # Hint: You may need to use the np.copy function to create a copy of the board.
        # Hint: You may need to use the np.inf constant to represent infinity.
        # Hint: You may need to use the max function to get the maximum value in a list.
        
       
        max_score = -np.inf
        best_move = None
            
        moves=gf.get_moves()
            
        for move in moves:
            new_board, move_made, _=move(board)
            if move_made:
                score, _ = self.expectimax(new_board, depth - 1, turn=0)
                if score > max_score:
                    max_score = score
                    best_move = move

        return max_score, best_move

        # #all_possible_moves = gf.get_all_possible_moves(board)
        # best_move, _ = get_max_score_move( board, depth)
        # return best_move,_


    # def minimizer_node(self, board: np.ndarray, depth: int):
    #     """
    #     Returns the best move for the given board state and turn.
    #     ...
    #     :type depth: int
    #     :type board: np.ndarray
    #     :param board: The board state for which the best move is to be found.
    #     :param depth: Depth to which agent takes actions for each move
    #     :return: Returns the move with lowest score, for the given board state.
    #     """

    #     def get_min_score_move(empty_cells, current_board, current_depth):
    #         min_score = np.inf
    #         best_move = None

    #         for cell in empty_cells:
    #             for value in [2, 4]:
    #                 child_board = np.copy(current_board)
    #                 child_board[cell[0], cell[1]] = value
    #                 _, score = self.maximizer_node(child_board, current_depth - 1)

    #                 if score < min_score:
    #                     min_score = score
    #                     best_move = (cell[0], cell[1], value)

    #         return best_move, min_score
        

    #     empty_cells = np.transpose(np.nonzero(board == 0))  # Get indices of empty cells
    #     best_move, _ = get_min_score_move(empty_cells, board, depth)
    #     return best_move

    def chance_node(self, board: np.ndarray, depth: int):
        """
        Returns the expected score for the given board state and turn.
        ...
        :type depth: int
        :type board: np.ndarray
        :param board: The board state for which the expected score is to be found.
        :param depth: Depth to which agent takes actions for each move
        :return: Returns the expected score for the given board state.
        """
        
        # TODO: Complete chance_node function to return the expected score for the given board state.
        # Hint: You may need to use the gf.get_empty_cells function to get all empty cells in the board.
        # Hint: You may need to use the gf.add_new_tile function to add a new tile to the board.
        # Hint: You may need to use the np.copy function to create a copy of the board.
        
        empty_cells = gf.get_empty_cells(board)
        total_score = 0

        for cell in zip(empty_cells[0], empty_cells[1]):
            for tile_val in [2, 4]:
                new_board = np.copy(board)
                new_board[cell] = tile_val

                score, _ = self.expectimax(new_board, depth - 1, 1)
                total_score += score * 0.9 if tile_val == 2 else score * 0.1

        return total_score, None

        # empty_cells = gf.get_empty_cells(board)
        # expected_score = calculate_expected_score(empty_cells, board, depth)

        # return expected_score, None
        
        
