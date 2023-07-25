import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from models import Base


@pytest.fixture
async def async_engine():
    engine = create_async_engine('sqlite+aiosqlite://', echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine


@pytest.fixture
def sync_engine():
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture
def session_factory(sync_engine: Engine):
    yield sessionmaker(sync_engine)

@pytest.fixture
def auto_session_factory(sync_engine: Engine):
    auto_engine = sync_engine.execution_options(isolation_level="AUTOCOMMIT")
    yield sessionmaker(auto_engine)
