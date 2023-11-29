"""
Створити клас Clothing (name, description, location, colour, size). Додати enum type: SHIRT, JEANS,
JACKET, ….Додати клас Wardrobe, котрий містить одяг.Визначити функцію are goOut(Clothing*) - вивести
кількість типів одягу та чи готова людина вийти на вулицю (якщо кількість типів більша, ніж
три - так, менша - ні). Посортуйте одяг за розміром. Додайте ще один метод до класу одягу.
"""
from enum import Enum


class ClothingType(Enum):
    """
    Enumeration representing different types of clothing
    """
    SHIRT = "shirt"
    JEANS = "jeans"
    JACKET = "jacket"


class Clothing:
    """
     Represents an individual piece of clothing
    """
    def __init__(self, name, description, location, *args):
        """
        Initializing
        """
        self.__name = name
        self.__description = description
        self.__location = location
        self.__colour = args[0]
        self.__size = args[1]
        self.__clothing_type = args[2]

    def __del__(self):
        """
        Destructed clothing
        """
        return f"Clothing {self.__name} has been destructed"

    @property
    def clothing_type(self):
        """
        Getter method for the clothing_type property
        """
        return self.__clothing_type

    @property
    def size(self):
        """
        Getter method for the size property
        """
        return self.__size

    def clothes_info(self):
        """
        Method prints all values of clothing
        """
        print(f"Name: {self.__name}")
        print(f"Description: {self.__description}")
        print(f"Location: {self.__location}")
        print(f"Colour: {self.__colour}")
        print(f"Size: {self.size}")
        print(f"Type: {self.clothing_type.value}")


class Wardrobe:
    """
    Represents a collection of clothing items
    """
    def __init__(self):
        """
        Initializing
        """
        self.clothes = []

    def add_clothes(self, clothing):
        """
        Method adds clothing to the wardrobe
        """
        self.clothes.append(clothing)

    def are_go_out(self):
        """
        The method displays the number of clothes in the wardrobe
        and indicates the readiness of a person to go outside
        """
        unique_types = set()
        unique = []
        for clothing in self.clothes:
            if clothing.clothing_type not in unique_types:
                unique_types.add(clothing.clothing_type)
                unique.append(clothing)

        print(f"Number of types of clothing: {len(unique)}")
        if len(unique) >= 3:
            print("A person is ready to go outside")
        else:
            print("A person is not ready to go outside")

    def sort_clothes(self):
        """
        The method sorts and returns clothes
        """
        self.clothes.sort(key=lambda x: x.size)
        for clothing in self.clothes:
            clothing.clothes_info()
            print("+++++++++++++++++")


if __name__ == "__main__":
    shirt_1 = Clothing("T-Shirt", "Casual cotton shirt",
                       "Wardrobe", "Blue", 33, ClothingType.SHIRT)
    jeans_1 = Clothing("Blue Jeans", "Classic denim jeans",
                       "Wardrobe", "Blue", 32, ClothingType.JEANS)
    jacket_1 = Clothing("Leather Jacket", "Stylish leather jacket",
                        "Wardrobe", "Black", 31, ClothingType.JACKET)
    shirt_2 = Clothing("T-Shirt 2", "Casual cotton shirt",
                       "Wardrobe", "Blue", 34, ClothingType.SHIRT)
    jeans_2 = Clothing("White Jeans", "Classic denim jeans",
                       "Wardrobe", "Blue", 37, ClothingType.JEANS)
    jacket_2 = Clothing("Denim Jacket", "Stylish leather jacket",
                        "Wardrobe", "Black", 31, ClothingType.JACKET)
    shirt_3 = Clothing("T-Shirt 3", "Casual cotton shirt",
                       "Wardrobe", "Blue", 33, ClothingType.SHIRT)
    jeans_3 = Clothing("Black Jeans", "Classic denim jeans",
                       "Wardrobe", "Blue", 32, ClothingType.JEANS)
    jacket_3 = Clothing("Suede Jacket", "Stylish leather jacket",
                        "Wardrobe", "Black", 31, ClothingType.JACKET)

    wardrobe = Wardrobe()
    for cloth in [shirt_1, shirt_2, shirt_3, jeans_1, jeans_2,
                  jeans_3, jacket_1, jacket_2, jacket_3]:
        wardrobe.add_clothes(cloth)

    wardrobe.sort_clothes()

    wardrobe.are_go_out()
