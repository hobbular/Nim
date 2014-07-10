import random

#############################################
# Game board class
#############################################
class GameBoard:
    board = [['|','|','|','|','|'],
             ['|','|','|','|'],
             ['|','|','|'],
             ['|','|']]
    sticks = [5,4,3,2]
    human_move = True    # this is how we'll track whose turn it is
    
    #############################################
    # Displays the current state of the board
    #############################################
    def display(self):
        print
        space_count = 0
        for line in self.board:
            print str(space_count+1)+": "+(space_count*' '),
            for item in line:
                print item,
            print (space_count*' ')+" ("+str(self.sticks[space_count])+")"
            space_count += 1
        print

    #############################################
    # Changes the board based on the chosen move.
    # If the move was illegal, returns False.
    #############################################
    def make_move(self,pile,count):
        if not '|' in self.board[pile] or count == 0:
            # tried to take sticks from an empty pile
            return False
        # remove UP TO count sticks from pile
        removed = 0
        index = 0
        while removed < count and '|' in self.board[pile]:
            # find a stick to remove
            while self.board[pile][index] != '|':
                index += 1
            # remove it
            self.board[pile][index] = ' '
            removed += 1
        self.sticks[pile] -= removed
        return True

    #############################################
    # Count number of sticks in a given row
    #############################################
    def count_sticks(line):
        return sum(1 for x in line if x == '|')

    #############################################
    # Count number of sticks left on the board
    #############################################
    def count_board(self):
        return sum(x for x in self.sticks)

    #############################################
    # Determines whether the board is empty
    #############################################
    def is_empty(self):
        return '|' in self.board[0] or '|' in self.board[1] or '|' in self.board[2] or '|' in self.board[3]

#############################################
# My variables for my game
#############################################
board = GameBoard()
num_piles = len(board.board)

#############################################
# PLAY THE GAME!!
#############################################
while board.count_board() > 0:
    board.display()

    # if it's the human's turn:
    while board.human_move:
        pile_num = int(raw_input("pick a pile 1-"+str(num_piles)+": "))
        while pile_num < 1 or pile_num > num_piles:
            pile_num = int(raw_input("that's not one of the options: "))
        pile_num -= 1
        if board.sticks[pile_num] == 0:
            print "You can't remove sticks from an empty pile!"
            continue
        how_many = int(raw_input("how many sticks: "))
        while how_many < 1:
            how_many = int(raw_input("nice try. gotta pick up at least one: "))
        success = board.make_move(pile_num,how_many)
        if success:
            break
    
    # if it's the computer's turn:
    while not board.human_move:
        pile_num = random.randint(0,3)
        while board.sticks[pile_num] == 0:
            pile_num = random.randint(0,3)
        if board.count_board() == board.sticks[pile_num]+1:
            # if it's about to win, have it take everything in that pile
            how_many = board.sticks[pile_num]+1
        else:
            how_many = random.randint(1,board.sticks[pile_num])
        success = board.make_move(pile_num,how_many)
        if success:
            print "Computer removed",how_many,"sticks from pile",pile_num+1
            break

    # switch whose turn it is
    board.human_move = not board.human_move

#############################################
# WHO WON???
#############################################
if board.human_move:
    # the computer had the last move and picked up the last stick
    print "You win!"
    print "I AM DELETING SYSTEM 32"
else:
    # you had to pick up the last stick
    print "You lose! YOU SUCK"
