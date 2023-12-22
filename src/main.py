import asyncio
from pokemon import Pokemon


async def main():
    pokemon = Pokemon()
    while pokemon.running:
        pokemon.mainloop()
        await asyncio.sleep(0)
    pokemon.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
