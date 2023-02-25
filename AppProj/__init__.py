from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from FacilityForms import CreateFacilityForm
import Facilities, shelve, User, Schedule

from declarationForm import CreateUserForm

from ScheduleForms import CreateScheduleForm

app = Flask(__name__)
app.secret_key = "OCML3BRawWEUdkgcuKHLpw"

admins = {
    "admin1": {
        "username": "admin1",
        "password": "1",
        "bio": "admin?"
    }
}
customers = {
    "customer1": {
        "username": "customer1",
        "password": "2",
        "bio": "customer?"
    },
    "customer2": {
        "username": "customer2",
        "password": "3",
        "bio": "customer?"
    }
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        req = request.form

        username = req.get("username")
        password = req.get("password")
        u = req.get("u")

        if u == "admin":
            if not username in admins:
                print("Username not found")

                return redirect(request.url)
            else:
                user = admins[username]

            if not password == user["password"]:
                print("Incorrect password")

                return redirect(request.url)

            else:
                session["ADMINS"] = user["username"]
                print(session)
                print("session username set")

                return redirect(url_for("index"))
        elif u == "customer":
            if not username in customers:
                print("Username not found")

                return redirect(request.url)
            else:
                user = customers[username]

            if not password == user["password"]:
                print("Incorrect password")

                return redirect(request.url)

            else:
                session["CUSTOMERS"] = user["username"]
                print(session)
                print("session username set")

                return redirect(url_for("index2"))

    return render_template("login.html")


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route("/log-out-admin")
def log_out_admin():
    session.pop("ADMINS", None)
    print(session)

    return redirect(url_for("login"))


@app.route("/log-out-customer")
def log_out_customer():
    session.pop("CUSTOMERS", None)
    print(session)

    return redirect(url_for("login"))


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        var = request.form.get('f')
        print(var)

        return redirect(url_for('test'))

    return render_template('test.html')


@app.route('/adminCrowdControl', methods=['GET', 'POST'])
def adminCrowdControl():
    create_facility_form = CreateFacilityForm(request.form)
    if request.method == 'POST' and create_facility_form.validate():
        img = request.form.get('f')
        facilities_dict = {}
        db = shelve.open('facilities.db', 'c')

        try:
            facilities_dict = db['Facilities']
        except:
            print("Error in retrieving Facilities from facilities.db.")

        try:
            datetime.strptime(create_facility_form.opentime.data, "%H:%M:%S").strftime("%H:%M:%S")
            datetime.strptime(create_facility_form.opentime.data, "%H:%M:%S").strftime("%H:%M:%S")
            try:
                int(create_facility_form.quantity.data)
                int(create_facility_form.max.data)
                if int(create_facility_form.quantity.data) > create_facility_form.max.data:
                    facilities = Facilities.Facilities(create_facility_form.name.data,
                                                       create_facility_form.location.data,
                                                       create_facility_form.max.data, create_facility_form.max.data,
                                                       create_facility_form.opentime.data,
                                                       create_facility_form.closetime.data)

                else:
                    facilities = Facilities.Facilities(create_facility_form.name.data,
                                                       create_facility_form.location.data,
                                                       create_facility_form.max.data,
                                                       create_facility_form.quantity.data,
                                                       create_facility_form.opentime.data,
                                                       create_facility_form.closetime.data)
            except:
                print("quantity or max wrong")
                return redirect(url_for('adminCrowdControl'))
        except:
            print("time wrong")
            return redirect(url_for('adminCrowdControl'))

        facilities.set_img(img)
        facilities_dict[facilities.get_facility_id()] = facilities
        db['Facilities'] = facilities_dict
        db.close()

        return redirect(url_for('retrieve_facilities'))

    return render_template('adminCrowdControl.html', form=create_facility_form)


@app.route('/retrieveFacilities')
def retrieve_facilities():
    facilities_dict = {}
    db = shelve.open('facilities.db', 'r')
    facilities_dict = db['Facilities']
    db.close()

    facilities_list = []
    for key in facilities_dict:
        facility = facilities_dict.get(key)
        facilities_list.append(facility)

    now = datetime.now().strftime("%H:%M:%S")
    return render_template('retrieveFacilities.html', count=len(facilities_list), facilities_list=facilities_list,
                           now=now)


@app.route('/retrieveFacilitiesUser')
def retrieve_facilities_user():
    facilities_dict = {}
    db = shelve.open('facilities.db', 'r')
    facilities_dict = db['Facilities']
    db.close()

    facilities_list = []
    for key in facilities_dict:
        facility = facilities_dict.get(key)
        facilities_list.append(facility)

    now = datetime.now().strftime("%H:%M:%S")
    return render_template('retrieveFacilitiesUser.html', count=len(facilities_list), facilities_list=facilities_list,
                           now=now)


@app.route('/updateFacilities/<int:id>/', methods=['GET', 'POST'])
def update_facilities(id):
    update_facility_form = CreateFacilityForm(request.form)
    if request.method == 'POST' and update_facility_form.validate():
        img = request.form.get('f')
        facilities_dict = {}
        db = shelve.open('facilities.db', 'w')
        facilities_dict = db['Facilities']

        try:
            datetime.strptime(update_facility_form.opentime.data, "%H:%M:%S").strftime("%H:%M:%S")
            datetime.strptime(update_facility_form.opentime.data, "%H:%M:%S").strftime("%H:%M:%S")
            try:
                int(update_facility_form.quantity.data)
                int(update_facility_form.max.data)
                facility = facilities_dict.get(id)
                facility.set_name(update_facility_form.name.data)
                facility.set_location(update_facility_form.location.data)
                if int(update_facility_form.quantity.data) > facility.get_max():
                    facility.set_quantity(update_facility_form.max.data)
                else:
                    facility.set_quantity(update_facility_form.quantity.data)
                facility.set_max(update_facility_form.max.data)
                facility.set_opentime(update_facility_form.opentime.data)
                facility.set_closetime(update_facility_form.closetime.data)
                facility.set_img(img)

                db['Facilities'] = facilities_dict
                db.close()

                return redirect(url_for('retrieve_facilities'))
            except:
                return redirect(url_for('retrieve_facilities'))
        except:
            return redirect(url_for('retrieve_facilities'))
    else:
        facilities_dict = {}
        db = shelve.open('facilities.db', 'r')
        facilities_dict = db['Facilities']
        db.close()

        facility = facilities_dict.get(id)
        update_facility_form.name.data = facility.get_name()
        update_facility_form.location.data = facility.get_location()
        update_facility_form.quantity.data = facility.get_quantity()
        update_facility_form.max.data = facility.get_max()
        update_facility_form.opentime.data = facility.get_opentime()
        update_facility_form.closetime.data = facility.get_closetime()

        return render_template('updateFacilities.html', form=update_facility_form, facility=facility)


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('HealthDeclaration.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from HealthDeclaration.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.ic.data, create_user_form.phone_no.data,
                         create_user_form.room_no.data,
                         date_time, create_user_form.q1.data,
                         create_user_form.q2.data, create_user_form.q3.data, create_user_form.q4.data,
                         create_user_form.q5.data, create_user_form.q6.data,
                         create_user_form.q7.data, create_user_form.status.data)
        user.set_status()

        user.set_ans()
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_users'))
    return render_template('declarationForm.html', form=create_user_form)


@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('HealthDeclaration.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        user.set_ans()
        user.set_status()
        if user.get_first_name() == session["CUSTOMERS"]:
            users_list.append(user)

    return render_template('formInputs.html', count=len(users_list), users_list=users_list)


@app.route('/retrieveAdmin')
def retrieve_admin():
    ok = 0
    users_dict = {}
    db = shelve.open('HealthDeclaration.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        user.set_ans()
        user.set_status()
        users_list.append(user)
        if user.get_status() == "Safe":
            ok += 1
            print(ok)

    return render_template('retrieve_user_info.html', count=len(users_list), users_list=users_list, safe=ok)


@app.route('/viewDetails/<int:id>/')
def view_details(id):
    update_user_form = CreateUserForm(request.form)
    users_dict = {}
    try:
        db = shelve.open('HealthDeclaration.db', 'r')
        users_dict = db['Users']
        db.close()
    except IOError:
        print("error in retrieving updated info")
    except:
        print("an unknown error has occured.")
    else:
        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.ic.data = user.get_ic()
        update_user_form.phone_no.data = user.get_phone_no()
        update_user_form.room_no.data = user.get_room_no()
        update_user_form.q1.data = user.get_q1()
        update_user_form.q2.data = user.get_q2()
        update_user_form.q3.data = user.get_q3()
        update_user_form.q4.data = user.get_q4()
        update_user_form.q5.data = user.get_q5()
        update_user_form.q6.data = user.get_q6()
        update_user_form.q7.data = user.get_q7()
        user.get_status()

    return render_template('viewDetails.html', form=update_user_form)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('HealthDeclaration.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_ic(update_user_form.ic.data)
        user.set_phone_no(update_user_form.phone_no.data)
        user.set_room_no(update_user_form.room_no.data)
        user.set_time(date_time)
        user.set_q1(update_user_form.q1.data)
        user.set_q2(update_user_form.q2.data)
        user.set_q3(update_user_form.q3.data)
        user.set_q4(update_user_form.q4.data)
        user.set_q5(update_user_form.q5.data)
        user.set_q6(update_user_form.q6.data)
        user.set_q7(update_user_form.q7.data)
        user.set_ans()
        user.set_status()

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('HealthDeclaration.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.ic.data = user.get_ic()
        update_user_form.phone_no.data = user.get_phone_no()
        update_user_form.room_no.data = user.get_room_no()
        update_user_form.q1.data = user.get_q1()
        update_user_form.q2.data = user.get_q2()
        update_user_form.q3.data = user.get_q3()
        update_user_form.q4.data = user.get_q4()
        update_user_form.q5.data = user.get_q5()
        update_user_form.q6.data = user.get_q6()
        update_user_form.q7.data = user.get_q7()
        user.get_status()

        return render_template('update_declaration_form.html', form=update_user_form)


@app.route('/userRoomService', methods=['GET', 'POST'])
def userRoomService():
    create_schedule_form = CreateScheduleForm(request.form)

    if request.method == 'POST' and create_schedule_form.validate():

        schedules_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            schedules_dict = db['Schedules']
        except:
            print("Error in retrieving Schedules from storage.db.")

        schedule = Schedule.Schedule(create_schedule_form.cabin_no.data, create_schedule_form.date.data,
                                     create_schedule_form.time.data, create_schedule_form.remarks.data)
        schedules_dict[schedule.get_id()] = schedule
        db['Schedules'] = schedules_dict

        db.close()

        # session['schedule_created'] = schedule.get_first_name() + ' ' + schedule.get_last_name()

        return redirect(url_for('userMySchedule'))
    return render_template('userRoomService.html', form=create_schedule_form)


@app.route('/userMySchedule')
def userMySchedule():
    schedules_dict = {}
    db = shelve.open('storage.db', 'r')
    schedules_dict = db['Schedules']
    db.close()

    schedules_list = []
    for key in schedules_dict:
        schedule = schedules_dict.get(key)
        schedules_list.append(schedule)

    return render_template('userMySchedule.html', count=len(schedules_list), schedules_list=schedules_list)


@app.route('/roomService')
def roomService():
    schedules_dict = {}
    db = shelve.open('storage.db', 'r')
    schedules_dict = db['Schedules']
    db.close()

    schedules_list = []
    for key in schedules_dict:
        schedule = schedules_dict.get(key)
        schedules_list.append(schedule)

    return render_template('roomService.html', count=len(schedules_list), schedules_list=schedules_list)


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update_schedule(id):
    update_form = CreateScheduleForm(request.form)
    if request.method == 'POST' and update_form.validate():

        schedules_dict = {}
        db = shelve.open('storage.db', 'w')
        schedules_dict = db['Schedules']

        schedule = schedules_dict.get(id)
        schedule.set_cabin_no(update_form.cabin_no.data)
        schedule.set_date(update_form.date.data)
        schedule.set_time(update_form.time.data)
        schedule.set_remarks(update_form.remarks.data)

        db['Schedules'] = schedules_dict
        db.close()

        # session['schedule_updated'] = schedule.get_first_name() + ' ' + schedule.get_last_name()

        return redirect(url_for('roomService'))
    else:
        schedules_dict = {}
        db = shelve.open('storage.db', 'r')
        schedules_dict = db['Schedules']
        db.close()

        schedule = schedules_dict.get(id)
        update_form.cabin_no.data = schedule.get_cabin_no()
        update_form.date.data = schedule.get_date()
        update_form.time.data = schedule.get_time()
        update_form.remarks.data = schedule.get_remarks()

        return render_template('update.html', form=update_form)


@app.route('/deleteSchedule/<int:id>', methods=['POST'])
def delete_schedule(id):
    schedules_dict = {}
    db = shelve.open('storage.db', 'w')
    schedules_dict = db['Schedules']

    schedule = schedules_dict.pop(id)

    db['Schedules'] = schedules_dict
    db.close()

    # session['schedule_deleted'] = schedule.get_first_name() + ' ' + schedule.get_last_name()

    return redirect(url_for('userMySchedule'))


if __name__ == '__main__':
    app.run()
