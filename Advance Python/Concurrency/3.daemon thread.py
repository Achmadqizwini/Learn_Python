import time
from threading import Thread

# A daemon thread is a background thread.
# A daemon thread is useful for executing tasks that are not critical.
# The program can exit and doesn’t need to wait for the daemon threads to be completed.


def task():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"has been waiting for {count} second")
        if count == 10:
            break


t = Thread(target=task)
t.start()


def task2():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"has been waiting for {count} seconds")


t2 = Thread(target=task2, daemon=True)
t2.start()

user_input = input("do you want to quit\n")
