class User:
    count_id = 0

    def __init__(self, first_name, last_name, ic, phone_no, room_no, time, q1, q2, q3, q4, q5, q6, q7, status):
        User.count_id += 1


        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ic = ic
        self.__phone_no = phone_no
        self.__room_no = room_no
        self.__time = time
        self.__q1 = q1
        self.__q2 = q2
        self.__q3 = q3
        self.__q4 = q4
        self.__q5 = q5
        self.__q6 = q6
        self.__q7 = q7
        self.__ans = []
        self.__status = status

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_ic(self):
        return self.__ic

    def get_phone_no(self):
        return self.__phone_no

    def get_room_no(self):
        return self.__room_no

    def get_time(self):
        return self.__time

    def get_q1(self):
        return self.__q1

    def get_q2(self):
        return self.__q2

    def get_q3(self):
        return self.__q3

    def get_q4(self):
        return self.__q4

    def get_q5(self):
        return self.__q5

    def get_q6(self):
        return self.__q6

    def get_q7(self):
        return self.__q7

    def get_status(self):
        return self.__status

    def get_ans(self):
        return self.__ans

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_ic(self, ic):
        self.__ic = ic

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def set_room_no(self, room_no):
        self.__room_no = room_no

    def set_time(self, time):
        self.__time = time

    def set_q1(self, q1):
        self.__q1 = q1

    def set_q2(self, q2):
        self.__q2 = q2

    def set_q3(self, q3):
        self.__q3 = q3

    def set_q4(self, q4):
        self.__q4 = q4

    def set_q5(self, q5):
        self.__q5 = q5

    def set_q6(self, q6):
        self.__q6 = q6

    def set_q7(self, q7):
        self.__q7 = q7

    def set_status(self):
        for i in self.__ans:
            if i == "Yes":
                self.__status = "Danger"
                break
            else:
                self.__status = "Safe"

    def set_ans(self):
        self.__ans = [self.get_q1(), self.get_q2(), self.get_q3(), self.get_q4(), self.get_q5(), self.get_q6(),
                      self.get_q7()]
