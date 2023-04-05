import random
import sys
import time
n=[i for i in range(1,10)]
board=[" " for j in range(9)]
print("TIC-TAC-TOE")
print()
def print_board():
    row1="| {} | {} | {} |".format(board[0],board[1],board[2])
    row2="| {} | {} | {} |".format(board[3],board[4],board[5])
    row3="| {} | {} | {} |".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move_human(icon):
    if icon=="X":
        number="HUMAN"
    elif icon=="O" :
        number="COMPUTER"
    print("your turn player {}".format(number))
    choice1=int(input("enter ur move(1-9) :").strip())
    if choice1 >0 and choice1 <=9:
        if board[choice1-1] ==" ":
            board[choice1-1]=icon
        else:
            print()
            print("the space is occupied")
            print()
            player_move_human(icon)
    else:
        print("Invalid Move")
        player_move_human(icon)
def player_move_computer(icon):
    n1=random.choice(n)
    print("computer turn")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if board[n1-1]==" ":
        board[n1-1]=icon
    else :
        print()
        print("the space occupied")
        player_move_computer(icon)
def victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or (board[3]==icon and board[4]==icon and board[5]==icon) or (board[6]==icon and board[7]==icon and board[8]==icon) or (board[0]==icon and board[4]==icon and board[8]==icon) or (board[2]==icon and board[4]==icon and board[6]==icon) or (board[0]==icon and board[3]==icon and board[6]==icon) or (board[1]==icon and board[4]==icon and board[7]==icon) or (board[2]==icon and board[5]==icon and board[8]==icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    ch=int(input("which mode u want play \n 1.computer vs player \n"))
    if ch==1:
        while True:
            print_board()
            player_move_human("X")
           
            if victory("X"):
                print("player Human wins game")
                sys.exit()
                print()
            elif is_draw():
                print("it is draw")
                print()
                sys.exit()
            print_board()
            player_move_computer("O")
            if victory("O"):
                print("player Computer wins")
                print()
                sys.exit()

            elif is_draw():
                print("it is a draw")
                sys.exit()
                print()
    elif ch==2:
        while True:
            print_board()
            player_move_human("X")
            
            if victory("X"):
                print("player Human wins game")
                print()
            elif is_draw():
                print("it is draw")
                print()
            print_board()
            player_move_human("O")
            
            if victory("O"):
                print_board()
                print("player human wins")
                sys.exit()
                print()
            elif is_draw():
                print("it is a draw")
                sys.exit()
                print()
        
            
            
    else:
        print("enter again: ")
