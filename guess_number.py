print('\nДобро пожаловать в игру Отгадай число!')
print('\nЯ загадал натуральное число из диапазона от 1 до 100.')
print('\nПостарайтесь отгадать его за минимальное число попыток.\n')
import random
the_number = random.randint(1,100)
tries = 1
while tries < 100:
    tries += 1
    guess = int(input('Ваше предположение: '))
    if guess < the_number:
        print('Больше...')
    elif guess > the_number:
            print('Меньше...')
    else:
        guess == the_number
        print('Юху, Вы отгадали это и правда: ', the_number)
        print('Вы сделали', tries, 'попыток')
    if tries == 5 and guess != the_number:
        print('Увы, Вы проиграли. Начните заново')
        break
            
    
input('\nНажмите Enter для выхода')
