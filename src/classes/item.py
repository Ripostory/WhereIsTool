"""
The most basic of Objects, a findable Item. Keeps track of what it is, and where it was last seen.
"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.classes.base import WIBase
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.classes.location import Location
else:
    Location = "Location"


class Item(WIBase):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    location: Mapped["Location"] = relationship(back_populates="items")

    def __repr__(self) -> str:
        return f"Item(name='{self.name}', location_id='{self.location_id}')"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
