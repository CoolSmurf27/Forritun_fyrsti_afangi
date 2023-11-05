

class Vector:
    TOLERANCE = 0.000_000_1

    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"[[ {self.x} {self.y} {self.z} ]]"

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: "Vector") -> bool:
        if isinstance(other, Vector):
            return abs(self - other) < self.TOLERANCE
        return False

    def __mul__(self, scalar: float) -> "Vector":
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self * scalar


    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector.

        This means that Python will be able to recreate the object
        from the representation
        when repr() is used in conjunction with functions like eval().
        """

        return f"Vector({self.x}, {self.y}, {self.z})"


    def __gt__(self, other: "Vector") -> bool:
        return abs(self) > abs(other)

    def __ge__(self, other: "Vector") -> bool:
        return abs(self) >= abs(other)

    def __lt__(self, other: "Vector") -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: "Vector") -> bool:
        return abs(self) <= abs(other)

    def dot(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector(x, y, z)

