from typing import List
from models.base import Base, str_255
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, text, ForeignKey, CHAR
from enum import Enum as PyEnum


class Status(PyEnum):
    ACTIVE = "active"
    BANNED = "banned"
    INACTIVE = "inactive"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str_255]
    email: Mapped[str_255] = mapped_column(unique=True)
    status: Mapped[Status] = mapped_column(
        Enum(Status), default=Status.ACTIVE, server_default=text(f"'{Status.ACTIVE}'")
    )

    posts: Mapped[List["Post"]] = relationship("Post", back_populates="user")  # type: ignore
    passport: Mapped["Passport"] = relationship()


class Passport(Base):
    __tablename__ = "passports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
