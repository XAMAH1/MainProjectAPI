from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base import Base


class DeviceBaseModel(Base):
    __tablename__ = 'device'

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
    )
    ip_device: Mapped[str] = mapped_column(
        nullable=False,
    )

    token_real: Mapped["TokenBaseModel"] = relationship(
        back_populates="device_real"
    )