import asyncio
import time
from asyncio import CancelledError


async def square(n: int):
    return n*n


async def main():
    res = await square(10)
    print(f"the result is {res}")

    resx = await square(5)
    print(f"the result is {resx}")

asyncio.run(main())


async def cor1():
    print("coroutine 1 start ...")
    await asyncio.sleep(3)
    print("coroutine 1 is done")


async def cor2():
    print("coroutine 2 start ...")
    await asyncio.sleep(1)
    print("coroutine 2 is done")


async def main2():
    start = time.time()
    await asyncio.gather(cor1(), cor2())
    end = time.time()
    print(f"it took {end-start: 0.2f} second")

asyncio.run(main2())

print("\ncreate a task\n")


async def show_message():
    for _ in range(3):
        await asyncio.sleep(0.2)
        print('API call is in progress...')


async def main3():
    start = time.perf_counter()

    message_task = asyncio.create_task(
        show_message()
    )

    task1 = asyncio.create_task(cor1())
    task2 = asyncio.create_task(cor2())

    await task1
    await task2
    await message_task

    end = time.perf_counter()

    print(f"the execution time is = {end - start: 0.2f} seconds")


asyncio.run(main3())

print("\ncancelling the task\n")


async def call_api(message, result=100, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main4():
    task = asyncio.create_task(call_api(
        "calling the API", result=2, delay=5
    ))

    time_elapsed = 0
    while not task.done():
        time_elapsed += 1
        await asyncio.sleep(1)
        print("task has not complete, checking again in a second")
        if time_elapsed == 3:
            print("cancelling the task")
            task.cancel()
            break

    try:
        await task
    except CancelledError:
        print('Task has been cancelled.')

asyncio.run(main4())

print("\ncancel a task using wait for\n")


async def main5():
    task = asyncio.create_task(call_api(
        "calling the API", result=2000, delay=5
    ))

    max_timeout = 3

    try:
        await asyncio.wait_for(task, timeout=max_timeout)
    except TimeoutError:
        print("the task is cancelled due to tiumeout error")

asyncio.run(main5())


print("\nshielding a task from cancellation\n")


async def main6():
    task = asyncio.create_task(call_api(
        "calling the API", result=2000, delay=5
    ))

    max_timeout = 3

    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=max_timeout)
    except TimeoutError:
        print('The task took more than expected and will complete soon.')
        result = await task
        print(result)

asyncio.run(main6())

print("\nshielding a task from cancellation\n")


async def my_coroutine(id, delay):
    print(f"Coroutine {id} started")
    await asyncio.sleep(delay)
    print(f"Coroutine {id} finished")


async def main7():
    tasks = [asyncio.create_task(my_coroutine(1, 3)), asyncio.create_task(
        my_coroutine(2, 1)), asyncio.create_task(my_coroutine(3, 2))]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"Task {task.get_name()} completed")

asyncio.run(main7())
