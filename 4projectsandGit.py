# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
correct_password = 'QAE'
current_password = input('ENTER THE PASSWORD:')
while correct_password != current_password:
    print('INCORRECT PASSWORD TRY AGAIN:')
    current_password = input('ENTER THE PASSWORD:')
else:
    print('Welcome')

string_1 = 'This is totally random'
char_1 = input('Enter the character that you want to count:')
result_1= 0
current_index=0
while current_index < len(string_1):
    if string_1[current_index]== char_1:
        result_1 += 1
    current_index += 1
else:
    print(f'Current index is at it\'s last position # {current_index},the loop has stopped. ')

    print(f'The character {char_1} occurs {result_1} times\U0001F913')



    ''' We will make the board using dictionary 
         in which keys will be the location(i.e : top-left,mid-right,etc.)
        and initialliy it's values will be empty space and then after every move 
        we will change the value according to player's choice of move. '''

    theBoard = {'7':' ' ,'8': ' ' ,'9':' ',
               '4':' ' ,'5': ' ' ,'6':' ',
               '1':' ' ,'2': ' ' ,'3':' '}

    board_keys =[]

    for key in theBoard:
       board_keys.append(key)

    def printboard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print( '-+-+-' )
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-' )
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    def game():

        turn = 'X'
        count = 0


        for i in range(10):
            printboard(theBoard)
            print("It's your turn," + turn +".Move to which area?")

            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That area is already filled.\nMove to which area ?")
                continue

            if count >= 5:

                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['9']== theBoard['6'] == theBoard['3'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break
                elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                    printboard(theBoard)
                    print("\Game 0ver.\n")
                    print("****" + turn + " won.****")
                    break

            if count == 9:
                print("\Game 0ver.\n")
                print("It's a Tie!!")

            if turn =='X':
                turn ='0'
            else:
                turn ='X'




        restart  = input("Do you want to play Again?(y/n)")
        if restart =="y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = " "

            game()

    if __name__ == "__main__":
        game()