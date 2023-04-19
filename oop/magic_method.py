class Mangga:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "debug: {} dengan jumlah {}".format(self.nama, self.jumlah)

    def __str__(self) -> str:
        return "{} dengan jumlah {}".format(self.nama, self.jumlah)


mangga1 = Mangga("arumanis", 1)
mangga2 = Mangga("Manalagi", 2)

print(repr(mangga1))
print(mangga2)
