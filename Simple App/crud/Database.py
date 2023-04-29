from . import operation

DB_NAME = "data.txt"

template = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy"
}


def init_console():
    try:
        with open(DB_NAME, "r")as file:
            print("database ditemukan : ")
    except:
        print("database tidak ditemukan, silahkan membuat data baru")
        operation.create_first_data()
