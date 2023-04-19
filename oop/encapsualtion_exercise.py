class Hero:
    __jumlah = 0

    def __init__(self, name, health, attack_power, armor):
        self.__name = name
        self.__healthBase = health
        self.__attackPowerBase = attack_power
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attackPower = self.__attackPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax
        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : \n\tlevel: {}\n\thealth: {}/{}\n\tattack power: {}\n\tarmor: {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attackPower, self.__armor)

    @property
    def gainEXP(self):
        pass

    @gainEXP.setter
    def gainEXP(self, exp):
        self.__exp += exp
        if (self.__exp >= 100):
            print("LEVEL UP!")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attackPower = self.__attackPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level

    def attack(self, enemy):
        print(self.__name, "attack")
        self.gainEXP = 120


ling = Hero("Ling", 100, 5000, 0)
print(ling.info)
ling.gainEXP = 120
print(ling.info)
# print(ling.__dict__)

miya = Hero("miya", 1000, 2000, 50)
ling.attack(miya)
print("================")
print(ling.info)
