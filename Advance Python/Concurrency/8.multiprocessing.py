import multiprocessing
import time


def task(n=100_000_000):
    while n:
        n -= 1


def main():
    start = time.perf_counter()
    task()
    task()
    end = time.perf_counter()
    print(f"it took {end-start: 0.2f} second ")

    print("\nnow using multiprocessing\n")


def main2():
    start_time = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.perf_counter()

    print(f"it took {end_time-start_time: 0.2f} second")


if __name__ == "__main__":
    main()
    main2()
