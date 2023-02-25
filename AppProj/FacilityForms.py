from wtforms import Form, StringField, IntegerField, DateTimeField, validators

class CreateFacilityForm(Form):
    name = StringField('Name of facility', [validators.DataRequired()])
    location = StringField('Location of facility', [validators.DataRequired()])
    quantity = IntegerField('Current number of people', [validators.InputRequired()])
    max = IntegerField('Maximum number of people allowed', [validators.DataRequired()])
    opentime = StringField('Opening Time (Hour:Minute:Second)', [validators.DataRequired()])
    closetime = StringField('Closing Time (Hour:Minute:Second)', [validators.DataRequired()])
