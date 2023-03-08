from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('enums', views.enums, name='enums'),

    path('tasks', views.tasks, name='tasks'),
    path('tasks/<int:taskId>', views.getTask, name='getTask'),

    path('assets/personnel', views.getPersonnel, name='getPersonnel'),
    path('assets/vehicles', views.getVehicles, name='getVehicles'),
    path('assets/buildings', views.getBuildings, name='getBuildings'),
    path('assets/modules', views.getModules, name='getModules'),

    path('inventory/warehouses', views.getWarehouses, name='getWarehouses'),
    path('inventory/warehousesWithReport', views.getWarehousesWithReport, name='getWarehousesWithReport'),
    path('inventory/stocks', views.getStocks, name='getStocks'),

    # =========================ICKO Services==================================
    path('tasks/cargoHandling/loadCargo', views.loadCargo, name='loadCargo'),
    path('tasks/cargoHandling/moveCargo', views.moveCargo, name='moveCargo'),

    path('cargoHistory', views.cargoHistory),
    path('cargoHistory/Custom', views.cargoHistoryCustom),
    path('loadTime', views.avgLoadTime),
    path('loadTime/Custom', views.avgLoadTimeCustom),

    path('truckStatus', views.truckStatus),
    # =========================================================================

    path('assets/temp', views.temp, name='getTemp'),

]
