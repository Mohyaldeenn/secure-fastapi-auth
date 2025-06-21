
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create an asynchronous engine to connect to the database
engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create a factory for asynchronous sessions
# The expire_on_commit=False is important for using session objects outside of a request context in FastAPI
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False
)