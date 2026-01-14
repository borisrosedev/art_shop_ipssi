from datetime import datetime as dt, timezone
from uuid import uuid4,  UUID
from sqlalchemy import Integer, String, Enum as AlchemyEnum
from enum import Enum
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import Mapped, mapped_column
from .. import db
from .timestamp import TimestampModel


class UserRole(Enum):
    standard = "standard"
    premium = "premium"
    admin = "admin"

class User(TimestampModel):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    photo_name: Mapped[str | None] = mapped_column(nullable=True)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname:Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(AlchemyEnum(UserRole), default=UserRole.standard, name="user_role")
    last_login: Mapped[dt | None] = mapped_column(
        nullable=True
    )
    is_blacklisted: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    has_agreed: Mapped[bool] = mapped_column(default=False,nullable=False)

    @property
    def password(self):
         raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self, value: str):
        self.password_hash = generate_password_hash(value, "scrypt", salt_length=16)

    def check_password(self, value:str)-> bool:
        return check_password_hash(self.password_hash, value)

    def to_dic(self) -> dict:
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email, 
            "role": self.role.value,
            "is_verified": self.is_verified,
        }