from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, ForeignKey
from database.base import Base
from ..db_type_record_model import TypeRecord


class RecordingBaseModel(Base):
    __tablename__ = 'recording'


    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    content: Mapped[str] = mapped_column(
        nullable=False,
    )
    type_recording: Mapped[TypeRecord] = mapped_column(
        nullable=False,
    )
    date_create: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
    )
    user: Mapped[str] = mapped_column(
        ForeignKey("users.email"),
        nullable=False,
    )