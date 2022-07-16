import random
password_list=[]
for char in range(1, nr_letters+1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
  password_list.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
  password_list.append(random.choice(numbers))
  
random.shuffle(password_list)

password=""
for char in password_list:
  password+=char
print(password)  
  
