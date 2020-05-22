# We have a class defined for vehicles. Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a
# blue van named Jump worth $10,000.00. An example of usage:

# # define the Vehicle class


class Vehicle:
    def __init__(self, name="", kind="car", color="", value="$100.00"):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth {self.value}."
        return desc_str


def main():
    car1 = Vehicle("Fer", "convertible", "red", "$60,000.00")
    car2 = Vehicle("Jump", "van", "blue", "$10,000.00")
    print(car1.description())
    print(car2.description())


if __name__ == "__main__":
    main()
