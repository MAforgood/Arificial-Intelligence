# # import numpy as np
# # import game_functions as gf

# # def evaluate_state(board: np.ndarray) -> float:
# #     """
# #     Returns the score of the given board state.
# #     :param board: The board state for which the score is to be calculated.
# #     :return: The score of the given board state.
# #     """
# #     # Feature weights (you can adjust these as needed)
# #     monotonicity_weight = 2.0
# #     smoothness_weight = 0.5
# #     free_tiles_weight = 0.5

# #     # Calculate feature values
# #     monotonicity = calculate_monotonicity(board)
# #     smoothness = calculate_smoothness(board)
# #     free_tiles = calculate_free_tiles(board)

# #     # Calculate the overall score using the linear combination of features and weights
# #     score = (
# #         monotonicity_weight * monotonicity +
# #         smoothness_weight * smoothness +
# #         free_tiles_weight * free_tiles
# #     )

# #     return score

# # def calculate_monotonicity(board: np.ndarray) -> float:
# #     """
# #     Calculate the monotonicity of the board.
# #     """
# #     monotonicity = 0

# #     for i in range(board.shape[0]):
# #         row_values = board[i, :]
# #         monotonicity += calculate_monotonicity_in_array(row_values)

# #     for j in range(board.shape[1]):
# #         col_values = board[:, j]
# #         monotonicity += calculate_monotonicity_in_array(col_values)

# #     return monotonicity

# # def calculate_monotonicity_in_array(array: np.ndarray) -> float:
# #     """
# #     Calculate the monotonicity in a 1D array.
# #     """
# #     monotonicity = 0

# #     non_zero_indices = np.nonzero(array)[0]

# #     for k in range(1, len(non_zero_indices)):
# #         prev_index = non_zero_indices[k - 1]
# #         current_index = non_zero_indices[k]

# #         monotonicity += abs(array[prev_index] - array[current_index])

# #     return monotonicity

# # def calculate_smoothness(board: np.ndarray) -> float:
# #     """
# #     Calculate the smoothness of the board.
# #     """
# #     smoothness = 0

# #     for i in range(board.shape[0]):
# #         for j in range(board.shape[1]):
# #             if board[i, j] != 0:
# #                 # Find the closest non-zero tile in the same row
# #                 right_neighbor = find_next_non_zero(board, i, j, direction='right')
# #                 # Find the closest non-zero tile in the same column
# #                 down_neighbor = find_next_non_zero(board, i, j, direction='down')

# #                 # Calculate smoothness based on the absolute difference
# #                 smoothness -= abs(board[i, j] - right_neighbor)
# #                 smoothness -= abs(board[i, j] - down_neighbor)

# #     return smoothness

# # def find_next_non_zero(board: np.ndarray, row: int, col: int, direction: str) -> int:
# #     """
# #     Find the closest non-zero tile in the specified direction.
# #     """
# #     if direction == 'right':
# #         for j in range(col + 1, board.shape[1]):
# #             if gf.within_bounds((row, j)) and board[row, j] != 0:
# #                 return board[row, j]
# #     elif direction == 'down':
# #         for i in range(row + 1, board.shape[0]):
# #             if gf.within_bounds((i, col)) and board[i, col] != 0:
# #                 return board[i, col]

# #     return 0  # If no non-zero tile is found in the specified direction

# # def calculate_free_tiles(board: np.ndarray) -> float:
# #     """
# #     Calculate the number of free tiles in the board.
# #     """
# #     free_tiles = np.count_nonzero(board == 0)
# #     return free_tiles
# # import numpy as np
# # import game_functions as gf
# # weight_matrix = np.array([
# #     [327680, 16384, 8192, 4096],
# #     [163840, 8192, 4096, 2048],
# #     [81920, 4096, 2048, 1024],
# #     [4096, 2048, 1024, 512]
# # ])
# # def evaluate_state(board: np.ndarray) -> float:
# #     score_weighted = 0
# #     score_clusters = 0

