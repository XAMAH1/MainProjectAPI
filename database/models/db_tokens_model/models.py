from datetime import datetime
from sqlalchemy import text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base import Base


class TokenBaseModel(Base):
    __tablename__ = 'token'

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('autme.id'),
        nullable=False,
    )
    token: Mapped[str] = mapped_column(
        nullable=False,
    )
    create_date: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        nullable=False,
    )
    device: Mapped[int] = mapped_column(
        ForeignKey('device.id'),
        nullable=False,
    )

    autme_real: Mapped["AutmeBaseModel"] = relationship(
        back_populates="token_real"
    )
    device_real: Mapped["DeviceBaseModel"] = relationship(
        back_populates="token_real"
    )