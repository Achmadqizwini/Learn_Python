class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def ingfo(self):
        print("{}: \n\t health :{}".format(self.__name, self.__health))


class Fighter(Hero):
    pass


class Mage(Hero):
    def __init(self, name, health):
        Hero.__init__(name, health)
        super().ingfo()


class Marksman(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        super().ingfo()


alu = Hero("alu", 1000)
badang = Fighter("badang", 2000)
print(alu.__dict__)
print(badang.__dict__)

valentina = Mage("valen", 5000)
print(valentina.__dict__)

wanwan = Marksman("wanwan", 100)
print(wanwan.__dict__)
