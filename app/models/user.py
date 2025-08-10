from app.backend.db import Base
from sqlalchemy.orm import Mapped, mapped_column




class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_supplier: Mapped[bool] = mapped_column(default=False)
    is_customer: Mapped[bool] = mapped_column(default=True)

    # reviews: Mapped[list["Review"]] = relationship("Review", back_populates="user", cascade="all, delete-orphan")