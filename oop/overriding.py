class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def ingfo(self):
        print("{}: \n\t health :{}".format(self.name, self.health))


class Fighter(Hero):
    pass


class Mage(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    # overriding method ingfo di class hero (superclass)
    def ingfo(self):
        print("Hero {} \n\t Health : {} \n\t Type: Mage".format(
            self.name, self.health))


class Marksman(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)


valentina = Mage("valen", 5000)
wanwan = Marksman("wanwan", 100)


valentina.ingfo()
wanwan.ingfo()

print(valentina.__dict__)
