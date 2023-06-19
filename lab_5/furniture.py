from abc import ABC, abstractmethod


# Abstract Product: furniture
class furniture(ABC):
    @abstractmethod
    def create_furniture(self):
        pass


# Concrete Product: table
class table (furniture):
    def create_furniture(self):
        print("Creating table...")


# Concrete Product: chair
class chair (furniture):
    def create_furniture(self):
        print("Creating chair...")


# Concrete Product: KinderSurprise
class sofa (furniture):
    def create_furniture(self):
        print("Creating Kinder Surprise...")





# Abstract Factory: FurnitureFactory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_furniture(self) -> furniture:
        pass

    def pack_furniture(self):
        return "furniture ready"


# Concrete Factory: factory2
class factory2(FurnitureFactory):
    def create_furniture(self) -> furniture:
        return chair()
    def create_furniture(self) -> furniture:
        return table()


# Concrete Factory: factory1
class factory1(FurnitureFactory):
    def create_chair(self) -> furniture:
        return chair()

    def create_table(self) -> furniture:
        return table()

    def create_sofa(self) -> furniture:
        return sofa()


# Usage
factory1 = factory1()

chair = factory1.create_chair()
chair.create_furniture()
# Вывод: Creating chair...

sofa = factory1.create_sofa()
table.create_furniture()
# Вывод: Creating sofa...


table = factory1.create_table()
if table is not None:
    table.create_furniture()
else:
    print("table not available")
# Вывод: table not available

packaged_furniture = factory1.pack_furniture()
print(packaged_furniture)