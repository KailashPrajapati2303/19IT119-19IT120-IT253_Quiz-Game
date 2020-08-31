import json
import random
import getpass

user = []

def play():
    print('=============START GAME===============')
    print('enter a subject :')


def About():
    print('=============ABOUT===============')
    print('This project criated by Kailash prajapati and Savan prajapati\n2nd Semester Project ')

def Rules():
    print('=========HOW TO PLAY THE GAME==========')
    print('start the game and choose any subject in give Answer')
def Score():
    print('=============SCORE===============')
    Score=0
    print(Score)

if __name__ == "__main__":
	choice = 1
while choice !=5:
         print('=============QUIZ GAME===============')
         print('           1. START QUIZ')
         print('           2. VIEW SCORE')
         print('           3. ABOUT THE GAME')
         print('           4. HOW TO PLAY THE GAME')
         print('           5. EXIT')
         choice = int(input('\nEnter your choice'))
         if choice == 1:
             play()
         elif choice == 2:
             Score()
         elif choice == 3:
             About()
         elif choice == 4:
             Rules()
         elif choice == 5:
             break
         else:
             print('Your choice is wrong \nplease enter right choice')