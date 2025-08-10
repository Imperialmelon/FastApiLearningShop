from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .category import Category

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    slug: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    image_url: Mapped[str]
    stock: Mapped[int]
    supplier_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    rating: Mapped[float]
    is_active: Mapped[bool] = mapped_column(default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products")
