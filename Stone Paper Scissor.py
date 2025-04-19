import random

choicer = ('stone','paper','scissor')
computer_Choice = random.choice(choicer)

while True:
   
   Select_one = input("Choice any one (STONE,PAPER,SCISSOR):").lower()

   if Select_one not in choicer:
      print("Invailed Choice")
      continue

   
   print(f'Your Choice : {Select_one}')
   print(f'Computer choice : {computer_Choice}')

   if Select_one == computer_Choice:
      print("Match Tai!!")
   elif(Select_one =='stone' and computer_Choice =='scisoor'
        or Select_one == 'scissor' and computer_Choice =='paper'
        or Select_one == 'paper' and  computer_Choice == 'stone'):
      print("You Won")
   else:
      print("You Defeated")

   select = input("Do you want to continue (Yes/NO):").lower()
   if select == 'no':
      break


# for multiple cursor to use ctrl+ D to select multiple cursor
# agar hatana ha to do bar escap batan dabao