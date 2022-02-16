import random
import math # yes the code didnt used math but its the way i used on video, i dont want to send a different code only to github.

# chars
boom = '💥'
money = '💲'
trident = '⚜'

charList1 = {0:boom, 1:money, 2:trident}
charList2 = {0:boom, 1:money, 2:trident}
charList3 = {0:boom, 1:money, 2:trident}

# table
row1 = {0:'0', 1:'0', 2:'0'}
row2 = {0:'0', 1:'0', 2:'0'}
row3 = {0:'0', 1:'0', 2:'0'}

# game
def game():
    print(f"""[ {row1[0]} ] [ {row1[1]} ] [ {row1[2]} ]\n[ {row2[0]} ] [ {row2[1]} ] [ {row2[2]} ]\n[ {row3[0]} ] [ {row3[1]} ] [ {row3[2]} ]""")
    firstOption = input("Want to roll?\n> ")
    if firstOption == "y" or firstOption == "yes":
        randomize()
    elif firstOption == "n" or firstOption == "no":
        exit()
    else:
        return print("Invalid option")
        game()

# Randomize / Shuffle the rows
def randomize():
    # first shuffle
    random.shuffle(charList1)
    row1[0] = charList1[0]
    row1[1] = charList1[1]
    row1[2] = charList1[2]
    # second suffle
    random.shuffle(charList2)
    row2[0] = charList2[0]
    row2[1] = charList2[1]
    row2[2] = charList2[2]
    # third shuffle
    random.shuffle(charList3)
    row3[0] = charList3[0]
    row3[1] = charList3[1]
    row3[2] = charList3[2]
    
    checkSame()
    game()

# Check if a row is the same
def checkSame():
    if row1[0] == row2[0] and row2[0] == row3[0] and row1[0] == row3[0]:
        return print("First row is the same! You won the game!")
    elif row1[1] == row2[1] and row2[1] == row3[1] and row1[1] == row3[1]:
        return print("Second row is the same! You won the game!")
    elif row2[2] == row2[2] and row2[2] == row3[2] and row1[2] == row3[2]:
        return print("Third row is the same! You won the game!")
    else:
        pass

game()
