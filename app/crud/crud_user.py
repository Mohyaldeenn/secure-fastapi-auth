
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

async def get_user_by_email(db: Session, *, email: str) -> User | None:
    """
    Get a user by their email address.
    """
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_user(db: Session, *, user_in: UserCreate) -> User:
    """
    Create a new user in the database.
    """
    hashed_password = get_password_hash(user_in.password)
    # Create a new User model instance
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user