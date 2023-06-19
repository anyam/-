import random


class Massage:
    def __init__(self, user1, user2, sign, cost):
        self.user1 = user1
        self.user2 = user2
        self.sign = sign
        self.cost = cost

    def __str__(self):
        return f"СМС: от кого: {self.user1} кому: {self.user2}, Вес: {self.sign} кол-во знаков, Стоимость: {self.cost} $"


class TempDatabase:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def send_messages(self, main_database):
        print("Отправка сообщений в основную базу данных:")
        for index, message in enumerate(self.messages, start=1):
            main_database.add_message(message)
            print(f"{index}. {message}")
        print("Сообщения успешно отправлены.")
        self.messages = []


class MainDatabase:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

        user1 = message.user1


class Messenger:
    def __init__(self):
        self.temporary_database = TempDatabase()
        self.main_database = MainDatabase()
        self.users = ["apple", "pear", "grape", "strawberry", "carrot"]

    def generate_messages(self, num_messages):
        for _ in range(num_messages):
            user1 = random.choice(self.users)
            user2 = random.choice([user for user in self.users if user != user1])
            sign = random.randint(1, 100)
            cost = random.randint(10, 100)
            message = Massage(user1, user2, sign, cost)
            self.temporary_database.add_message(message)

        if len(self.temporary_database.messages) >= 10:
            self.temporary_database.send_messages(self.main_database)



messenger = Messenger()
messenger.generate_messages(5)