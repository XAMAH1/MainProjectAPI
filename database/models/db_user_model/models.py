from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, text

from database.base import Base
from ..db_role_model import RoleBaseModel


class UserBaseModel(Base):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(
        primary_key=True,
    )
    nickname: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )
    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    role: Mapped[RoleBaseModel] = mapped_column(

    )

    subscription: Mapped[str] = mapped_column(
        ForeignKey('subscription.name'),
        nullable=False,
    )
    subscription_start_time: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False,
    )
    subscription_end_time: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now() + INTERVAL '1 year')",),
        nullable=False,
    )

    autme_real: Mapped["AutmeBaseModel"] = relationship(
        back_populates="user_real"
    )

    subscription_real: Mapped["SubscriptionBaseModel"] = relationship(
        back_populates="user_real"
    )
