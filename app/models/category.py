from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .products import Product

class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=True)

    products: Mapped[list['Product']] = relationship(back_populates='category')
