
class Vehicle:
    def _init_(self, name="", kind="car", color="", value=""):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth {self.value}."
        return desc_str


# Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer
# and car2 to be a blue van named Jump worth $10,000.00
car1 = Vehicle("Ferrari", "convertible", "red", "60000.00")
car2 = Vehicle("Ford", "van", "blue", "10000.00")
# test code
print(car1.description())
print(car2.description())
