class cake:
    def __init__(self):
        self.cream_cheese = None
        self.cream = None
        self.glaze = None
        self.strawberry = None

    def set_cream_cheese(self, cream_cheese):
        self.cream_cheese = cream_cheese

    def set_cream(self, cream):
        self.cream = cream

    def set_glaze(self, glaze):
        self.glaze = glaze

    def set_milk_foam(self, milk_foam):
        self.milk_foam = milk_foam

    def display(self):
        print("Ваше пирожное готово!")

# Builder
class cakeBuilder:
    def __init__(self):
        self.cake = cake()

    def cream(self):
        self.cake.set_cream("Взбивание сливок")
        print("Взбивание сливок")

    def glaze(self):
        self.cake.set_glaze("Приготовление глазури")
        print("Приготовление глазури")

    def cream_cheese(self):
        self.cake.set_cream_cheese("Приготовление кремчиза")
        print("Приготовление кремчиза")

    def get_cake(self):
        return self.cake

# Builder: client1
class client1(cakeBuilder):
    def add_strawberry(self):
        self.cake.strawberry = "Добавление клубника"
        print("Добавление клубники")

# Builder: client2
class client2(cakeBuilder):
    def cheesecake(self):
        self.cake.set_cream_cheese("Добавление кремчиза")
        print("Добавление кремчиза")

# Director
class director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def prepare_cake(self):
        self.builder.cream_cheese()
        self.builder.glaze()
        self.builder.cream()

        if isinstance(self.builder, client1):
            self.builder.add_strawberry()


        return self.builder.get_cake()


director = director()

builder_name = input("Введите имя кондитера (client1 или client2): ")

if builder_name == "client1":
    builder = client1()
elif builder_name == "client2":
    builder = client2()
else:
    builder = cakeBuilder()

director.set_builder(builder)
cake = director.prepare_cake()
cake.display()