class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.real_part == 0 and self.imaginary_part == 0:
            return "0"
        elif self.real_part == 0:
            return f"{self.imaginary_part}i"
        elif self.imaginary_part == 0:
            return f"{self.real_part}"
        elif self.imaginary_part > 0:
            return f"{self.real_part} + {self.imaginary_part}i"
        else:
            return f"{self.real_part} - {abs(self.imaginary_part)}i"

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real_part}, {self.imaginary_part})"

    def re(self) -> float:
        return self.real_part

    def im(self) -> float:
        return self.imaginary_part

    def __eq__(self, other: "ComplexNumber") -> bool:
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.real_part, -self.imaginary_part)

    def __neg__(self) -> "ComplexNumber":
        return ComplexNumber(-self.real_part, -self.imaginary_part)

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        real = self.real_part + other.real_part
        imag = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real, imag)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        real = self.real_part - other.real_part
        imag = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real, imag)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        real = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        imag = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        return ComplexNumber(real, imag)

    def inverse(self) -> "ComplexNumber":
        denominator = (self.real_part ** 2) + (self.imaginary_part ** 2)
        real = self.real_part / denominator
        imag = -self.imaginary_part / denominator
        return ComplexNumber(real, imag)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        return self * other.inverse()
