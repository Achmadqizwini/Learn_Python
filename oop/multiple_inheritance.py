class Tipe_hero:
    def setTipe(self, type):
        self.type = type

    def getTipe(self):
        print(self.type)


class Tier_Hero:
    def setTier(self, tier):
        self.tier = tier

    def getTier(self):
        print(self.tier)


class Hero(Tier_Hero, Tipe_hero):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power


alu = Hero("alucard", 1000, 5000)
alu.setTier("epic")
alu.getTier()

alu.setTipe("fighter")
alu.getTipe()
