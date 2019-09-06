class Vehicle:

    def __init__(self):
        self.number = ''


class FourWheeler(Vehicle):

    def __init__(self):
        Vehicle.__init__()


class TwoWheeler(Vehicle):

    def __init__(self):
        Vehicle.__init__()


class ParkingSection:

    def __init__(self, identifier, no_of_slots):
        self.identifier = identifier
        self.no_of_slots = no_of_slots
        self.slots = [False] * (no_of_slots+1)  # False means free and True means occupied


class TwoWheelerSection(ParkingSection):

    def __init__(self):
        ParkingSection.__init__()


class FourWheelerSection(ParkingSection):

    def __init__(self):
        ParkingSection.__init__()


class ParkingLot:

    def __init__(self):
        self.two_wheeler_charges = 20
        self.four_wheeler_charges = 40
        self.two_wheeler_section = self.__create_two_wheeler_section()
        self.four_wheeler_section = self.__create_four_wheeler_section()

    @staticmethod
    def __create_two_wheeler_section():
        return []

    @staticmethod
    def __create_four_wheeler_section():
        return []

    def change_two_wheeler_charges(self, charge):
        pass

    def change_four_wheeler_charges(self, charge):
        pass

    def park_vehicle(self, vehicle):
        pass

    def remove_vehicle(self, vehicle):
        pass

    def find_free_slot(self, vehicle_type):
        pass
