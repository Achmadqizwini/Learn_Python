from threading import Thread
from time import perf_counter, sleep


def task():
    print("Starting a task ")
    sleep(1)
    print("done")


start_time = perf_counter()
task()
task()
end_time = perf_counter()

print(f"it took {end_time - start_time: 0.2f} second")

print("\n Using Threading \n")


def task2():
    print("Starting a task ")
    sleep(1)
    print("done")


start_time2 = perf_counter()

# Creating a new thread
thread1 = Thread(target=task2)
thread2 = Thread(target=task2)

# Start the thread

thread1.start()
thread2.start()

# wait for the threads to complete
thread1.join()
thread2.join()

end_time2 = perf_counter()

print(f"it took {end_time2-start_time2: 0.2f} seconds")

print("\npassing argumen to threads\n")


def task3(id):
    print(f"Starting the task {id}")
    sleep(1)
    print(f"the task {id} complete")


time_start3 = perf_counter()

# create and start 15 threads

threads = []
for i in range(1, 16):
    thread = Thread(target=task3, args=(i,))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

end_time3 = perf_counter()

print(f"it took {end_time3-time_start3: 0.2f} second")

print("\n without thread to run 15 task\n")
