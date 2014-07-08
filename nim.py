import random

#############################################
# My variables for my game
#############################################
board = [['|','|','|','|','|'],
         ['|','|','|','|'],
         ['|','|','|'],
         ['|','|']]

human_move = True    # this is how we'll track whose turn it is

#############################################
# Displays the current state of the board
#############################################
def display_board(board):
    print
    space_count = 0
    for line in board:
        print str(space_count+1)+": "+(space_count*' '),
        for item in line:
            print item,
        print (space_count*' ')+" ("+str(count_sticks(line))+")"
        space_count += 1
    print

#############################################
# Changes the board based on the chosen move.
# If the move was illegal, returns False.
#############################################
def make_move(board,pile,count):
    if not '|' in board[pile] or count == 0:
        # tried to take sticks from an empty pile
        return False
    # remove UP TO count sticks from pile
    removed = 0
    index = 0
    while removed < count and '|' in board[pile]:
        # find a stick to remove
        while board[pile][index] != '|':
            index += 1
        # remove it
        board[pile][index] = ' '
        removed += 1
    return True

#############################################
# Count number of sticks in a given row
#############################################
def count_sticks(line):
    return sum(1 for x in line if x == '|')

#############################################
# Count number of sticks left on the board
#############################################
def count_board(board):
    return sum(count_sticks(board[x]) for x in range(len(board)))

#############################################
# PLAY THE GAME!!
#############################################
while '|' in board[0] or '|' in board[1] or '|' in board[2] or '|' in board[3]:
    display_board(board)

    # if it's the human's turn:
    while human_move:
        pile_num = int(raw_input("pick a pile 1-4: "))
        while pile_num < 1 or pile_num > 4:
            pile_num = int(raw_input("that's not one of the options: "))
        how_many = int(raw_input("how many sticks: "))
        while how_many < 1:
            how_many = int(raw_input("nice try. gotta pick up at least one: "))
        pile_num -= 1
        success = make_move(board,pile_num,how_many)
        if success:
            break
        print "You can't remove sticks from an empty pile!"
    
    # if it's the computer's turn:
    while not human_move:
        pile_num = random.randint(0,3)
        while count_sticks(board[pile_num]) == 0:
            pile_num = random.randint(0,3)
        if count_board(board) == count_sticks(board[pile_num])+1:
            # if it's about to win, have it take everything in that pile
            how_many = count_sticks(board[pile_num])
        else:
            how_many = random.randint(1,count_sticks(board[pile_num]))
        success = make_move(board,pile_num,how_many)
        if success:
            print "Computer removed",how_many,"sticks from pile",pile_num+1
            break

    # switch whose turn it is
    human_move = not human_move

#############################################
# WHO WON???
#############################################
if human_move:
    # the computer had the last move and picked up the last stick
    print "You win!"
else:
    # you had to pick up the last stick
    print "You lose!"
