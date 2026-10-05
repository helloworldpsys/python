#a guessing game by combining all the concepts i learned  till now 
'''like it will generate a random number in t he range of 1 to 50
and the user have to guess this random number 
so user have to guess this lucky_number 
and  if the random number is  35 and user guessed it 45 thn we will
give user  a hint that the guesses is too high and  too low for
if it guessed  25 and  the  game continues  till user guessed it correct
'''
import random 

def play_game():
    lucky_num=(random.randint(1, 50))

    while True:
        user_num = int(input("guess the  lucky number: "))
        if user_num == lucky_num:
            print("you won ")
            break
        elif user_num<lucky_num:
            print("too low")
        elif user_num>lucky_num:
            print("too high")   
play_game(5)
