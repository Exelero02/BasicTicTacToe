class TicTacToe:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.board = []
        self.game_over = False

    def initialize_board(self, size):
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (len(row) * 2 - 1))

    def get_input(self):
        while True:
            try:
                row = int(input("Enter row number (1 to {}): ".format(len(self.board)))) - 1
                col = int(input("Enter column number (1 to {}): ".format(len(self.board)))) - 1
                if 0 <= row < len(self.board) and 0 <= col < len(self.board) and self.board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid input! Please choose an empty cell.")
            except ValueError:
                print("Invalid input!")

    def check_winner(self):
        lines = self.board + list(zip(*self.board)) + [[self.board[i][i] for i in range(len(self.board))]] + [
            [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]]
        for line in lines:
            if all(cell == line[0] and cell != ' ' for cell in line):
                self.game_over = True
                return True
        if all(cell != ' ' for row in self.board for cell in row):
            self.game_over = True
            return False
        return False

    def run(self):
        size = int(input("Enter the size of the game grid (5-25): "))
        if size < 5:
            print("Minimum grid size is 5")
            return
        self.initialize_board(size)

        while not self.game_over:
            print("Current Player: {}".format(self.players[self.current_player_index][0]))
            self.display_board()
            row, col = self.get_input()
            self.board[row][col] = self.players[self.current_player_index][1]
            if self.check_winner():
                self.display_board()
                if self.game_over:
                    print("Game Over!")
                    if self.check_winner() is False:
                        print("Draw!")
                    else:
                        print("Player {} wins!".format(self.players[self.current_player_index][0]))
                break
            self.current_player_index = (self.current_player_index + 1) % len(self.players)


if __name__ == "__main__":
    players = []
    num_players = int(input("Enter the number of players (2 to 4): "))
    for i in range(num_players):
        name = input("Enter name for Player {}: ".format(i + 1))
        symbol = input("Enter symbol for Player {} (e.g., X, O, #, @): ".format(i + 1))
        players.append((name, symbol))
    TicTacToe(players).run()
