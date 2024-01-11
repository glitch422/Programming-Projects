from random import randint
import sys

#generate a number 1 ~ 10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))



while True:
  try:
    #input from user?
    guess = int(input('Guess a number 1~10:\t'))
  
    #check that input is a number 1~10
    if 0 < guess < 11:
      if guess == answer:
        print('You are a genius!')
        break
      else:
        print('Hey bozo, I said 1~10')
  except ValueError:
    print('please enter a number')
    continue

