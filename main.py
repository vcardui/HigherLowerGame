from replit import clear
import random
from game_data import data
import art

score = 0
status = 'neutral'

numbers = []
for item in data:
  x = data.index(item)
  numbers.append(x)
  

def get_random():
  random_int = random.choice(numbers)
  #print(f"random_int = {random_int}")
  numbers.remove(random_int)
  return random_int

def compare_A_vs_B(item_1, item_2):
  global data
  global vs
  global score

  user_guess_follower_count = 0
  comparison_follower_count = 0

  print(f"Compare A: {data[item_1]['name']}, a {data[item_1]['description']} from {data[item_1]['country']}.")
  #Show number of followers (A)
  #print(f"follower_count = {data[item_1]['follower_count']}")
  print(f'{art.vs}')
  print(f"Against B: {data[item_2]['name']}, a {data[item_2]['description']} from {data[item_2]['country']}.")
  #Show number of followers (B)
  #print(f"follower_count = {data[item_2]['follower_count']}")
  
  ok_input = False
  while ok_input == False:
    user_guess = str(input(""))
    
    if user_guess in ('a', 'A'):
      user_guess_Nº_item = item_1
      user_guess_follower_count = data[item_1]['follower_count']
      comparison_follower_count = data[item_2]['follower_count']
      ok_input = True
      
    elif user_guess in ('b', 'B'):
      user_guess_Nº_item = item_2
      user_guess_follower_count = data[item_2]['follower_count']
      comparison_follower_count = data[item_1]['follower_count']
      ok_input = True
      
    else:
      print("   Please type a valid answer...")
      
  #Delete later ↓
  #print(f"user_guess = {user_guess}")
  #print(f"user_guess_follower_count = {user_guess_follower_count}")
  #print(f"comparison_follower_count = {comparison_follower_count}")

  if user_guess_follower_count < comparison_follower_count:
    return False
  elif comparison_follower_count < user_guess_follower_count:
    item_that_won[0] = user_guess_Nº_item
    score += 1
    return True
  elif user_guess_follower_count == comparison_follower_count:
    print("OMG! This is so un expected. Both items have the same follower count.")
    return True
    

#Actual code:

item_that_won = []
item_that_won.append(get_random())

game_is_over = False
while game_is_over == False:
    
  clear()
  print(f'{art.logo}')

  if status == 'right':
    print(f"You're right! Current score: 🔥 {score}")
  
  empty_list = []
  if numbers == empty_list:
    print("YOU ARE AMAZING!!! There are no more options left...\n ·: YOU HAVE WON :·")
    game_is_over = True
  else:
    #Delete later ↓
    #print(f"item_that_won = {item_that_won}")
    
    item_A = int(item_that_won[0])
    item_B = get_random()
    result = compare_A_vs_B(item_1 = item_A, item_2 = item_B)
    
    if result == True:
      status = 'right'

    elif result == False:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_is_over = True