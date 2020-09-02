from vector import Vector
from typing import NewType

linline = NewType("linline", object)

class linline:
    """A mathematical representation of a linear line

    The linear line is a simplified version of the polynomial line 'polyline'.
    
    """
    def __init__(self, rc: float, b: float) -> None:
        self.rc = rc
        self.b = b
    
    @classmethod
    def fromString(string, variable="x") -> linline:
        """Create a line from a string

        The string has to be in the form of "ax+b".\n
        Change the variable with the second argument. Pass the variable as a string like 'p'.

        """
        rc, b = string.split(variable)[:2]
        return linline(rc, b)
    
    @classmethod
    def fromVector(direction, location=Vector(0,0)):
        rc = direction.y / direction.x
        b = direction.x * location.y - direction.y * location.x
        return linline(rc, b)

    def intersect(self, other: linline) -> Vector.Vector:
        """Calculate the point on which the two lines intersect
        
        The two lines intersect on one point. Intersect() calculates
        that point and give back a vector.

        Args:
            other: a linline; the line that intersects
        """
        new_x = (other.b - self.b) / (self.rc - other.rc)
        return Vector.Vector(new_x, self.calc(new_x))

    def calc(self, x: float) -> float:
        """Calculate the output with a given x value

        The mathematical equivalent of f(x). Calc() calculates
        the value that corresponds to the x value given.

        Args:
            x: a float; the x value for the value to be calculated
        """
        return self.rc * x + self.b
        
    def __str__(self):
        return f"Linear Line: {self.rc}x + {self.b}"
    
    def __repr__(self):
        return f"linline({self.rc}x + {self.b})"

if __name__ == "__main__":
    l1 = linline(1,2)
    l2 = linline.fromString("3x+1")

