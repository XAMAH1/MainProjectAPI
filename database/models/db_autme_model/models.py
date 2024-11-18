from datetime import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class AutmeBaseModel(Base):
    __tablename__ = 'autme'

    id: Mapped[str] = mapped_column(
        primary_key=True
    )
    email: Mapped[str] = mapped_column(
        ForeignKey('users.email'),
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        nullable=False,
    )
    create_date: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False,
    )

    user_real: Mapped["UserBaseModel"] = relationship(
        back_populates="autme_real"
    )
    token_real: Mapped["TokenBaseModel"] = relationship(
        back_populates="autme_real"
    )