class Hero():
    def __init__(self, name, hp=100, attack_power=20):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        other.hp -= self.attack_power
    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self):
        self.player = Hero('игрок')
        self.computer = Hero('компьютер')

    def start(self):
        print('Битва начинается!')

        while self.player.is_alive() and self.computer.is_alive():
            # ход игрока
            self.player.attack(self.computer)
            print(
                f'{self.player.name} атакует {self.computer.name}. '
                f'У компьютера осталось {self.computer.hp} здоровья'
            )
            if not self.computer.is_alive():
                break
            # ход компьютера
            self.computer.attack(self.player)
            print(
                f'{self.computer.name} атакует {self.player.name}. '
                f'У игрока осталось {self.player.hp} здоровья'
            )
        if self.player.is_alive():
            print('Победил игрок!')
        else:
            print('Победил компьютер!')

game = Game()
game.start()
