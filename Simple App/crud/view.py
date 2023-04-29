from . import operation


def read_console():
    data_file = operation.read()
    # print(data_file)

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # data
    for index, data in enumerate(data_file):
        data_list = data.split(",")

        pk = data_list[0]
        date_add = data_list[1]
        penulis = data_list[2]
        judul = data_list[3]
        tahun = data_list[4]

        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")

    # footer
    print("="*100+"\n")
