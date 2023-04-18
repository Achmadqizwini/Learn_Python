class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name  # private variable using __private
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def attacked(self, damage):
        self.__health -= damage


hero1 = Hero("Saber", 1000, 10)
print(hero1.__dict__)
print(hero1.getName())
print(hero1.getHealth())

hero1.attacked(300)
print(hero1.getHealth())
