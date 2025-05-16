class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

class Warrior(Character):
    def attack(self, enemy):
        damage = 20
        enemy.hp -= damage
        print(f"{self.name} ударил мечом {enemy.name} на {damage} урона!")

class Mage(Character):
    def attack(self, enemy):
        damage = 15
        enemy.hp -= damage
        print(f"{self.name} использовал заклинание на {enemy.name} — {damage} урона!")

w = Warrior("Арслан", 100)
m = Mage("Темир", 80)

w.attack(m)
m.attack(w)
print(f"{m.name} жив? {m.is_alive()}")
print(f"{w.name} жив? {w.is_alive()}")
