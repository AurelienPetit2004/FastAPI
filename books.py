from fastapi import FastAPI
import asyncio


app = FastAPI()

@app.get("/")
async def first_api():
    return {"message": "Hello Eric!"}



async def fetch(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    print(f"done for {id}")
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    task1 = asyncio.create_task(fetch(1, 2))
    task2 = asyncio.create_task(fetch(2, 3))

    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch(3, 1))

    result3 = await task3

    print(result1, result2, result3)


asyncio.run(main())
