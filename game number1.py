# импортируем модуль для работы со случайными числами
import random

# число попыток угадать
guesses_made = 0

print("Здравствуйте! Введите вашу фамилию")
a = str(input())
print("введите ваше имя")
b = str(input())
print( b + " " + a + " поиграем угадай число!")

point = 10
x = random.randint(1, 10)
while guesses_made < 6:
    print("Я загадал число, угодай какое от 0 до 10")
    player = int(input())
    guesses_made = guesses_made + 1
    point = point - 1
    if player > x:
        print("Вы ввели больше")
    if player < x:
        print("Вы ввели меньше")
    if player == x:
        print("Поздравляю")
        break
if player == x:
    print("Круто ты угодал мое число " + str(x) + " из " + str(guesses_made) + " попыток!" +" Твой выигрыш " + (str(point)) + " очков!" )
if player != x:
    print("Жаль ты проиграл, попытки закончились, ты не выиграл очки. Мое число было " + " " + str(x))

