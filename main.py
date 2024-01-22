rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(player_choice)

import random
computer_choice = random.randint(0, 2)
print(computer_choice)

options = [rock, paper, scissors]

if player_choice == computer_choice:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} this is a tie")
elif player_choice == 0 and computer_choice == 1:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} computer wins")
elif player_choice == 0 and computer_choice == 2:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} you win")
elif player_choice == 1 and computer_choice == 0:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} You win")
elif player_choice == 1 and computer_choice == 2:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} the computer wins")
elif player_choice == 2 and computer_choice == 0:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} compuer wins")
else:
  print(f"You chose {options[player_choice]} the computer chose {options[computer_choice]} You win")
  
# computer_RPS = rock
# if computer_choice == 0:
#   computer_RPS = rock
# elif computer_choice == 1:
#   computer_RPS = paper
# else:
#   computer_RPS = scissors
  
