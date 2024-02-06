class GameSolution:
#     """
#         A class for solving the Water Sort game and finding solutions(normal, optimal).

#         Attributes:
#             ws_game (Game): An instance of the Water Sort game which implemented in game.py file.
#             moves (List[Tuple[int, int]]): A list of tuples representing moves between source and destination tubes.
#             solution_found (bool): True if a solution is found, False otherwise.

#         Methods:
#             solve(self, current_state):
#                 Find a solution to the Water Sort game from the current state.
#                 After finding solution, please set (self.solution_found) to True and fill (self.moves) list.

#             optimal_solve(self, current_state):
#                 Find an optimal solution to the Water Sort game from the current state.
#                 After finding solution, please set (self.solution_found) to True and fill (self.moves) list.
#     """
   def __init__(self, game):
        """
            Initialize a GameSolution instance.
            Args:
                game (Game): An instance of the Water Sort game.
        """
        self.ws_game = game  # An instance of the Water Sort game.
        self.moves = []  # A list of tuples representing moves between source and destination tubes.
        self.tube_numbers = game.NEmptyTubes + game.NColor  # Number of tubes in the game.
        self.solution_found = False  # True if a solution is found, False otherwise.
        self.visited_tubes = set()  # A set of visited tubes.

#     def check_victory(self, current_state):
#          for tube in current_state:
#             if len(tube) > 0 and tube[-1] != tube[0]:
#                 return False
#          self.solution_found = True
#          return True

#     def solve(self, current_state, moves=[]):
#         """
#         Find a solution to the Water Sort game from the current state using Depth-First Search (DFS).

#         Args:
#             current_state (List[List[int]]): A list of lists representing the colors in each tube.
#             moves (List[Tuple[int, int]]): A list of tuples representing moves between source and destination tubes.

#         This method attempts to find a solution to the Water Sort game by recursively exploring
#         different moves and configurations starting from the current state.
#         """

#         # Check if the current state is a winning state
#         if self.check_victory(current_state):
#             self.moves = moves  # Set the solution moves
#             self.solution_found = True  # Mark solution as found
#             return

#         # Generate possible moves from the current state
#         for source_tube in range(self.tube_numbers):
#          if len(current_state[source_tube]) == 0:
#                continue  # Skip empty source tubes
#          for dest_tube in range(self.tube_numbers):
#                 if source_tube != dest_tube :
#                     # Check if the destination tube has enough space for water
#                     if len(current_state[dest_tube]) < self.ws_game.NColorInTube:
#                         # Make a move by copying the current state and updating it
#                         new_state = [list(tube) for tube in current_state]
#                         color_to_move = new_state[source_tube][-1]  # Get the color to move

#                         # Find and group all units of the same color in the source tube
#                         units_to_move = [i for i, color in enumerate(new_state[source_tube]) if color == color_to_move]
#                         units_to_move.reverse()  # Reverse to move from bottom to top

#                         # Move the grouped units to the destination tube
#                         for unit_index in units_to_move:
#                             new_state[source_tube].pop(unit_index)
#                             new_state[dest_tube].append(color_to_move)

#                         new_moves = moves + [(source_tube, dest_tube)]

#                         # Check if the new state has not been visited before
#                         state_hash = tuple(tuple(tube) for tube in new_state)
#                         if state_hash not in self.visited_tubes:
#                             self.visited_tubes.add(state_hash)

#                             # Recursively call solve with the new state
#                             self.solve(new_state, new_moves)

#         # If the current state is not a winning state, and all moves have been explored, backtrack
#         return
   def check_victory(self, current_state):
        for tube in current_state:
            if len(tube) > 0 and tube[-1] != tube[0]:
                return False
        self.solution_found = True
        return True
   def solve(self, current_state, moves=[]):
        """
     Find a solution to the Water Sort game from the current state using Depth-First Search (DFS).

    Args:
        current_state (List[List[int]]): A list of lists representing the colors in each tube.
        moves (List[Tuple[int, int]]): A list of tuples representing moves between source and destination tubes.

    This method attempts to find a solution to the Water Sort game by recursively exploring
    different moves and configurations starting from the current state.
    """
    

    # Check if the current state is a winning state
        if self.check_victory(current_state):
         self.moves = moves  # Set the solution moves
         self.solution_found = True  # Mark solution as found
         return

    # Generate possible moves from the current state
        for source_tube in range(self.tube_numbers):
         if len(current_state[source_tube]) == 0:
            continue  # Skip empty source tubes

         for dest_tube in range(self.tube_numbers):
            if source_tube != dest_tube:
                # Check if the destination tube index is within the valid range
                if 0 <= dest_tube < self.tube_numbers:
                    print("Current State:", current_state)
                    print("Destination Tube:", dest_tube)
                    # Check if the destination tube has enough space for water
                if(dest_tube<4):
                    if len(current_state[dest_tube]) < self.ws_game.NEmptyTubes + self.ws_game.NColor:
                        # Make a move by copying the current state and updating it
                        new_state = [list(tube) for tube in current_state]
                        color_to_move = new_state[source_tube][-1]  # Get the color to move

                        # Find and group all units of the same color in the source tube
                        units_to_move = [i for i, color in enumerate(new_state[source_tube]) if color == color_to_move]
                        units_to_move.reverse()  # Reverse to move from bottom to top

                        # Move the grouped units to the destination tube
                        for unit_index in units_to_move:
                            new_state[source_tube].pop(unit_index)
                            new_state[dest_tube].append(color_to_move)

                        new_moves = moves + [(source_tube, dest_tube)]

                        # Check if the new state has not been visited before
                        state_hash = tuple(tuple(tube) for tube in new_state)
                        if state_hash not in self.visited_tubes:
                            self.visited_tubes.add(state_hash)

                            # Recursively call solve with the new state
                            self.solve(new_state, new_moves)

    # If the current state is not a winning state, and all moves have been explored, backtrack



   def optimal_solve(self, current_state):
        """
            Find an optimal solution to the Water Sort game from the current state.

            Args:
                current_state (List[List[int]]): A list of lists representing the colors in each tube.

            This method attempts to find an optimal solution to the Water Sort game by minimizing
            the number of moves required to complete the game, starting from the current state.
        """
        pass
