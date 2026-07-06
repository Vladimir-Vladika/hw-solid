from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print('удар мечом')

class Bow(Weapon):
    def attack(self):
        print('стреляет из лука')

class Axe(Weapon):
    def attack(self):
        print("рубит топором")

class Monster:
    def __init__(self, hp):
        self.hp = hp

class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, monster):
        self.weapon.attack()
        monster.hp -= 10

fighter = Fighter(Sword())
monster = Monster(100)

fighter.attack(monster)
print("HP монстра:", monster.hp)

fighter.change_weapon(Bow())
fighter.attack(monster)
print("HP монстра:", monster.hp)