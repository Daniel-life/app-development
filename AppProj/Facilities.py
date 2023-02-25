import datetime

class Facilities:
    count_id = 0

    def __init__(self, name, location, max, quantity, opentime, closetime):
        Facilities.count_id += 1
        self.__facility_id = Facilities.count_id
        self.__name = name
        self.__location = location
        self.__max = max
        self.__quantity = quantity
        self.__opentime = datetime.datetime.strptime(opentime, "%H:%M:%S").strftime("%H:%M:%S")
        self.__closetime = datetime.datetime.strptime(closetime, "%H:%M:%S").strftime("%H:%M:%S")
        self.__img = ""

    def get_facility_id(self):
        return self.__facility_id
    def get_name(self):
        return self.__name
    def get_location(self):
        return self.__location
    def get_max(self):
        return self.__max
    def get_quantity(self):
        return self.__quantity
    def get_opentime(self):
        return self.__opentime
    def get_closetime(self):
        return self.__closetime
    def get_img(self):
        return self.__img


    def set_name(self, name):
        self.__name = name
    def set_location(self, location):
        self.__location = location
    def set_max(self, max):
        self.__max = max
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def set_opentime(self, o):
        self.__opentime = datetime.datetime.strptime(o, "%H:%M:%S").strftime("%H:%M:%S")
    def set_closetime(self, c):
        self.__closetime = datetime.datetime.strptime(c, "%H:%M:%S").strftime("%H:%M:%S")
    def set_img(self, i):
        self.__img = i

    def time_in_range(self, x):
        if self.get_opentime() <= self.get_closetime():
            return self.get_opentime() <= x <= self.get_closetime()
        else:
            return self.get_opentime() <= x or x <= self.get_closetime()
