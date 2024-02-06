from game import Game
from ai_solution import GameSolution

if __name__ == "__main__":
    # game = Game()
    # game.run_game()
 game = Game()
 initial_state=[[],[1,2],[2,2]]
 solver=GameSolution(game)
 solver.solve(initial_state)
 if solver.solution_found:
    print("Solution found!")
    print("Moves:", solver.moves)
 else:
    print("No solution found.")