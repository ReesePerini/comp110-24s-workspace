"""Practice making points."""
from lessons.CQ08.point import Point

my_point: Point = Point(2.0, 4.0)
my_point.scale_by(2)

print(my_point.x)
print(my_point.y)

other_point: Point = Point(1.0, 3.0)
other_point.scale(3)

print(other_point.x)
print(other_point.y)