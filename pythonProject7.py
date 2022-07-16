import random
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

list_images=[rock, paper, scissors]
user=int(input("Select 0 for rock, 1 for paper and 2 for scissors:"))
print(list_images[user])

computer=random.randint(0,2)
print("Computer chose:")
print(list_images[computer])
if (user==0 and computer==0) or (user==1 and computer==1) or (user==2 and computer==2):
  print("It's a draw")
if (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
  print("You win!")
if (user==2 and computer==0) or (user==1 and computer==2) or (user==2 and computer==0) :
  print("You lose")

