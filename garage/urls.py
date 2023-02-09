from django.urls import path
from . import views


app_name = "garage"

urlpatterns = [
        path('', views.cars, name='garage-cars'),
        path('drivers/', views.drivers, name='garage-drivers'),
        path('oilcards/', views.oilCards, name='garage-oilcards'),
        path('parameters/', views.parameters, name='garage-parameters'),
        path('addCarMethod/', views.addCarMethod, name='addCarMethod'),
        path('assignCarMethod/', views.assignCarMethod, name='assignCarMethod'),
        path('addNewDriverMethod/', views.addNewDriverMethod, name='addNewDriverMethod'),
        path('addmilestageMethod/<id>', views.addmilestageMethod, name='addmilestageMethod'),
        path('changeDriverLicenseMethod/<id>', views.changeDriverLicenseMethod, name='changeDriverLicenseMethod'),
        path('changeOilCardLimitMethod/<id>', views.changeOilCardLimitMethod, name='changeOilCardLimitMethod'),
        path('addRepairLogMethod', views.addRepairLogMethod, name='addRepairLogMethod'),
        path('addOilCardMethod', views.addOilCardMethod, name='addOilCardMethod'),
        path('assignOilCardToCarMethod', views.assignOilCardToCarMethod, name='assignOilCardToCarMethod'),
        path('deleteCarMethod/<id>', views.deleteCarMethod, name='deleteCarMethod'),
        path('deleteDriverMethod/<id>', views.deleteDriverMethod, name='deleteDriverMethod'),
        path('deleteCardMethod/<id>', views.deleteCardMethod, name='deleteCardMethod'),
        path('filtercar', views.filtercar, name='filtercar'),
        path('filterdriver', views.filterdriver, name='filterdriver'),
        path('filteroilcard', views.filteroilcard, name='filteroilcard'),
        path('editCarMethod/<id>', views.editCarMethod, name='editCarMethod'),
        path('editDriverMethod/<id>', views.editDriverMethod, name='editDriverMethod'),
        path('hesabat', views.hesabat, name='hesabat'),
]



