import asyncio

async def fetch_user(id: int) -> dict:
    await asyncio.sleep(0.5)
    return {"id": id, "name":"Tahmid"}

async def main ():
    users = await asyncio.gather(
        # Running at the same time
        fetch_user(1), fetch_user(2), fetch_user(3)
    )
    print(users)

if __name__ == "__main__":
    asyncio.run(main())