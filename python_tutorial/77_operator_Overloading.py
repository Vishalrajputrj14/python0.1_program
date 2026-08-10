class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 3
print(v3)  # Output: Vector(7, 10)
print(v4)  # Output: Vector(3, 4)
print(v5)  # Output: Vector(6, 9)
