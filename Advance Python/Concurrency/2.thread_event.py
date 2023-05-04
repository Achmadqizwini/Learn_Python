from threading import Event, Thread
from time import sleep


def task(event: Event, id: int) -> None:
    print(f"Starting the {id} thread, waiting for signal...")
    event.wait()
    print(f"received a signal, the {id} task is complete")


def main():
    event = Event()

    t1 = Thread(target=task, args=(event, 1))
    t2 = Thread(target=task, args=(event, 2))

    t1.start()
    t2.start()

    print("Blocking the main thread for 3 second")
    sleep(5)

    event.set()


if __name__ == "__main__":
    main()
