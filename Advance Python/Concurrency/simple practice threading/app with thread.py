from threading import Thread
from time import perf_counter


def replace(filename, sub_str, new_sub_str):
    print(f"processing the file {filename}")
    with open(filename, 'r') as file:
        content = file.read()

    # replace the substring inside the content
    content = content.replace(sub_str, new_sub_str)

    with open(filename, 'w') as file:
        file.write(content)


def main():
    filenames = [
        "test1.txt",
        "test2.txt",
        "test3.txt",
        "test4.txt",
        "test5.txt",
        "test6.txt",
        "test7.txt",
        "test8.txt",
        "test9.txt",
        "test10.txt",
    ]

    # a = 0
    # while a < 3:
    # create threads
    threads = [Thread(target=replace, args=(filename, 'id', 'ids'))
               for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()
        # a += 1


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
