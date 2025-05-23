<<<<<<< HEAD
import random


guess_number = random.randint(1,1000)
count =10
while count>0:
    print(f'Chance Left {count}!')

    try:
      n = int(input('Enter number between 1 to 1000 : ')) 
    except:
        print("Enter Vailed number")
        continue

    if n<1 or n>1000:
        print("Number out of range!")
        continue
    

    if n>guess_number:
        print("Enterd number is too high!!")
        
    elif n<guess_number:
        print('Entered number is too low!!')

    else:
        print(f' Congratulations! {n} is the correct number!')
        print(" You Win!!")
        break

    count -=1

    if count ==0:
        print(f" You Lose the Game! The correct number was {guess_number}. Try again next time.")   

    
    

=======
import random


guess_number = random.randint(1,1000)
count =10
while count>0:
    print(f'Chance Left {count}!')

    try:
      n = int(input('Enter number between 1 to 1000 : ')) 
    except:
        print("Enter Vailed number")
        continue

    if n<1 or n>1000:
        print("Number out of range!")
        continue
    

    if n>guess_number:
        print("Enterd number is too high!!")
        
    elif n<guess_number:
        print('Entered number is too low!!')

    else:
        print(f' Congratulations! {n} is the correct number!')
        print(" You Win!!")
        break

    count -=1

    if count ==0:
        print(f" You Lose the Game! The correct number was {guess_number}. Try again next time.")   

    
    

>>>>>>> 24e997752c4f7a453d885da1e91bcefa948f39e2
