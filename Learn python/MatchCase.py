num = int(input("Enter your age :"))

match num:
    case 0 if num >=0 and num <18 :
        print(" You can  not drive car ")
    case 1:
        print(num)
    case _:
        print("Default statement")
        


