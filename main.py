# text-based version of tic-tac-toe

class Board:
    def __init__(self):
        self.moves = [' ' for _ in range(9)]
        self.board = ""

    def update_board(self):
        self.board = f" {self.moves[0]} | {self.moves[1]} | {self.moves[2]} \n" \
                     f"-----------\n" \
                     f" {self.moves[3]} | {self.moves[4]} | {self.moves[5]} \n" \
                     f"-----------\n" \
                     f" {self.moves[6]} | {self.moves[7]} | {self.moves[8]} \n"

    def display_board(self):
        print(self.board)

    def check_if_over(self) -> bool:
        for i in range(3):
            if (self.moves[i] == self.moves[i+1] == self.moves[i+2]) and self.moves[i] != ' ':
                print("exit 1")
                return True
            if (self.moves[i] == self.moves[i+3] == self.moves[i+6]) and self.moves[i] != ' ':
                print("exit 2")
                return True
        if (self.moves[0] == self.moves[4] == self.moves[8]) and self.moves[0] != ' ':
            print("exit 3")
            return True
        if (self.moves[2] == self.moves[4] == self.moves[6]) and self.moves[2] != ' ':
            print("exit 4")
            return True
        return False

    def check_move(self, move):
        options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if self.moves[move] == ' ' and move in options:
            return True
        return False


board = Board()

while True:
    print("\nWelcome to Tic-Tac-Toe!\n")
    print("Player 1, you are X's")
    print("Player 2, you are O's")

    while True:
        move1 = int(input("Player 1, make a move (enter 0-8): "))
        while not board.check_move(move1):
            print("That space is already taken or you entered an invalid number.")
            move1 = int(input("Please enter another: "))
        board.moves[move1] = "X"
        board.update_board()
        board.display_board()
        if board.check_if_over():
            winner = "Player 1"
            break

        move2 = int(input("Player 2, make a move (enter 0-8): "))
        while not board.check_move(move2):
            move2 = int(input("That space is already taken. Please enter another: "))
        board.moves[move2] = "O"
        board.update_board()
        board.display_board()
        if board.check_if_over():
            winner = "Player 2"
            break

    print(f"Congrats {winner}! You won!")
    board.moves = [' ' for _ in range(9)]
    play_again = input("Would you like to play again? (enter y/n): ")
    if play_again == "n":
        break
