from sqlalchemy.orm import DeclarativeBase

from database.settings import ECHO_MOD


class Base(DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        if ECHO_MOD:
            cols = []
            for idx, col in enumerate(self.__table__.columns.keys()):
                if col in self.repr_cols or idx < self.repr_cols_num:
                    cols.append(f"{col}={getattr(self, col)}")

            return f"<{self.__class__.__name__} {', '.join(cols)}>"

