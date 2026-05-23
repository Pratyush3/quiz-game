##print("This is a quiz game")
from questions import questions



## Welcoming the player
print("Welcome to the quiz game!")
score=0
rules = """The rules of the game are as follows:
1. You will be asked a series of questions.
2. Each correct answer will earn you 4 point.
3. Each wrong answer will deduct 1 point(for hard difficulty) and 0.5 point(for medium difficulty) and 0.25 point(for easy difficulty).
4. You can choose the difficulty level at the beginning of the game.
5. The game will end when you have answered all the questions or if you choose to quit
6. You can also choose to skip a question, but you will not earn any points for that question.
7. There will be a time limit for each question, and if you do not answer within the time limit, it will be skipped.
8. At the end of the game, your score will be displayed, and you can choose to play again or quit.
"""
print(rules)

difficulty_asker = """Choose your difficulty:
1. Easy
2. Medium
3. Hard"""
print(difficulty_asker)


difficulty = int(input("Your difficulty level: "))

if difficulty == 1 :
    print("You've chosen easy difficulty")
elif difficulty == 2: 
    print("You've chosen medium difficulty")
elif difficulty == 3:
    print("You've chosen hard difficulty")
else:
    print("Please choose a valid number")
    
