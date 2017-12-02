from random import *
import collections

scores = 0
outs = 0
bases = collections.deque([False, False, False], maxlen=3)

def menu():
  print('Welcome to Baseball!')
  print('1. Bat')
  print('2. Pitch')
  return input('What would you like to do?')

def showInfo(bases, strikes):
  global outs
  global scores
  print('On First? ' + str(bases[0]))
  print('On Second? ' + str(bases[1]))
  print('On Third? ' + str(bases[2]))
  print('STRIKES %d' % strikes)
  print('OUTS %d' % outs)
  print('SCORES %d' % scores)

def roll(lower, upper):
  return randint(lower, upper)

def homerun():
  global scores
  global bases
  scores = scores + len(list(filter(lambda x: x, bases))) + 1
  bases = collections.deque([False, False, False], maxlen=3)

def shiftRunners(outcome):
  global bases
  global scores
  if outcome >= 4:
    homerun()
    outcome = outcome - 4
      
  else:
    base_list = list(bases)
    scores = scores + len(list(filter(lambda x: x, base_list[-outcome:])))
  
  bases.appendleft(True)

  for i in range(0, outcome-1):
    bases.appendleft(False)

  print(base_list[-outcome:])
    

def calcBatterResult(outcome, difference):
  if difference == 0:
    homerun()
  else:
    shiftRunners(outcome)
  
def calcPitcherResult(outcome, difference):
  global outs
  if difference == 0:
    outs = outs + 1

  while (outcome - 3 >= 0):
    outs = outs + 1
    outcome = outcome - 3
  
  return outcome

def playBall(playerIsBatter):
  strikes = 0
  while (scores < 3 and outs < 3):
    playerGuess = int(input('Guess a number between 1 and 6\n'))
    aiGuess = roll(1, 6)
    playerRoll = roll(1, 6)
    aiRoll = roll(1, 6)
    print('Player rolled a %d' % playerRoll)
    print('AI rolled a %d' % aiRoll)
    print('AI guessed %d' % aiGuess)
    if playerIsBatter:
      differenceB = abs(playerGuess - playerRoll)
      differenceP = abs(aiGuess - aiRoll)
    else: 
      differenceB = abs(aiGuess - aiRoll)
      differenceP = abs(playerGuess - playerRoll)
    
    print('Batter was %d away from being correct' % differenceB)
    print('Pitcher was %d away from being correct' % differenceP)
    outcome = abs(differenceP - differenceB)

    if differenceP > differenceB:
      strikes = 0
      calcBatterResult(outcome, differenceB)
    elif differenceP < differenceB:
      strikes = calcPitcherResult(outcome+strikes, differenceP)
    else:
      if strikes < 2:
        strikes = strikes + 1

    showInfo(bases, strikes)
  if scores >= 3:
    print('The batter has won!')
  else:
    print('The pitcher has won!')

response = menu()
playBall(int(response) == 1)
