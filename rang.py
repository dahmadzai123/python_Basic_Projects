import  random
letters = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'x']

numbers= ['1,' '2', '3', '4', '5', '6','7', '8', '9', '10']
symbols = ['!', '@', '#', '$']

print("welcom to the pypassword generator!")

nr_letters = int(input("how many letters do you want to enter "))
nr_numbers = int(input("how many numbers do you want to enter "))
nr_symbols = int(input("How many symbols do you want to enter "))

password = []
for char in range(1, nr_letters +1):
    password += random.choice(letters)
    
    
for char in range(1, nr_numbers +1):
    password += random.choice(numbers)
    
    
for char in range(1, nr_symbols +1):
    password += random.choice(symbols)
    
print(password)
random.shuffle(password)
print(password)

password = ""
for char in password:
    password += char
print(f"your password is {password}")