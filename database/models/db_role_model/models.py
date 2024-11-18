import enum

from ...base import Base

class RoleBaseModel(enum.Enum):
    user = 'user'
    admin = 'admin'