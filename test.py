import time
import asyncio

async def task1():
    print("Task 1: Before blocking")
    time.sleep(2)  # Event loop stuck here - can't switch tasks!
    print("Task 1: After blocking")

async def task2():
    print("Task 2: Running")

async def main():
    asyncio.create_task(task1())
    asyncio.create_task(task2())
    await asyncio.sleep(0)

asyncio.run(main())