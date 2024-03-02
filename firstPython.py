rock = '''
    ________
---'(________)
    (________)
    (________)
----(_______)  

'''
paper = '''

    _______
---'_________)
    __________)
--- ________)
    ____)
'''
scissors = '''
    ____
---'____)_____
     __________)
    __________)
--- _____)
    _____)
'''
import random 
game_images = [rock, paper, scissors]
user_choics = int(input("welcom to rock paper scissors game\nplease chose your item. \n"))
print(game_images[user_choics])
print(f"you chose{user_choics}")
computer_choics = random.randint(0,2)
print(f"computer chose.{computer_choics}")
print(game_images[computer_choics])
if computer_choics < user_choics:
    print("you win")
elif computer_choics == rock and user_choics == paper:
    print("computer win")
else:
    print("you lose")