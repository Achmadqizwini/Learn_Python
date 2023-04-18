class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def attacking(self, enemy, attackPower):
        print(self.name, "attack", enemy.name)
        print("the damage dealt :", attackPower)
        hero1.attacked(self, self.attackPower)

    def attacked(self, enemy, attackPower):
        print("omaigadd i got attacked by " + enemy.name)
        print("and i got ", attackPower,  "damage")
        self.health -= attackPower - self.armor
        print("now my hp is:", self.health)


hero1 = Hero("miya", 1000, 100, 5)
hero2 = Hero("balmontok", 5000, 200, 100)
hero2.attacking(hero1, 200)
