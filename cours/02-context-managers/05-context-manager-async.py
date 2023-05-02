import contextlib
import asyncio


@contextlib.asynccontextmanager
async def simple_async_context_manager():
    print("Avant l'exécution du bloc")
    yield
    print("Après l'exécution du bloc")


async def main():
    async with simple_async_context_manager():
        print("Dans le bloc")


asyncio.run(main())
