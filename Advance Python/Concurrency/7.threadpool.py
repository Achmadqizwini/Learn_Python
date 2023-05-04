from concurrent.futures import ThreadPoolExecutor
from time import perf_counter, sleep


def task(id):
    print(f"Starting the task {id}")
    sleep(1)
    return (f"task {id} done")


start = perf_counter()
print(task(1))
print(task(2))
end = perf_counter()

print(f"it took {end-start: 0.2f} second")

print("\nusing thread pool\n")

start2 = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)

    print(f1.result())
    print(f2.result())

    # ALTERNATIF
    # results = executor.map(task, [1,2])
    # for result in results:
    #     print(result)

finish = perf_counter()
print(f"It took {finish-start2: 0.2f} second(s) to finish.")
