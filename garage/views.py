import csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars, CarMilestage, RelCarDriver, RelPetrolCar, PetrolCard, DriverLicences, RepairServices, Drivers, \
    Organizations, RelPetrolLimit, Repair, RepairCategory

# Create your cars page here.
def cars(request):
    cars = Cars.objects.filter(status=1)
    drivers = Drivers.objects.filter(status=1)
    repair_services = RepairServices.objects.all()
    categories = RepairCategory.objects.filter(status=1)
    car_driver = RelCarDriver.objects.filter(status=1)
    car_listview = []
    oil_cards = PetrolCard.objects.filter(status=1)
    for car in cars:
        t = {}
        t['id'] = car.id
        t['marka'] = car.brand
        t['model'] = car.model
        t['number'] = car.registered_number
        t['dep'] = car.department
        t['engine'] = car.engine_power
        t['year'] = car.year_manufactured
        t['ban'] = car.BAN
        if len(RelCarDriver.objects.filter(status=1, car=car.id)) < 1:
            t['driver'] = ' '
        else:
            drivername = RelCarDriver.objects.filter(status=1, car=car.id)[0].driver.name
            driversurname = RelCarDriver.objects.filter(status=1, car=car.id)[0].driver.surname

            t['driver'] = drivername + ' ' + driversurname
            #t['driver'] = RelCarDriver.objects.filter(status=1, car=car.id)[0].car.registered_number

        if len(RelCarDriver.objects.filter(status=1, car=car.id)) < 1:
            t['date'] = ' '
        else:
            t['date'] = RelCarDriver.objects.filter(status=1, car=car.id)[0].date_assignment
        if len(RelPetrolCar.objects.filter(car_id=car.id, status=1)) > 0:
            petrolcardID = RelPetrolCar.objects.filter(car_id=car.id, status=1)[0].card_id
            #print('petrolcard id:', petrolcardID)
            petrolcardnumber = PetrolCard.objects.filter(id=petrolcardID)[0].card_number

            petrolcardlimit = RelPetrolLimit.objects.filter(card_id=petrolcardID)[0].limit
            #print('assigned petrol card number', petrolcardnumber)
            #print(petrolcardID, petrolcardlimit, petrolcardnumber)

        else:
            petrolcardnumber = 'Yanacaq kartı seçilməyib.'
            petrolcardlimit = ''
        t['petrolcardnumber'] = petrolcardnumber
        t['petrolcardlimit'] = petrolcardlimit
        if len(CarMilestage.objects.filter(car_id=car.id, status=1)) > 0:
            milestage = CarMilestage.objects.filter(car_id=car.id, status=1)[0].milestage
        else:
            milestage = 0
        t['milestage'] = milestage
        t['milestagehistorypopupdash'] = '#milestagehistory' + str(car.id)
        t['milestagehistorypopupid'] = 'milestagehistory' + str(car.id)
        t['oilcardpopupiddash'] = '#oilCardCars' + str(car.id)
        t['oilcardpopupid'] = 'oilCardCars' + str(car.id)
        t['milestagepopupiddash'] = '#updateMileStage' + str(car.id)
        t['milestagepopupid'] = 'updateMileStage' + str(car.id)
        t['repairhistorypopupiddash'] = '#viewHistoryCars' + str(car.id)
        t['repairhistorypopupid'] = 'viewHistoryCars' + str(car.id)
        t['editcardatapopupiddash'] = '#editCars' + str(car.id)
        t['editcardatapopupid'] = 'editCars' + str(car.id)
        t['deletecariddash'] = '#deleteCar' + str(car.id)
        t['deletecarid'] = 'deleteCar' + str(car.id)
        milestagehistory = []
        for j in CarMilestage.objects.filter(car_id=car.id):
            milestageitem = {}
            milestageitem['date'] = j.date
            milestageitem['milestage'] = j.milestage
            milestagestring = str(milestageitem['date'])[:11] + ' | ' + str(milestageitem['milestage'])
            milestagehistory.append(milestagestring)

        repairhistorylist = []
        repairhistorylist2 = []
        repairstring = ''
        for i in Repair.objects.filter(car_id=car.id):
            repairitem = {}
            repairitem['date'] = i.date
            repairitem['service'] = RepairServices.objects.filter(id=i.repair_service)[0].name
            repairitem['desc'] = i.repair_description
            repairstring = str(repairitem['date']) + " tarixində " + repairitem['desc'] +" (Servis: " + repairitem['service'] + ")"
            repairhistorylist.append(repairitem)
            repairhistorylist2.append(repairstring)
        t['repairhistorylist'] = repairhistorylist
        t['repairhistorylist2'] = repairhistorylist2
        t['milestagehistory'] = milestagehistory
        #print(milestagehistory)
        car_listview.append(t)

    return render(request, 'garage/index.html', {"cars": cars, "drivers": drivers, "services": repair_services, "categories": categories, 'car_listview':car_listview})


