import random
import binascii


rock = '''                _    
                 | |   
 _ __ ___    ___ | | __
| '__| _ |  |__ ||/ /
| | | (_) |(__(  | < _
|_|  |___|  |___||_| |_|
                     '''

paper = ''' 
_ __   __ _ _ __   ___ _ __ 
| '_ | / _` | '_ | / _ | '__|
| |_) | (_| | |_) |  __/ |   
| .__/ |__,_| .__/ |___|_|   
| |         | |              
|_|         |_|              '''


scissors = '''
    _       ,|'
   (_).  ,|'
   __  ::
  (__)'  `|.
            `|.
'''
print("Welcome to Rock-Paper-Scissors!")
game = [rock, paper, scissors]
player_1 = random.choice(game)
ask_player_2 = int(input("What do you choose? \n"
                  "type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if ask_player_2 < len(game):
    player_2 = game[ask_player_2]
    if player_2 in game:
        print(f"Computer chose: {player_1}")
        print(f"You chose: {player_2}")
        if player_2 == "Rock" and player_1 == "Scissors":
            print("You WIN!")
        elif player_2 == "Paper" and player_1 == "Rock":
            print("You WIN!")
        elif player_2 == "Scissors" and player_1 == "Paper":
            print("You WIN!")
        else:
            print("You LOSE!")
else:
    print("You choose an INVALID option.!!\n"
          "type 0 for Rock, 1 for Paper, 2 for Scissors: ")












