# Implement the Shape class
class Shape:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        name = type(self).__name__
        area = "{:.2f}".format(self.get_area())
        perimeter = "{:.2f}".format(self.get_perimeter())
        return f"{name} with area of {area} and perimeter of {perimeter}"




