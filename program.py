import random
import string

print("                        Random Password Generator              ")
print("                        Please enter below details             ")

#using string to get all upper & lower case letters & number & symbol

lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
num=list(string.digits)
sym=list(string.punctuation)

lower_letters=int(input("Enter how many lower case letter you want?  "))
upper_letters=int(input("Enter how many Upper case letter you want?  "))
number=int(input("Enter how many numbers letter you want?  "))
symbol=int(input("Enter how many symbols letter you want?  "))


password=''
#using for loop 
for char in range(1,lower_letters+1):
    random_lower_letter=random.choice(lower)
    password +=random_lower_letter
    
for char in range(1,upper_letters+1):
    random_upper_letter=random.choice(upper)
    password +=random_upper_letter
    
for char in range(1,number+1):
    random_number=random.choice(num)
    password +=random_number
    
for char in range(1,symbol+1):
    random_symbol=random.choice(sym)
    password +=random_symbol
    
final = list(password)
random.shuffle(final)
final_password = ''.join(final)
print(f'Your password is\n {final_password}')
    














