from random import choice


class TicTacToe:

    def __init__(self, p1, p2):
        self.__board = ['_' for _ in range(9)]
        self.player, self.pos, self.over, self.toss_winner, self.toss_loser = None, None, False, None, None
        self.winner, self.loser = None, None
        self.p1, self.p2 = p1, p2
        self.display()
        self.toss(self.p1, self.p2)
        while not self.over:
            for ___ in (self.toss_winner, self.toss_loser):
                self.play(___)
                self.over = self.win_check(___)
                if self.over is True:
                    break
                self.draw_check()
                if self.over is True:
                    break
        if self.winner is not None:
            print("{} has WON the game".format(self.winner))
        else:
            print("The Match is a Draw :-)")

    def display(self):
        for _, __ in enumerate(self.__board):
            print(__, end='         ')
            if (_ + 1) % 3 == 0:
                print('\n')

    def play(self, player):
        self.player = player
        valid = True
        self.pos = input("{}'s Turn! Enter a Position(1 to 9)\n".format(self.player)).strip()
        while valid:
            try:
                self.pos = int(self.pos)
                if self.pos < 1 or self.pos > 9:
                    raise IndexOutOfRange("Index Out of Range")
                elif self.__board[self.pos - 1] != '_':
                    raise ValueAlreadyPresent("That Position is already Taken")
            except IndexOutOfRange as IOR:
                print("Enter a Integer between 1 and 9", IOR.args, sep='    ')
                self.pos = input("Try Again {}. Enter a Position(1 to 9)\n".format(self.player)).strip()
            except ValueAlreadyPresent as VAP:
                print(VAP.args)
                self.display()
                self.pos = input("Try Again {}. Enter a Position(1 to 9)\n".format(self.player)).strip()
            except ValueError:
                print("Enter a Valid Integer")
                self.pos = input("Try Again {}. Enter a Position(1 to 9)\n".format(self.player)).strip()
            else:
                valid = False
                print("{} player marked {}".format(self.player, self.pos))
                self.__board[self.pos-1] = self.player
                self.display()

    def toss(self, p1, p2):
        print("{} calls the toss and {} has to flip the coin".format(p1, p2))
        toss_call = input("Enter Your Toss Call {}\n".format(p1)).strip()
        while True:
            if toss_call.lower() in ['h', 'head', 'heads']:
                print("{} has called for HEADS".format(p1))
                toss_called = "Heads"
                break
            elif toss_call.lower() in ['t', 'tail', 'tails']:
                print("{} has called for TAILS".format(p1))
                toss_called = "Tails"
                break
            else:
                toss_call = input("Enter a Valid Toss Call {}\n".format(p1))
        toss_outcome = choice(["Heads", "Tails"])
        print("Toss Outcome was {} and {} had called {}".format(toss_outcome, p1, toss_called))
        if toss_outcome == toss_called:
            print("{} has WON the Toss".format(p1))
            self.toss_winner, self.toss_loser = p1, p2
        else:
            print("{} has WON the Toss".format(p2))
            self.toss_winner, self.toss_loser = p2, p1

    def win_check(self, p):
        win_cells = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for _ in win_cells:
            cells = 0
            for __ in _:
                if self.__board[__] == p:
                    cells += 1
                else:
                    break
                if cells == 3:
                    self.winner = p
                    return True

    def draw_check(self):
        cells = 0
        for _ in self.__board:
            if _ == '_':
                cells += 1
        if cells == 0:
            self.over = True
            self.winner = None


class IndexOutOfRange(IndexError):
    def __init__(self, message):
        super().__init__(message)


class ValueAlreadyPresent(ValueError):
    def __init__(self, message):
        super().__init__(message)


if __name__ == '__main__':
    B = TicTacToe('X', 'O')
    print(B._TicTacToe__board)