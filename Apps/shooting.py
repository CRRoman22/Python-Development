class Enemy:
    name = ""
    lives = 0
    def __init__(self,name,lives):
        self.name = name
        self.lives = lives
    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + " killed ")
        else:
            print(self.name + ' has ' + str(self.lives) + ' lives ')
class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster',2)
class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien',5)
a = Monster()
b = Alien()

while True:
    x = input()
    if x == 'exit':
        break
    elif x == 'gun':
        a.hit()
    elif x == 'laser':
        b.hit()
