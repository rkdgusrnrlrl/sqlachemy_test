import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from models import Base

async def async_main() -> None:
    engine = create_async_engine('sqlite+aiosqlite://', echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(async_main())
