year = int(input("Enter year:"))

if(year % 4 == 0 and year % 100 !=0) or year % 400 ==0:
    print(f"{year} is a leep year ")
else:
    print(f"{year} is not a leep year ")


    # using function



    # def is_leap(year):
    # if(year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
    #     return True
    # else:
    #     return False

def is_leap_year(year):
    if year % 4 == 0:
      if year % 100 == 0:
       if year % 400 == 0:
        return True
       else:
        return False
      else:
        return True
    else:
      return False
  

if is_leap_year(year):
  print(f"{year} is a leep year")
else:
  print(f"{year} is not a leep year")