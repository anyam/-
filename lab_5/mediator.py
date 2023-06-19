# Mediator
class RailwayStation:
    def __init__(self):
        self.trains = []
        self.passengers = []
        self.railway_track_service = RailwayTrackService()

    def register_train(self, train):
        self.trains.append(train)

    def register_passenger(self, passenger):
        self.passengers.append(passenger)

    def request_departure(self, train):
        if self.railway_track_service.check_railway_track_availability() == "свободен":
            print(f"Поезд '{train}'уехал.")
            for passenger in self.passengers:
                passenger.notify_departure()
        else:
            print(f"Поезд {train} не может выехать.")

# Service
class Train:
    def __init__(self, name):
        self.name = name

    def request_departure_clearance(self, railway_station):
        railway_station.request_departure(self)

    def __str__(self):
        return self.name

# Client
class Passenger:
    def __init__(self, name):
        self.name = name

    def notify_departure(self):
        print(f"Пассажир {self.name} уехал")



class RailwayTrackService:
    def check_railway_track_availability(self):
        return "свободен"


railway_station = RailwayStation()
train = Train("004С МОСКВА КАЗ - КИСЛОВОДСК")
railway_station.register_train(train)

passenger1 = Passenger("Ольга")
railway_station.register_passenger(passenger1)

passenger2 = Passenger("Борис")
railway_station.register_passenger(passenger2)

train.request_departure_clearance(railway_station)