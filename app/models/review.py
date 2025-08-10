from sqlalchemy.orm import Mapped, mapped_column
from app.backend.db import Base
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy import DateTime, func



class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    comment: Mapped[str] = mapped_column(nullable=True)
    comment_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    grade: Mapped[float]
    is_active: Mapped[bool] = mapped_column(default=True)


