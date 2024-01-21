class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Represent the game board as a list
        self.current_player = "X"  # Start with player X
        self.winner = None  # Will be set to the winning player if there's a winner

    def display_board(self):
        """Display the current state of the board."""
        print(f" {self.board[0]}(1) | {self.board[1]}(2) | {self.board[2]}(3) ")
        print("-----------")
        print(f" {self.board[3]}(4) | {self.board[4]}(5) | {self.board[5]}(6) ")
        print("-----------")
        print(f" {self.board[6]}(7) | {self.board[7]}(8) | {self.board[8]}(9) ")

    def make_move(self, position):
        """Make a move on the board."""
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.check_winner()
            self.switch_player()
        else:
            print("Invalid move. The position is already taken.")

    def switch_player(self):
        """Switch the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if there is a winner."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combo in winning_combinations:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                and self.board[combo[0]] != " "
            ):
                self.winner = self.current_player

    def is_board_full(self):
        """Check if the board is full."""
        return " " not in self.board

    def play_game(self):
        """Play the Tic-Tac-Toe game."""
        while not self.winner and not self.is_board_full():
            self.display_board()
            position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
            if 0 <= position <= 8:
                self.make_move(position)
            else:
                print("Invalid move. Please enter a number between 1 and 9.")

        self.display_board()
        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a tie! The board is full.")

# Create an instance of the TicTacToe class and play the game
game = TicTacToe()
game.play_game()
