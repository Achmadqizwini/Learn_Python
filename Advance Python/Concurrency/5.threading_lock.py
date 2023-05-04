# A race condition occurs when two threads try to access a shared variable simultaneously.

# The first thread reads the value from the shared variable. The second thread also reads the value from the same shared variable.

from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Thread
from time import sleep

counter = 0


def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(1)

    counter = local_counter
    print(f"counter : {counter}")


t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"the final counter is {counter}")

print("\nUsing lock to prevent the race condition\n")

counterr = 0


def increase2(by):
    global counterr

    lock.acquire()

    local_counter = counterr
    local_counter += by

    sleep(1)

    counterr = local_counter
    print(f"counter: {counterr}")

    lock.release()


lock = Lock()

with ThreadPoolExecutor() as executor:
    executor.map(increase2, [10, 20])

print(f"the final counter is {counterr}")
