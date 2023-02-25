class Schedule:
    count_id = 0

    def __init__(self, cabin_no, date, time, remarks):
        Schedule.count_id += 1
        self.__id = Schedule.count_id
        self.__cabin_no = cabin_no
        self.__date = date
        self.__time = time
        self.__remarks = remarks


    def get_id(self):
        return self.__id

    def get_cabin_no(self):
        return self.__cabin_no

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_remarks(self):
        return self.__remarks



    def set_id(self, id):
        self.__id = id

    def set_cabin_no(self, cabin_no):
        self.__cabin_no = cabin_no

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    def set_remarks(self, remarks):
        self.__remarks = remarks