# Create your drivers page here.
def drivers(request):
    drivers = Drivers.objects.filter(status=1)
    licenses = DriverLicences.objects.filter(status=1)
    driversListView = []
    for driver in drivers:
        t = {}
        t['id'] = driver.id
        t['fullname'] = driver.name + " " + driver.surname
        t['name'] = driver.name
        t['surname'] = driver.surname
        t['dep'] = driver.department
        #print('driver licence lennn:' , len(DriverLicences.objects.filter(status=1, driver_id=driver.id)))
        if len(DriverLicences.objects.filter(status=1, driver_id=driver.id)) > 0:
            seriya = DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].license_seriya
            #print('seriya', seriya)

            number =DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].license_number
            #print('num', number)
            t['license'] = seriya + number
            t['date'] = DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].date_valid
        else:
            t['license'] = ' '
        t['updatelicensedash'] = '#updatelicense' + str(driver.id)
        t['updatelicenseid'] = 'updatelicense' + str(driver.id)
        t['editdriverdatadash'] = '#editDriver' + str(driver.id)
        t['editdriverdataid'] = 'editDriver' + str(driver.id)
        t['deletedriverdatadash'] = '#deleteDriver' + str(driver.id)
        t['deletedriverdataid'] = 'deleteDriver' + str(driver.id)
        driversListView.append(t)



    return render(request, 'garage/drivers.html', {"driversListView": driversListView})


# Create your views here.
def oilCards(request):
    cards = PetrolCard.objects.filter(status=1)
    cars = Cars.objects.filter(status=1)

    petrolcardListView = []
    for card in cards:
        t = {}
        t['id'] = card.id
        t['number'] = card.card_number
        if len(RelPetrolLimit.objects.filter(status=1, card_id = card.id)) > 0:
            t['limit'] = RelPetrolLimit.objects.filter(status=1, card_id=card.id)[0].limit
        else:
            t['limit'] = ''
        t['changelimitpopupdash'] = '#changeOilCardLimit' + str(card.id)
        t['changelimitpopupid'] = 'changeOilCardLimit' + str(card.id)
        t['limithistorypopupdash'] = '#viewOilCardHistory' + str(card.id)
        t['limithistorypopupid'] = 'viewOilCardHistory' + str(card.id)
        t['assignhistorypopupdash'] = '#assignCard' + str(card.id)
        t['assignhistorypopupid'] = 'assignCard' + str(card.id)
        t['deletecarddash'] = '#deleteCard' + str(card.id)
        t['deletecardid'] = 'deleteCard' + str(card.id)
        limithistorylist = []
        limithistorylist2 = []
        repairstring = ''
        for i in RelPetrolLimit.objects.filter(card_id=card.id):
            limititem = {}
            limititem['date'] = i.date_registered
            limititem['limit'] = i.limit
            limitstring = str(limititem['date'])[:11] + " | " + str(limititem['limit'])
            limithistorylist.append(limititem)
            limithistorylist2.append(limitstring)
        t['limithistorylist'] = limithistorylist
        t['limithistorylist2'] = limithistorylist2

        assignhistorylist = []
        assignhistorylist2 = []
        assignstring = ''
        for i in RelPetrolCar.objects.filter(card_id=card.id):
            assignitem = {}
            assignitem['date'] = i.date_registered
            assignitem['car'] = Cars.objects.filter(id=i.car_id)[0].registered_number
            assignstring = str(assignitem['date'])[:11] + " | " + str(assignitem['car'])
            assignhistorylist.append(limititem)
            assignhistorylist2.append(assignstring)
        t['assignhistorylist'] = assignhistorylist
        t['assignhistorylist2'] = assignhistorylist2

        petrolcardListView.append(t)
    return render(request, 'garage/oilCards.html', {'petrolcardListView': petrolcardListView, 'cars': cars, 'cards': cards})


