from random import randint


class Hero():
    def __init__(self, name, health, armor, power):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.new = True

    # печать инфо о персонаже:
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)

    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0


class Warrior(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный воин', self.name)
            self.new = False
        else:
            print('Снова появляется воинственный', self.name)

    # метод для вывода на экран текстового описания атаки
    def attack(self, enemy):
        print(self.name, 'бесстрашно набрасывается на', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()


class Dragon(Hero):
    def hello(self):
        if self.new:
            print('-> НОВЫЙ ГЕРОЙ! С неба спускается свирепый дракон', self.name)
            self.new = False
        else:
            print('И вновь перед нами разъярённый дракон', self.name)

    def attack(self, enemy):
        print(self.name, 'направляет поток смертельного огня на', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()


knight = Warrior('Ричард', 50, 25, 20)
print('Приветствуем тебя, славный рыцарь', knight.name)
print(
    'Ты стоишь у входа в лес, полный смертельных опасностей. Готов ли ты войти внутрь и сразиться с врагами (да/нет)?')
answer = input()
if answer == 'да':
    play = True
    print('\n***Да начнётся битва!*** \n')
else:
    play = False

enemies = list()
enemies.append(Warrior('Питер', 15, 0, 10))
enemies.append(Warrior('Сержио', 10, 15, 5))
enemies.append(Dragon('Дрогон', 1, 25, 60))
enemies.append(Dragon('Визерион', 1, 10, 30))

while play:
    # определяем, с кем будет биться рыцарь
    # в качестве индекса берём длину списка, т.к. после убийства врагов список будет сокращаться
    enemy = enemies[randint(0, len(enemies) - 1)]
    enemy.hello()
    enemy.print_info()

    is_attack = input('Вступить в бой (да/нет)?')
    if is_attack == 'да':
        if randint(0, 1) == 1:
            figthers = [knight, enemy]
        else:
            figthers = [enemy, knight]
        figthers[0].strike(figthers[1])
        figthers[0].attack(figthers[1])
    print('---')

    # проверяем, погибли текущий враг и если да, то удаляем его из списка
    if enemy.check_alive() == False:
        print(enemy.name, 'погиб от руки', knight.name, '\n')
        enemies.remove(enemy)

    # проверяем условия завершения игры (погиб рыцарь или убиты все враги)
    if knight.check_alive() == False:
        print('Храбрый рыцарь', knight.name, 'погиб в бою с врагами')
        play = False
    if len(enemies) == 0:
        print('Храбрый рыцарь', knight.name, 'победил всех врагов!')
        play = False
print('Тут и сказочке конец')
