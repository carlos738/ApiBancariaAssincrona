from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite in-memory compartilhado (permite múltiplas conexões)
DATABASE_URL = "sqlite+aiosqlite:///:memory:?cache=shared"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
