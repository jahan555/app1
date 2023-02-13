from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#to take current date ->

class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registered_number = models.CharField(max_length=100)
    engine_power = models.CharField(max_length=50)
    year_manufactured = models.CharField(max_length=100)
    organisation = models.IntegerField(null=True)
    department = models.CharField(max_length=100)
    BAN = models.CharField(max_length=100)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class Drivers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    organization = models.IntegerField(null=True)
    department = models.CharField(max_length=100)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class DriverLicences(models.Model):
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    license_seriya = models.CharField(max_length=10)
    license_number = models.CharField(max_length=50)
    status = models.IntegerField(null=True)
    date_valid = models.CharField(max_length=100)
    date_registered = models.DateTimeField(default=timezone.now)


class RelCarDriver(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)
    date_assignment = models.CharField(max_length=100)
    date_registered = models.DateTimeField(default=timezone.now)


class CarMilestage(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    milestage = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class RepairServices(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class RepairCategory(models.Model):
    category_name = models.TextField(null=True)
    status = models.IntegerField(null=True)


class Repair(models.Model):
    car_id = models.IntegerField(null=True)
    repair_cat = models.ForeignKey(RepairCategory, on_delete=models.CASCADE)
    repair_service = models.IntegerField(null=True)
    repair_price = models.IntegerField(null=True)
    repair_description = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    date_registered = models.DateTimeField(default=timezone.now)


class PetrolCard(models.Model):
    card_number = models.CharField(max_length=50)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class RelPetrolCar(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    card = models.ForeignKey(PetrolCard, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class RelPetrolLimit(models.Model):
    card = models.ForeignKey(PetrolCard, on_delete=models.CASCADE)
    limit = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)


class Organizations(models.Model):
    name = models.CharField(max_length=250)
    status = models.IntegerField(null=True)




