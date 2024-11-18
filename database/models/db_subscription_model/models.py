from sqlalchemy.orm import Mapped, mapped_column, relationship


from ...base import Base

class SubscriptionBaseModel(Base):
    __tablename__ = 'subscription'

    name: Mapped[str] = mapped_column(
        primary_key=True
    )
    price: Mapped[float] = mapped_column(
        nullable=False,
    )
    isHide: Mapped[bool] = mapped_column(
        default=False,
        nullable=False,
    )
    access_real: Mapped[list["AccessBaseModel"]] = relationship(
        back_populates="subscription_real"
    )
    user_real: Mapped["UserBaseModel"] = relationship(
        back_populates="subscription_real"
    )