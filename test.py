import random
from colorama import Fore, init
init(autoreset=True)
with open('5-letter-words.txt', 'r') as file:
    word_bank = [line.strip() for line in file]
word = word_bank[random.randint(1, 3103)]
attempt = 1
point = 0


while attempt < 7:
 print(word)
 check = 0
 guess = input(f'What is your {attempt} guess? Only 5 characters:')
 print(guess)
 if len(guess) > 5:
   guess = input('Please only input 5 characters:')
 if guess == word or attempt == 6:
   point = 6-attempt
   print (f'The game is over, you scored, {point}, the correct word was: {word}.')
   break
 if guess != word:
   print(guess==word)
   for char in guess:
     if char == guess[check]:
       print(Fore.GREEN + char)
       check+=1
     elif char in word:
       print(Fore.YELLOW + char)
       check+=1
     else:
       print(char)
       check+=1   
 attempt+=1