# Create your views here.
def parameters(request):
    return render(request, 'garage/settings.html')


def addCarMethod(request):
    data = request.POST.copy()
    #print('add car method: ', data)
    newcar = Cars(brand=data['marka'], model=data['model'], registered_number=data['number'], BAN=data['ban'],
                  engine_power=data['engine'], year_manufactured=data['year'], organisation=1, department=data['dep'], status=1)
    newcar.save()
    return cars(request)


def addmilestageMethod(request,id):
    data = request.POST.copy()
    #print('add milestage method: ', id,data)
    if len(CarMilestage.objects.filter(car=id, status=1)) > 0:
        for record in CarMilestage.objects.filter(car=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()
    newmilestage = CarMilestage(car_id=id, date=data['datemilestage'], milestage=data['milestage'], status=1)
    newmilestage.save()
    return cars(request)


def assignCarMethod(request):
    data = request.POST.copy()
    #print('assign car method: ', data)
    #print('relcardriver query set', RelCarDriver.objects.filter(car=data['carid'], status=1))
    #print('len relcardriver query set', len(RelCarDriver.objects.filter(car=data['carid'], status=1)))
    if len(RelCarDriver.objects.filter(car=data['carid'], status=1)) > 0:
        for record in RelCarDriver.objects.filter(car=data['carid'], status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    assigncar = RelCarDriver(car_id=data['carid'], driver_id=data['driverid'], date_assignment=data['date'], status=1)
    assigncar.save()
    return cars(request)


def addNewDriverMethod(request):
    data = request.POST.copy()
    #print('add car method: ', data)
    newdriver = Drivers(name=data['name'], surname=data['surname'], department=data['department'], status=1)
    newdriver.save()
    driverid = Drivers.objects.filter(name=data['name'], surname=data['surname'])[0].id
    newlicense = DriverLicences(driver_id=driverid, license_seriya=data['seriya'], license_number=data['number'], date_valid=data['date'], status=1)
    newlicense.save()
    return drivers(request)


def changeDriverLicenseMethod(request, id ):
    data = request.POST.copy()
    id = id #driver id
    print('driver id',id)
    if len(DriverLicences.objects.filter(driver_id=id, status=1)) > 0:
        for record in DriverLicences.objects.filter(driver_id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()
    newdriverlicense = DriverLicences(driver_id=id, license_seriya=data['seriya'], license_number=data['number'], status=1, date_valid=data['date'])
    newdriverlicense.save()
    return drivers(request)


def addOilCardMethod(request):
    data = request.POST.copy()
    #print('add oil card method: ', data)
    newpetrolcard = PetrolCard(card_number=data['number'], status=1)
    #print(1)
    newpetrolcard.save()
    #print(2)
    petrolcardid = PetrolCard.objects.filter(card_number=data['number'])[0].id
   # print(3)
    newlimit = RelPetrolLimit(card_id=petrolcardid, limit=data['limit'], status=1)
   # print(4)
    newlimit.save()
    #print(5)
    return oilCards(request)


def assignOilCardToCarMethod(request):
    data = request.POST.copy()
    print("assign oil card to car method:", data)
    if len(RelPetrolCar.objects.filter(card=data['cardid'], status=1)) > 0:
        for record in RelPetrolCar.objects.filter(car=data['cardid'], status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    assigncard = RelPetrolCar(car_id=data['carid'], card_id=data['cardid'], status=1)
    assigncard.save()
    return oilCards(request)


def changeOilCardLimitMethod(request, id ):
    data = request.POST.copy()
   # print('change petrol card limit method: ', id, data)
    if len(RelPetrolLimit.objects.filter(card_id=id, status=1)) > 0:
        for record in RelPetrolLimit.objects.filter(card_id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()
    newcardlimit = RelPetrolLimit(card_id=id, limit=data['limit'], status=1)
    newcardlimit.save()
    return oilCards(request)


def addRepairLogMethod(request):
    data = request.POST.copy()
    #print('add repair log: ', id, data)
    newrepairlog = Repair(car_id=data['carid'], date=data['date'], repair_service=data['serviceid'], repair_description=data['desc'], repair_cat_id=data['categoryid'], repair_price=data['price'])
    newrepairlog.save()
    return cars(request)


def deleteCarMethod(request,id):
    data = request.POST.copy()
    #print('delete car method: ', id, data)
    if len(Cars.objects.filter(id=id, status=1)) > 0:
        for record in Cars.objects.filter(id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    return cars(request)


def filtercar(request):
    data = request.POST.copy()
    marka = str(data["marka"])
    model = str(data["model"])
    number = str(data["number"])

    print("FILTER: ",marka, model, number)
    cars = []
    if marka=="":
            if model=="":
                    if number=="":
                            cars = Cars.objects.filter(status=1)
                    else:
                            cars =Cars.objects.filter(registered_number = number, status=1)
            else:
                    if number=="":
                            cars =Cars.objects.filter(model=model,status=1)
                    else:
                            cars =Cars.objects.filter(model=model,registered_number=number, status=1)

    else:
            if model=="":
                    if number=="":
                            cars = Cars.objects.filter(brand=marka,status=1)
                    else:
                            cars = Cars.objects.filter(brand=marka, registered_number=number, status=1)
            else:
                    if number=="":
                            cars = Cars.objects.filter(brand=marka, model=model, status=1)
                    else:
                            cars = Cars.objects.filter(brand=marka, model=model, registered_number=number, status=1)
    print(cars)
    drivers = Drivers.objects.filter(status=1)
    repair_services = RepairServices.objects.all()
    categories = RepairCategory.objects.filter(status=1)
    car_driver = RelCarDriver.objects.filter(status=1)
    car_listview = []
    oil_cards = PetrolCard.objects.filter(status=1)
    for car in cars:
        t = {}
        t['id'] = car.id
        t['marka'] = car.brand
        t['model'] = car.model
        t['number'] = car.registered_number
        t['dep'] = car.department
        t['engine'] = car.engine_power
        t['year'] = car.year_manufactured
        t['ban'] = car.BAN
        if len(RelCarDriver.objects.filter(status=1, car=car.id)) < 1:
            t['driver'] = ' '
        else:
            drivername = RelCarDriver.objects.filter(status=1, car=car.id)[0].driver.name
            driversurname = RelCarDriver.objects.filter(status=1, car=car.id)[0].driver.surname

            t['driver'] = drivername + ' ' + driversurname
            # t['driver'] = RelCarDriver.objects.filter(status=1, car=car.id)[0].car.registered_number

        if len(RelCarDriver.objects.filter(status=1, car=car.id)) < 1:
            t['date'] = ' '
        else:
            t['date'] = RelCarDriver.objects.filter(status=1, car=car.id)[0].date_assignment
        if len(RelPetrolCar.objects.filter(car_id=car.id, status=1)) > 0:
            petrolcardID = RelPetrolCar.objects.filter(car_id=car.id, status=1)[0].card_id
            # print('petrolcard id:', petrolcardID)
            petrolcardnumber = PetrolCard.objects.filter(id=petrolcardID)[0].card_number

            petrolcardlimit = RelPetrolLimit.objects.filter(card_id=petrolcardID)[0].limit
            # print('assigned petrol card number', petrolcardnumber)
            # print(petrolcardID, petrolcardlimit, petrolcardnumber)

        else:
            petrolcardnumber = 'Yanacaq kartı seçilməyib.'
            petrolcardlimit = ''
        t['petrolcardnumber'] = petrolcardnumber
        t['petrolcardlimit'] = petrolcardlimit
        if len(CarMilestage.objects.filter(car_id=car.id, status=1)) > 0:
            milestage = CarMilestage.objects.filter(car_id=car.id, status=1)[0].milestage
        else:
            milestage = 0
        t['milestage'] = milestage
        t['milestagehistorypopupdash'] = '#milestagehistory' + str(car.id)
        t['milestagehistorypopupid'] = 'milestagehistory' + str(car.id)
        t['oilcardpopupiddash'] = '#oilCardCars' + str(car.id)
        t['oilcardpopupid'] = 'oilCardCars' + str(car.id)
        t['milestagepopupiddash'] = '#updateMileStage' + str(car.id)
        t['milestagepopupid'] = 'updateMileStage' + str(car.id)
        t['repairhistorypopupiddash'] = '#viewHistoryCars' + str(car.id)
        t['repairhistorypopupid'] = 'viewHistoryCars' + str(car.id)
        t['editcardatapopupiddash'] = '#editCars' + str(car.id)
        t['editcardatapopupid'] = 'editCars' + str(car.id)
        t['deletecariddash'] = '#deleteCar' + str(car.id)
        t['deletecarid'] = 'deleteCar' + str(car.id)
        milestagehistory = []
        for j in CarMilestage.objects.filter(car_id=car.id):
            milestageitem = {}
            milestageitem['date'] = j.date
            milestageitem['milestage'] = j.milestage
            milestagestring = str(milestageitem['date'])[:11] + ' | ' + str(milestageitem['milestage'])
            milestagehistory.append(milestagestring)

        repairhistorylist = []
        repairhistorylist2 = []
        repairstring = ''
        for i in Repair.objects.filter(car_id=car.id):
            repairitem = {}
            repairitem['date'] = i.date
            repairitem['service'] = RepairServices.objects.filter(id=i.repair_service)[0].name
            repairitem['desc'] = i.repair_description
            repairstring = str(repairitem['date']) + " tarixində " + repairitem['desc'] + " (Servis: " + repairitem[
                'service'] + ")"
            repairhistorylist.append(repairitem)
            repairhistorylist2.append(repairstring)
        t['repairhistorylist'] = repairhistorylist
        t['repairhistorylist2'] = repairhistorylist2
        t['milestagehistory'] = milestagehistory
        # print(milestagehistory)
        car_listview.append(t)

    return render(request, 'garage/index.html',
                  {"cars": cars, "drivers": drivers, "services": repair_services, "categories": categories,
                   'car_listview': car_listview})


def filterdriver(request):
    data = request.POST.copy()
    name = str(data["name"])
    surname = str(data["surname"])

    drivers = Drivers.objects.filter(status=1)
    licenses = DriverLicences.objects.filter(status=1)

    if name == "":
        if surname == "":
            drivers = Drivers.objects.filter(status=1)
        else:
            drivers = Drivers.objects.filter(surname=surname, status=1)

    else:
        if surname == "":
            drivers = Drivers.objects.filter(name=name, status=1)
        else:
            drivers = Drivers.objects.filter(name=name, surname=surname, status=1)

    licenses = DriverLicences.objects.filter(status=1)
    driversListView = []
    for driver in drivers:
        t = {}
        t['id'] = driver.id
        t['fullname'] = driver.name + " " + driver.surname
        t['name'] = driver.name
        t['surname'] = driver.surname
        t['dep'] = driver.department
        # print('driver licence lennn:' , len(DriverLicences.objects.filter(status=1, driver_id=driver.id)))
        if len(DriverLicences.objects.filter(status=1, driver_id=driver.id)) > 0:
            seriya = DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].license_seriya
            # print('seriya', seriya)

            number = DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].license_number
            # print('num', number)
            t['license'] = seriya + number
            t['date'] = DriverLicences.objects.filter(status=1, driver_id=driver.id)[0].date_valid
        else:
            t['license'] = ' '
        t['updatelicensedash'] = '#updatelicense' + str(driver.id)
        t['updatelicenseid'] = 'updatelicense' + str(driver.id)
        t['editdriverdatadash'] = '#editDriver' + str(driver.id)
        t['editdriverdataid'] = 'editDriver' + str(driver.id)
        t['deletedriverdatadash'] = '#deleteDriver' + str(driver.id)
        t['deletedriverdataid'] = 'deleteDriver' + str(driver.id)
        driversListView.append(t)

    return render(request, 'garage/drivers.html', {"driversListView": driversListView})


def filteroilcard(request):
    data = request.POST.copy()
    cardnumber = data['cardnumber']
    # cards = PetrolCard.objects.filter(card_number=cardnumber, status=1)
    cards = PetrolCard.objects.filter(card_number__contains=cardnumber, status=1)

    cars = Cars.objects.filter(status=1)

    petrolcardListView = []
    for card in cards:
        t = {}
        t['id'] = card.id
        t['number'] = card.card_number
        if len(RelPetrolLimit.objects.filter(status=1, card_id=card.id)) > 0:
            t['limit'] = RelPetrolLimit.objects.filter(status=1, card_id=card.id)[0].limit
        else:
            t['limit'] = ''
        t['changelimitpopupdash'] = '#changeOilCardLimit' + str(card.id)
        t['changelimitpopupid'] = 'changeOilCardLimit' + str(card.id)
        t['limithistorypopupdash'] = '#viewOilCardHistory' + str(card.id)
        t['limithistorypopupid'] = 'viewOilCardHistory' + str(card.id)
        t['assignhistorypopupdash'] = '#assignCard' + str(card.id)
        t['assignhistorypopupid'] = 'assignCard' + str(card.id)
        t['deletecarddash'] = '#deleteCard' + str(card.id)
        t['deletecardid'] = 'deleteCard' + str(card.id)
        limithistorylist = []
        limithistorylist2 = []
        repairstring = ''
        for i in RelPetrolLimit.objects.filter(card_id=card.id):
            limititem = {}
            limititem['date'] = i.date_registered
            limititem['limit'] = i.limit
            limitstring = str(limititem['date'])[:11] + " | " + str(limititem['limit'])
            limithistorylist.append(limititem)
            limithistorylist2.append(limitstring)
        t['limithistorylist'] = limithistorylist
        t['limithistorylist2'] = limithistorylist2

        assignhistorylist = []
        assignhistorylist2 = []
        assignstring = ''
        for i in RelPetrolCar.objects.filter(card_id=card.id):
            assignitem = {}
            assignitem['date'] = i.date_registered
            assignitem['car'] = Cars.objects.filter(id=i.car_id)[0].registered_number
            assignstring = str(assignitem['date'])[:11] + " | " + str(assignitem['car'])
            assignhistorylist.append(limititem)
            assignhistorylist2.append(assignstring)
        t['assignhistorylist'] = assignhistorylist
        t['assignhistorylist2'] = assignhistorylist2

        petrolcardListView.append(t)
    return render(request, 'garage/oilCards.html',
                  {'petrolcardListView': petrolcardListView, 'cars': cars, 'cards': cards})
    return render(request, 'garage/index.html',
                  {"cars": cars, "drivers": drivers, "services": repair_services, 'car_listview': car_listview})

#this method does not save old data of updted cars
def editCarMethod_old(request,id):
    id = id

    data = request.POST.copy()
    brand = data['marka']
    model = data['model']
    registered_number = data['number']
    BAN = data['ban']
    engine_power = data['engine']
    year_manufactured = data['year']
    department = data['dep']


    if brand != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.brand = brand
            record.save(update_fields=['brand'])
            record.save()
    if model != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.model = model
            record.save(update_fields=['model'])
            record.save()
    if registered_number != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.registered_number = registered_number
            record.save(update_fields=['registered_number'])
            record.save()
    if BAN != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.BAN = BAN
            record.save(update_fields=['BAN'])
            record.save()
    if engine_power != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.engine_power = engine_power
            record.save(update_fields=['engine_power'])
            record.save()
    if year_manufactured != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.year_manufactured = year_manufactured
            record.save(update_fields=['year_manufactured'])
            record.save()
    if department != '':
        for record in Cars.objects.filter(id=id, status=1):
            record.department = department
            record.save(update_fields=['department'])
            record.save()

    return cars(request)

#this method changes status to 0 when updating car data
def editCarMethod(request, id):
    id = id
    data = request.POST.copy()
    dataUpdated = {}
    dataUpdated['brand'] = data['marka']
    dataUpdated['model'] = data['model']
    dataUpdated['registered_number'] = data['number']
    dataUpdated['BAN'] = data['ban']
    dataUpdated['engine_power'] = data['engine']
    dataUpdated['year_manufactured'] = data['year']
    dataUpdated['department'] = data['dep']

    # dataUpdated = {key: val for key, val in dataUpdated.items() if val != ''}

    car = Cars.objects.filter(id=id, status=1)[0]
    oldCarData = {}
    oldCarData['brand'] = car.brand
    oldCarData['model'] = car.model
    oldCarData['registered_number'] = car.registered_number
    oldCarData['BAN'] = car.BAN
    oldCarData['engine_power'] = car.engine_power
    oldCarData['year_manufactured'] = car.year_manufactured
    oldCarData['department'] = car.department

    for key, val in dataUpdated.items():
        if val == '':
            dataUpdated[key] = oldCarData[key]
    print(dataUpdated)

    if len(dataUpdated) > 0:
        for record in Cars.objects.filter(id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    newcar = Cars(brand=dataUpdated['brand'], model=dataUpdated['model'], registered_number=dataUpdated['registered_number'],
                  BAN=dataUpdated['BAN'],
                  engine_power=dataUpdated['engine_power'], year_manufactured=dataUpdated['year_manufactured'], organisation=1,
                  department=dataUpdated['department'],
                  status=1)
    newcar.save()
    updatedCarId = newcar.id

    for record in RelCarDriver.objects.filter(car_id=id, status=1):
        record.car_id = updatedCarId
        record.save(update_fields=['car_id'])
        record.save()

    for record in CarMilestage.objects.filter(car_id=id, status=1):
        record.car_id = updatedCarId
        record.save(update_fields=['car_id'])
        record.save()

    for record in Repair.objects.filter(car_id=id):
        record.car_id = updatedCarId
        record.save(update_fields=['car_id'])
        record.save()

    for record in RelPetrolCar.objects.filter(car_id=id, status=1):
        record.car_id = updatedCarId
        record.save(update_fields=['car_id'])
        record.save()


    return cars(request)


#this method changes status to 0 when updating driver data
def editDriverMethod(request, id):
    id = id
    data = request.POST.copy()

    dataUpdated = {}
    dataUpdated['name'] = data['name']
    dataUpdated['surname'] = data['surname']
    dataUpdated['department'] = data['dep']

    driver = Drivers.objects.filter(id=id, status=1)[0]
    oldDriverData = {}
    oldDriverData['name'] = driver.name
    oldDriverData['surname'] = driver.surname
    oldDriverData['department'] = driver.department

    #DriverLicences.objects.filter(driver_id=id, status=1)[0].id


    for key, val in dataUpdated.items():
        if val == '':
            dataUpdated[key] = oldDriverData[key]
    print(dataUpdated)

    if len(dataUpdated) > 0:
        for record in Drivers.objects.filter(id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    newdriver = Drivers(name=dataUpdated['name'], surname=dataUpdated['surname'], department=dataUpdated['department'], status=1)
    newdriver.save()
    updatedDriverId = newdriver.id

    for record in DriverLicences.objects.filter(driver_id=id, status=1):
        record.driver_id = updatedDriverId
        record.save(update_fields=['driver_id'])
        record.save()
    return drivers(request)


def deleteDriverMethod(request, id):
    data = request.POST.copy()
    #print('delete car method: ', id, data)
    if len(Drivers.objects.filter(id=id, status=1)) > 0:
        for record in Drivers.objects.filter(id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    return drivers(request)


def deleteCardMethod(request, id):
    data = request.POST.copy()
    #print('delete car method: ', id, data)
    if len(PetrolCard.objects.filter(id=id, status=1)) > 0:
        for record in PetrolCard.objects.filter(id=id, status=1):
            record.status = 0
            record.save(update_fields=['status'])
            record.save()

    return oilCards(request)


def hesabat(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Hesabat.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)

    repairs = Repair.objects.all()
    csvrow = ['Tarix', 'DQN', 'Servis', 'Kateqoriya', 'Görülən işlər', 'Xərc']
    writer.writerow(csvrow)
    for repair in repairs:
        row = []
        row.append(repair.date)
        # worksheet.write(0, row, repair.date)
        print('repair car id',repair.car_id)
        if len(Cars.objects.filter(id=repair.car_id))>0:
            row.append(Cars.objects.filter(id=repair.car_id)[0].registered_number)
        else:
            row.append(' ')
        if len(RepairServices.objects.filter(id=repair.repair_service)) > 0:
            row.append(RepairServices.objects.filter(id=repair.repair_service)[0].name)
        else:
            row.append(' ')
        if len(RepairCategory.objects.filter(id=repair.repair_cat_id)) > 0:
            row.append(RepairCategory.objects.filter(id=repair.repair_cat_id)[0].category_name)
        else:
            row.append(' ')
        row.append(repair.repair_description)
        row.append(repair.repair_price)
        writer.writerow(row)

    return response


