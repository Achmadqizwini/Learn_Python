class Mangga:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "debug: {} dengan jumlah {}".format(self.nama, self.jumlah)

    def __str__(self) -> str:
        return "{} dengan jumlah {}".format(self.nama, self.jumlah)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai jumlah"


mangga1 = Mangga("arumanis", 1)
mangga2 = Mangga("Manalagi", 2)

print(repr(mangga1))
print(mangga2)

print(mangga1 + mangga2)
print(mangga1.__dict__)
