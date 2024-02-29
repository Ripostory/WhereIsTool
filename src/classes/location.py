"""
The most basic unit of organization, a Location. Stores Items, and can contain sub-locations (such as shelves)
"""
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.classes.base import WIBase
from src.classes.item import Item


class Location(WIBase):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    sub_locations: Mapped[List["Location"]] = relationship(
        back_populates="parent_location"
    )
    parent_location_id: Mapped[Optional[int]] = mapped_column(ForeignKey("locations.id"))
    parent_location: Mapped[Optional["Location"]] = relationship(remote_side=[id])
    items: Mapped[List["Item"]] = relationship(
        back_populates="location", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Location(id={self.id!r}, name={self.name!r})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def update_from_key(self, key: str, value: any):
        match key:
            case "location_id":
                pass
            case "parent_location_id":
                self.parent_location_id = value
            case "name":
                self.name = value
            case _:
                raise KeyError(f"{key} is Invalid")
