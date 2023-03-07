from django import forms
from django.db import connection


class LgaForm(forms.Form):
    lgas = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM lga")
        lgas = cursor.fetchall()

    choices = [(lga[0], lga[1]) for lga in lgas]
    lga = forms.ChoiceField(choices=choices, label='Select LGA')
