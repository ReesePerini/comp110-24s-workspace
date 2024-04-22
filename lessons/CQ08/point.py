"""Practice with Methods."""
from __future__ import annotations

__author__ = "730384323"


# class definition
class Point:
    """Making a new class, Point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Create a new Point object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Update x and y attributes by a given factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns a new Point based on a given factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point