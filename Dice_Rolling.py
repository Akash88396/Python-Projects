<<<<<<< HEAD
import random

while True:
    roll_dice = input(" Want to Roll the dice? (Yes / No):").lower()

    if roll_dice == 'yes':
      value1 = random.randint(1,6)
      value2 = random.randint(1,6)
      print(f'{(value1,value2)}')
    elif roll_dice == 'no':
      print("Thanks for playing!!")
      break
    else:
      print('Invaild choice')





=======
import random

while True:
    roll_dice = input(" Want to Roll the dice? (Yes / No):").lower()

    if roll_dice == 'yes':
      value1 = random.randint(1,6)
      value2 = random.randint(1,6)
      print(f'{(value1,value2)}')
    elif roll_dice == 'no':
      print("Thanks for playing!!")
      break
    else:
      print('Invaild choice')





>>>>>>> 24e997752c4f7a453d885da1e91bcefa948f39e2
