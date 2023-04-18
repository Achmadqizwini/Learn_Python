class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} \n\thealth: {}".format(self.name, self.__health)

    @property  # merubah sebuah method seperti sebuah variable
    def info(self):
        return "name {} \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input


hero1 = Hero("jonson", 1000, 500)
hero1.name = "dadang"
print(hero1.info)

print("\n getter and setter armor")
print(hero1.armor)

hero1.armor = 102
print(hero1.armor)
