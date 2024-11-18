from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from ...base import Base


class AccessBaseModel(Base):
    __tablename__ = 'access'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
    )
    subscription_name: Mapped[str] = mapped_column(
        ForeignKey("subscription.name"),
        nullable=False,
    )

    subscription_real: Mapped["SubscriptionBaseModel"] = relationship(
        back_populates="access_real"
    )
    #   back_populates="access_real"