import time

from . import Database
from .utils import random_string


def create_first_data():
    penulis = input("Nama penulis : ")
    judul = input("Judul buku : ")
    tahun = input("Tahun terbit: ")

    data = Database.template.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y=%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.template["penulis"][len(penulis):]
    data["judul"] = judul + Database.template["judul"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{ data["pk"]}, {data["date_add"]}, {data["penulis"]}, { data["judul"]}, { data["tahun"]}\n'

    print(data_str)

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal mbueh")


def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()

            return content
    except:
        print("error to read data")
        return False
