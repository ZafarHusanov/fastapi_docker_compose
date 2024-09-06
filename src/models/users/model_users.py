
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Column, Integer


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )

    # id: Mapped[int] = mapped_column(primary_key=True)
    # username: Mapped[str] = mapped_column(String(50))
    # password: Mapped[str] = mapped_column(String())
    #
    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, username={self.username!r})"