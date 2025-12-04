from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated
from sqlalchemy import String

str_255 = Annotated[str, mapped_column(String(255))]


class Base(DeclarativeBase):
    pass
