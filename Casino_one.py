
import random

guessTaken = 0

print("Привет! Как тебя зовут?")
myName = input()

number = random.randint(1, 20)
print("Что ж, " + myName + ", я загадываю число от 1 до 20.")

for guessTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess > number:
        print('Твоё число слишком большое.')

    if guess < number:
        print('Твоё число слишком маленькое.')
    
    if guess == number:
        break

if guess == number:
    guessTaken = st(guessTaken + 1)
    print('Отлично, ' + myName + '!Ты справился за' + guessTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')