class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def set_name(self, name):
        self.name = name

    def clear(self):
        self.items = []

    def __str__(self):
        result = f"Catalog {self.name}:"
        for item in self.items:
            result += "\n\t" + str(item)
        return result