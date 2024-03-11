class ticTacToeMaster():
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.ai = "X"
        self.human = "O"
        self.empties = []

    def printBoard(self):
        print(" -----------")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print(" -----------")

    def emptyIndexes(self):
        self.empties = [i for i in range(9) if self.board[i] not in ["O", "X"]]

    def checkWinner(self, player):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        self.emptyIndexes()
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == player:
                return True
        return False

    def minimax(self, player):
        self.emptyIndexes()

        if self.checkWinner(self.human):
            return {'score': -1}
        elif self.checkWinner(self.ai):
            return {'score': 1}
        elif not self.empties:
            return {'score': 0}

        plays = []

        for index in self.empties:
            play = {}
            play['index'] = index
            self.board[index] = player

            if player == self.ai:
                result = self.minimax(self.human)
                play['score'] = result['score']
            else:
                result = self.minimax(self.ai)
                play['score'] = result['score']

            self.board[index] = ' '
            plays.append(play)

        if player == self.ai:
            bestScore = -float('inf')
            for play in plays:
                if play['score'] > bestScore:
                    bestScore = play['score']
                    bestPlay = play
        else:
            bestScore = float('inf')
            for play in plays:
                if play['score'] < bestScore:
                    bestScore = play['score']
                    bestPlay = play

        return bestPlay

    def play(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.human
            if self.checkWinner(self.human):
                print(f'Player {self.human} wins!')
                return True
            elif not any(cell == ' ' for cell in self.board):
                print("It's a draw!")
                return True
            else:
                aiMove = self.minimax(self.ai)['index']
                self.board[aiMove] = self.ai
                if self.checkWinner(self.ai):
                    print(f'Player {self.ai} wins!')
                    return True
                elif not any(cell == ' ' for cell in self.board):
                    print("It's a draw!")
                    return True
                return False
        else:
            print('Invalid move. Try again.')
            return False
# Create tictactoe game instance
game = ticTacToeMaster()


while True:
    # Print the board
    game.printBoard()

    # Player's turn
    while True:
        try:
            position = int(input("Enter your move (0-8): "))
            if 0 <= position <= 8 and game.board[position] == ' ':
                break
            else:
                print("Invalid move. Please enter a number between 0 and 8 for an empty cell.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    game.board[position] = game.human

    # Check if the game is over
    if game.checkWinner(game.human):
        game.printBoard()
        print(f'Player {game.human} wins!')
        break
    elif all(cell != ' ' for cell in game.board):
        game.printBoard()
        print("It's a draw!")
        break


    # AI's turn
    aiMove = game.minimax(game.ai)['index']
    game.board[aiMove] = game.ai

    # Check if the game is over
    if game.checkWinner(game.ai):
        game.printBoard()
        print("AI wins!")
        break
    '''
    Note: We dont need to check for a tie after AI's turn because board will always fill up on players turn, not the AI
    '''
