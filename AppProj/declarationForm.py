from wtforms import Form, StringField, RadioField, TextAreaField, IntegerField, validators
from wtforms_validators import AlphaNumeric


class CreateUserForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    ic = StringField('IC number', [validators.Length(min=1), validators.DataRequired(), AlphaNumeric()])
    phone_no = IntegerField('Phone number', [validators.DataRequired()])
    room_no = StringField('Room number', [validators.DataRequired()])
    q1 = RadioField('Q1. Are you feeling unwell with fever or flu-like symptoms, including mild cough, sort throat or '
                    'loss of the sense of smell? '
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    q2 = RadioField('Q2. Are you currently serving a Quarantine Order (QO),Stay-Home Notice (SHN) or Leave of Absence('
                    'LOA)? ', choices=[('Yes', 'Yes'), ('No', 'No')])

    q3 = RadioField('Q3. Do you have any contact or have been notified that you were in close contact with a '
                    'COVID-19 case within the last 14 days? '
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    q4 = RadioField('Q4. Do you have any adult member of your household (aged 18 and above) who is unwell (with fever '
                    'or( '
                    'flu-like symptoms, cough, sore throat or a loss of the sense of smell? '
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    q5 = RadioField('Q5. Do you have a household member who is currently serving Stay Home Notice - SHN (due to '
                    'overseas travel) in the same place of residence as yourself? '
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    q6 = RadioField('Q6. Do you have a household member who is on Home Quarantine order and is currently staying in '
                    'the same residence as yourself? '
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    q7 = RadioField('Q7. Have you volunteered/worked in an environment with a higher risk of exposure to COVID-19 '
                    'cases (e.g. swab-test site, foreign-worker dormitory, isolation facility, COVID-19 patient '
                    'transport, etc) in the last 14 days?'
                    , choices=[('Yes', 'Yes'), ('No', 'No')])

    status = TextAreaField('Status', [validators.Optional()])
