Knight Minimizer on Chess Board
Overview
This Python-based project provides a solution to reduce conflicts on a chess board by strategically removing knights. Knights threaten each other based on their unique L-shaped movement capabilities. The goal of this application is to minimize these threats by removing knights until no knight can attack another.

Features
Interactive Input: Users can define the size of the chess board and the initial positions of the knights.
Conflict Resolution: The application calculates potential conflicts and identifies knights that threaten the most peers.
Optimized Knight Removal: Implements a greedy algorithm to remove knights causing the most conflicts, efficiently updating the board state to reflect each change.
Output Visualization: Displays the updated board after all operations, showing remaining knights and positions from which knights have been removed.
How to Run
Clone the repository to your local machine.
Ensure Python 3.x is installed.
Run the script via the command line with python knights_chess_board.py.
Follow the on-screen prompts to input the chess board size and initial knight positions.
View the output directly in the terminal.
Contributing
Contributions to the project are welcome! Whether you have fixes for bugs, proposals for optimization, or additional features, please feel free to fork the repository, make changes, and submit a pull request.
