import time
from queue import Empty, Queue
from threading import Thread


def producer(queue):
    for i in range(1, 6):
        print(f"inserting {i} into the queue")
        time.sleep(1)
        queue.put(i)


def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f"processing the {item}")
            time.sleep(2)
            queue.task_done()


def main():
    queue = Queue()

    # create a producer and start it
    thread_produceer = Thread(target=producer, args=(queue,), daemon=True)

    # start the thread
    thread_produceer.start()

    # create a consumer thread and start it
    consumer_thread = Thread(target=consumer, args=(queue, ), daemon=True)

    # start the consumer thread
    consumer_thread.start()

    # wait for all tasks to be added to the queue
    thread_produceer.join()

    # wait for all tasks on the queue to be completed
    queue.join()


if __name__ == "__main__":
    main()
