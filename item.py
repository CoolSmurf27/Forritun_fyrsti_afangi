class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def set_name(self, name):
        self.name = name 
    #update the name

    def set_category(self, category):
        self.category = category 
    #update the category

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}"
    #return the name and category of the item