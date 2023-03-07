from django.db import models


class PollingUnit(models.Model):
    polling_unit_id = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.CharField(max_length=50)
    polling_unit_number = models.CharField(max_length=50)
    polling_unit_name = models.CharField(max_length=50)
    polling_unit_description = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField()
    user_ip_address = models.CharField(max_length=50)


class PollingUnitResult(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party_abbreviation = models.CharField(max_length=50)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField()
    user_ip_address = models.CharField(max_length=50)
