# number = int(input("Enter a number"))
# if number % 2:
#     print("this is an odd number")
# else:
#     print("the number is even")
# height = float(input("What is your height? "))
# weight = int(input("What is your weight? "))
# # BMI = weight / height
# BMI = weight / (height * height)
# if BMI <= 18.5:
#     print("your underweight")
#     if BMI > 18.5 and BMI < 25:
#         print("you have normal weight")
#     elif BMI  >25 or BMI < 30:
#         print("your slightly overwight")  
#     elif BMI > 30 or BMI < 35:
#         print("your abese")
# else:
#     print("your clincaly obese")
# if BMI <= 18.5:
#     print(f"your underweight {BMI}")
# if  BMI < 25:
#     print(F"you have normal weight {BMI}")
# elif BMI < 30:
#     print(F"your slightly overwight {BMI}")  
# elif BMI < 35:
#     print(F"your abese {BMI}")
# else:
#     print(F"your clincaly obese {BMI}")        

# year = int(input())

# if year % 4 == 0:
#  print("leap year")
# elif year % 100 == 0:
#  print("not leap year")
# elif year % 400 == 0:
#  print("leap year")
# else:
#  print("not leap year")
print("Welcom to the rollarcoster. ")
height = float(input("What is your height?"))

bill = 0

if height > 1.20:
  print("you can ride the rollarcoster ")
  age = int(input("how old are you? "))   
  if age < 12:
   bill = 5
   print("your ticket is $5 ")
  if age <= 18:
   bill = 7
   print("your ticket is $7")
  else:
    bill = 12    
    print("your ticket is $12 ")
      
  photo = input("do you want to photo press 'Y' for yes and 'N' for no" )
  if photo == "Y":
   bill += 3
   print(f"your bill well be {bill} $")
  else:
    print(f"your total bill well be {bill} $")
else:
    print("you can not rid the rollarcoster. ")
    
     
    