# #     # Calculate weighted score using the weight matrix
# #     for i in range(len(board)):
# #         for j in range(len(board[i])):
# #             score_weighted += board[i][j] * weight_matrix[i][j]

# #     # Calculate penalty for clusters of equal-valued tiles
# #     for i in range(len(board)):
# #         for j in range(len(board[i]) - 1):
# #             if board[i][j] == board[i][j + 1]:
# #                 score_clusters -= board[i][j]  # Subtract a penalty for each adjacent pair

# #     for j in range(len(board[0])):
# #         for i in range(len(board) - 1):
# #             if board[i][j] == board[i + 1][j]:
# #                 score_clusters -= board[i][j]  # Subtract a penalty for each adjacent pair

# #     # Combine the scores with a weighting factor
# #     total_score = 0.95 * score_weighted + 0.05 * score_clusters

# #     return total_score


# import numpy as np
# import game_functions as gf

# def evaluate_state(board: np.ndarray) -> float:
#     # Component 1: Sum of board values
#     score_sum = np.sum(board)

#     # Component 2: Bonus for large tiles in corners
#     corner_bonus = np.sum([board[i, j] for i in [0, -1]
#                            for j in [0, -1] if gf.within_bounds((i, j))])
#     score_sum += corner_bonus * 10

#     # Component 3: Penalty for adjacent tiles with large differences
#     for i in range(gf.CELL_COUNT):
#         for j in range(gf.CELL_COUNT):
#             current_value = board[i, j]

#             for ni, nj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
#                 if gf.within_bounds((ni, nj)):
#                     neighbor_value = board[ni, nj]
#                     if neighbor_value != 0:
#                         score_sum -= abs(current_value - neighbor_value)

#     # Component 4: Weighted score using the weight matrix
#     weight_matrix = np.array([
#         [327680, 16384, 8192, 4096],
#         [163840, 8192, 4096, 2048],
#         [81920, 4096, 2048, 1024],
#         [4096, 2048, 1024, 512]
#     ])
#     score_weighted = np.sum(board * weight_matrix)

#     # Component 5: Penalty for clusters of equal-valued tiles
#     score_clusters = 0
#     for i in range(len(board)):
#         for j in range(len(board[i]) - 1):
#             if board[i][j] == board[i][j + 1]:
#                 score_clusters -= board[i][j]  # Subtract a penalty for each adjacent pair

#     for j in range(len(board[0])):
#         for i in range(len(board) - 1):
#             if board[i][j] == board[i + 1][j]:
#                 score_clusters -= board[i][j]  # Subtract a penalty for each adjacent pair

#     # Combine the scores with weighting factors
#     weight_sum = 0.2
#     weight_clusters = 0.5
#     weight_weighted = 0.3
#     total_score = (
#         weight_sum * score_sum +
#         weight_clusters * score_clusters +
#         weight_weighted * score_weighted
#     )

#     return total_score
import numpy as np
import game_functions as gf
def evaluate_state(board: np.ndarray) -> float:
    # S-shaped weight matrix
    weight_matrix = np.array([
        [4096, 2048, 1024, 512],
        [32, 64, 128, 256],
        [16, 8, 4, 2],
        [0.125, 0.25, 0.5, 1]
    ])
    score = np.sum(board )

    # Bonus for large tiles
    max_tile = np.max(board)
    score += max_tile * 2

    # Penalty for empty cells
    empty_cells = np.count_nonzero(board == 0)
    score += empty_cells * 3

    # Penalty for adjacent tiles with large differences
    for i in range(3):
        for j in range(3):
            current_value = board[i, j]

            for ni, nj in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
                if 0 <= ni < 4 and 0 <= nj < 4:
                    neighbor_value = board[ni, nj]
                    if neighbor_value != 0:
                        score -= abs(current_value - neighbor_value)

    return score