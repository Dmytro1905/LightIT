# -*- coding: utf-8 -*- 
from random import randint
# создаем класс Players с атрибутами имя (name) и здоровье (health) 
class Players():
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
# создаем класс Fight с атрибутами limit_1 и limit_2, которые являются граничными значениями диапазонов нанесенных уронов или исцеления
class Fight():
    def __init__(self, limit_1, limit_2):
        self.limit_1 = limit_1
        self.limit_2 = limit_2
player = Players("Игрок") # создаем Игрока (экземпляр класса Players)
computer = Players("Противник") # создаем Противника (экземпляр класса Players)
average_damage = Fight(limit_1 = 18, limit_2 = 25) # создаем экземпляр класса Fight (первый вариант хода с нанесением умеренного урона в диапазоне от 18 до 25)
damage = Fight(limit_1 = 10, limit_2 = 35) # создаем экземпляр класса Fight (второй вариант хода с нанесением урона в диапазоне от 10 до 35)
recovery = Fight(limit_1 = 18, limit_2 = 25) # создаем экземпляр класса Fight (третий вариант хода - исцеление в диапазоне от 18 до 25)
while (player.health > 0 and computer.health > 0): # создаем цикл работы программы до тех пор, пока здоровье Игрока и Противника больше 0
    print("Выбор. Чей ход сейчас?")
    player_choice = randint(1, 2) # выбор случайным образом, кто будет ходить Игрок или Противник
    if player_choice == 1: # описание случая, если выбор хода пал на Игрока
        print("Выбор пал на Игрока")
        if (player.health == 100 and computer.health == 100): # описание случая, когда у игроков здоровье составляет 100 очков (процентов)
            damage_choice = randint(1, 2) # выбор варианта хода случайным образом
            if damage_choice == 1: # описание сценария первого варианта хода
                dam = randint(average_damage.limit_1, average_damage.limit_2) # выбор нанесенного урона случайным образом
                computer.health = computer.health - dam
                print("Противнику нанесен умеренный урон равный " + str(dam))
            elif damage_choice == 2: # описание сценария второго варианта хода
                dam = randint(damage.limit_1, damage.limit_2) # выбор нанесенного урона случайным образом
                computer.health = computer.health - dam
                print("Противнику нанесен урон равный " + str(dam))
        else:
            damage_choice = randint(1, 3) # выбор варианта хода случайным образом
            if damage_choice == 1: # описание сценария первого варианта хода
                dam = randint(average_damage.limit_1, average_damage.limit_2) 
                computer.health = computer.health - dam
                print("Противнику нанесен умеренный урон равный " + str(dam))
            elif damage_choice == 2: # описание сценария второго варианта хода
                dam = randint(damage.limit_1, damage.limit_2) 
                computer.health = computer.health - dam
                print("Противнику нанесен урон равный " + str(dam))
            elif damage_choice == 3: # описание сценария третьего варианта хода
                dam = randint(recovery.limit_1, recovery.limit_2) # выбор очков (процентов) исцеления случайным образом
                if (player.health <= 100 - dam): # описание ситуации недопущения возможности исцеления более 100 очков (процентов) здоровья 
                    player.health = player.health + dam
                else:
                    player.health = 100
                print("Здоровье Игрока восстановлено на " + str(dam))
    if player_choice == 2: # описание случая, если выбор хода пал на Противника
        print("Выбор пал на Противника")
        if (player.health == 100 and computer.health == 100): # описание случая, когда у игроков здоровье составляет 100 очков (процентов)
            damage_choice = randint(1, 2)
            if damage_choice == 1:
                dam = randint(average_damage.limit_1, average_damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен умеренный урон равный " + str(dam))
            elif damage_choice == 2:
                dam = randint(damage.limit_1, damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен урон равный " + str(dam))
        elif computer.health > 35: # описание ситуации, если количество очков (процентов) здоровья Противника более 35
            damage_choice = randint(1, 3)
            if damage_choice == 1:
                dam = randint(average_damage.limit_1, average_damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен умеренный урон равный " + str(dam))
            elif damage_choice == 2:
                dam = randint(damage.limit_1, damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен урон равный " + str(dam))
            elif damage_choice == 3:
                dam = randint(recovery.limit_1, recovery.limit_2)
                if (computer.health <= 100 - dam):
                    computer.health = computer.health + dam
                else:
                    computer.health = 100
                print("Здоровье Противника восстановлено на " + str(dam))
        elif computer.health <= 35: # описание ситуации, если количество очков (процентов) здоровья Противника менее или равно 35
            damage_choice = randint(1, 5)
            if damage_choice == 1:
                dam = randint(average_damage.limit_1, average_damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен умеренный урон равный " + str(dam))
            elif damage_choice == 2:
                dam = randint(damage.limit_1, damage.limit_2)
                player.health = player.health - dam
                print("Игроку нанесен урон равный " + str(dam))
            elif damage_choice >= 3: # увеличение шанса Противника на излечение
                dam = randint(recovery.limit_1, recovery.limit_2)
                if (computer.health <= 100 - dam):
                    computer.health = computer.health + dam
                else:
                    computer.health = 100
                print("Здоровье противника восстановлено на " + str(dam))
    if (player.health > 0 and computer.health > 0):
        print("Здоровье Игрока составляет " + str(player.health))
        print("Здоровье Противника составляет " + str(computer.health))
    elif (player.health < 0):
        print()
        print("Победил Противник!")
    elif (computer.health < 0):
        print()
        print("Победил Игрок!")
    print()