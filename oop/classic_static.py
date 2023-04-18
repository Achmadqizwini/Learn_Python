class Hero:

    # private class variabel
    __amount = 0

    def __init__(self, name):
        self.__name = name
        Hero.__amount += 1

    # method ini hanya berlaku untuk objek
    def getJumlah2(self):
        return self.__amount

    # method ini hanya berlaku untuk class
    def getJumlah():
        return Hero.__amount

    # static method
    @staticmethod
    def getAmount():
        return Hero.__amount

    @classmethod
    def getAmount2(cls):
        return cls.__amount


hero1 = Hero("miya")
print(Hero.getJumlah())
print(hero1.getJumlah2())

hero2 = Hero("badang")
print(Hero.getAmount())
print(hero2.getAmount())

print(Hero.getAmount2())
print(hero2.getAmount2())
