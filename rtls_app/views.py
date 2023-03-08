from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import *
import datetime
import pandas as pd
import json


def shitPrint(count):
    print("=================================")
    print("=================================")
    print("=================================")
    print("HERE", count)
    print("=================================")
    print("=================================")
    print("=================================")


# ==========================================================
# ==========================================================
# ==========================================================
######################## GETTERS ##########################
# ==========================================================
# ==========================================================
# ==========================================================


def enums(request):
    """
    Used for retrieving all the enumerations existing on the database.
    :param request:
    :return: A json series of all Enumerations
    """

    # passing data using serializer
    '''
    all_enums = serializers.serialize('json' ,  Enumeration.objects.all())
    '''

    # passing data using manual json creator
    data = {}
    all_enums = Enumeration.objects.all()
    for obj in all_enums:
        temp = {}
        temp['enumId'] = obj.enum_id
        temp['description'] = obj.description
        temp['enumTypeId'] = obj.enum_type_id_id
        temp['parentEnumId'] = obj.parent_enum_id_id

        data[obj.id] = temp

    return JsonResponse(data)


def tasks(request):
    if request.method == "GET":
        data_rec = request.GET
        # TODO : Setup Appropriate username in the following line of code
        username = "Admin"  # data_rec['username']
        asset_id = User.objects.get(username=username).asset_id_id

        task_resps = TaskResponsible.objects.filter(asset_id_id=asset_id)

        data = {}
        for task_resp in task_resps:
            temp = {}
            temp['fromDate'] = task_resp.fromDate
            temp['thruDate'] = task_resp.tillDate

            task = Task.objects.get(task_id=task_resp.task_id_id)

            temp['title'] = task.title
            temp['description'] = task.description
            temp['orderDate'] = task.orderDate
            temp['deadline'] = task.deadline
            temp['data'] = task.data

            temp['category'] = Enumeration.objects.get(id=task.category_enum_id_id).description
            temp['priority'] = Enumeration.objects.get(id=task.priority_enum_id_id).description
            temp['status'] = Enumeration.objects.get(id=task.status_enum_id_id).description
            if Task.objects.filter(task_id=task.parent_id_id):
                temp['parent'] = Task.objects.get(task_id=task.parent_id_id).task_id
            else:
                temp['parent'] = -1

            subTasks = Task.objects.filter(parent_id_id=task.task_id)

            if subTasks:
                counter = 0
                for subTask in subTasks:
                    if subTask.status_enum_id_id == Enumeration.objects.get(enum_id='tskStaDone').id:
                        counter += 1
                progress = counter / len(subTasks)
                temp['progress'] = progress
            else:
                temp['progress'] = 'No SubTask Defined'

            data[task_resp.id] = temp

        if "categoryEnumId" in data_rec.keys():
            category = Enumeration.objects.get(enum_id=data_rec["categoryEnumId"])
            data["category"] = category.description
        if "statusEnumId" in data_rec.keys():
            status = Enumeration.objects.get(enum_id=data_rec["statusEnumId"])
            data["status"] = status.description
        if "priorityEnumId" in data_rec.keys():
            priority = Enumeration.objects.get(enum_id=data_rec["priorityEnumId"])
            data["priority"] = priority.description

        return JsonResponse(data)


def getTask(request, taskId):
    if Task.objects.filter(task_id=taskId):
        task = Task.objects.filter(task_id=taskId)[0]
        data = {}
        data['title'] = task.title
        data['description'] = task.description
        data['orderDate'] = task.orderDate
        data['deadline'] = task.deadline
        data['data'] = task.data
        data['category_enum_id'] = task.category_enum_id_id
        data['priority_enum_id'] = task.priority_enum_id_id
        data['status_enum_id'] = task.status_enum_id_id
        data['parent_id'] = task.parent_id_id

        objs = Task.objects.filter(parent_id_id=taskId)
        subTasks = {}
        for obj in objs:
            subTasks[obj.task_id] = obj.description
        data['subtasks'] = subTasks

        return JsonResponse(data)
    else:
        return JsonResponse("Task {} Not Found".format(taskId), safe=False)


def getPersonnel(request):
    persons = Person.objects.all()
    data = {}
    for person in persons:
        tempData = {}
        tempData['firstName'] = person.first_name
        tempData['lastName'] = person.last_name
        tempData['birthDate'] = person.birth_date
        tempData['nationalID'] = person.nationalid
        tempData['assetID'] = person.asset_id_id
        tempData['gender'] = Enumeration.objects.get(id=person.gender_enum_id_id).description
        tempData['prefix'] = Enumeration.objects.get(id=person.prefix_enum_id_id).description
        post = Post.objects.get(post_id=person.post_id_id)
        tempData['postTitle'] = post.title
        tempData['postCode'] = post.code

        data[person.id] = tempData
    return JsonResponse(data=data)


def getVehicles(request):
    vehicles = Vehicle.objects.all()
    data = {}
    for vehicle in vehicles:
        tempData = {}
        tempData['name'] = vehicle.name
        tempData['brand'] = vehicle.brand
        tempData['color'] = vehicle.color
        tempData['assetID'] = vehicle.asset_id_id

        tempData['status'] = Enumeration.objects.get(id=vehicle.status_enum_id_id).description
        tempData['type'] = Enumeration.objects.get(id=vehicle.type_enum_id_id).description
        data[vehicle.id] = tempData

    print("============================")
    print("============================")
    print("============================")
    print(data)
    print("============================")
    print("============================")
    print("============================")

    # return render(request , "home.html", context={"data" : data})
    # return HttpResponse('home.html' , content=data)
    return JsonResponse(data=data)


def getBuildings(request):
    buildings = Building.objects.all()
    data = {}
    for building in buildings:
        tempData = {}
        tempData['name'] = building.name
        tempData['latitude'] = building.latitude
        tempData['longitude'] = building.longitude

        tempData['status'] = Enumeration.objects.get(id=building.status_enum_id_id).description
        tempData['type'] = Enumeration.objects.get(id=building.type_enum_id_id).description

        data[building.building_id] = tempData

    return JsonResponse(data=data)


def getModules(request):
    modules = Module.objects.all()
    data = {}
    for module in modules:
        tempData = {}
        tempData['name'] = module.name
        tempData['macAddr'] = module.mac_addr
        tempData['locationID'] = module.location_id_id
        tempData['status'] = module.status_enum_id_id

        if Person.objects.filter(asset_id_id=module.asset_id_id):
            person = Person.objects.filter(asset_id_id=module.asset_id_id)[0]
            tempData['assetName'] = person.first_name + " " + person.last_name + "_" + str(module.asset_id_id)
        elif Vehicle.objects.filter(asset_id_id=module.asset_id_id):
            vehicle = Vehicle.objects.filter(asset_id_id=module.asset_id_id)[0]
            tempData['assetName'] = vehicle.name + "_" + module.asset_id_id

        tempData['status'] = Enumeration.objects.get(id=module.status_enum_id_id).description
        tempData['type'] = Enumeration.objects.get(id=module.type_enum_id_id).description

        data[module.module_id] = tempData

    return JsonResponse(data=data)


def getWarehouses(request):
    data = {}
    warehouses = Building.objects.filter(type_enum_id_id=Enumeration.objects.get(enum_id='bldWarehouse').id)
    for warehouse in warehouses:
        tempData = {}
        tempData['name'] = warehouse.name
        tempData['latitude'] = warehouse.latitude
        tempData['longitude'] = warehouse.longitude

        tempData['status'] = Enumeration.objects.get(id=warehouse.status_enum_id_id).description
        tempData['type'] = Enumeration.objects.get(id=warehouse.type_enum_id_id).description

        data[warehouse.building_id] = tempData

    return JsonResponse(data=data)


def getStocks(request):
    data = {}
    stocks = Stock.objects.all()
    for stock in stocks:
        tempData = {}
        tempData['name'] = stock.name
        tempData['code'] = stock.code
        tempData['category'] = Enumeration.objects.get(id=stock.category_enum_id_id).description

        data[stock.stock_id] = tempData

    return JsonResponse(data=data)


def getWarehousesWithReport(request):
    data = {}
    warehouses = Building.objects.filter(type_enum_id_id=Enumeration.objects.get(enum_id='bldWarehouse').id)
    print(warehouses)
    for warehouse in warehouses:
        print("*********************")
        tempData = {}
        tempData['name'] = warehouse.name
        tempData['latitude'] = warehouse.latitude
        tempData['longitude'] = warehouse.longitude
        capacity = 0
        fullness = 0
        floors = warehouse.floor_set.all()
        for floor in floors:
            capacity += floor.capacity
            zones = floor.zone_set.all()
            for zone in zones:
                locations = zone.location_set.all()
                for location in locations:
                    palletes = location.inventory_set.all()
                    print(palletes)
                    for pallete in palletes:
                        if pallete.tillDate is None:
                            fullness += pallete.volume
        if capacity == 0:
            print("Prolem in Reading CAPACITY")
        else:
            tempData['fullnessCount'] = fullness
            fullness = fullness / capacity
        tempData['fullness'] = fullness
        tempData['capacity'] = capacity
        tempData['status'] = Enumeration.objects.get(id=warehouse.status_enum_id_id).description
        tempData['type'] = Enumeration.objects.get(id=warehouse.type_enum_id_id).description

        data[warehouse.building_id] = tempData

    return JsonResponse(data=data)


# ==========================================================
# ==========================================================
# ==========================================================
######################## SETTERS ##########################
# ==========================================================
# ==========================================================
# ==========================================================


def loadCargo(request):
    if request.method == "POST":
        data = request.POST
        taskID = data['taskID']

        task = Task.objects.filter(task_id=taskID)[0]
        task.status_enum_id_id = Enumeration.objects.get(enum_id='taskStaLoaded').id
        task.save()
        SAVE = True

        return JsonResponse(SAVE, safe=False)

    SAVE = False
    return JsonResponse(SAVE, safe=False)


def moveCargo(request):
    if request.method == "POST":
        data = request.POST
        taskID = data['taskID']

        task = Task.objects.filter(task_id=taskID)[0]
        task.status_enum_id_id = Enumeration.objects.get(enum_id='taskStaMoved').id
        task.save()
        SAVE = True

        return JsonResponse(SAVE, safe=False)

    SAVE = False
    return JsonResponse(SAVE, safe=False)


# TODO: Not Debugged
def cargoReception(request):
    if request.method == "POST":
        data = request.POST
        if "thruDate" in data.keys():
            newTask = Task(
                category_enum_id_id=Enumeration.objects.get(enum_id="tskCatCargoHandling").id,
                title=Enumeration.objects.get(enum_id='moveCargoTypeId').description,
                description=data['description'],
                priority_enum_id_id=Enumeration.objects.get(enum_id="priorityHigh").id,
                orderDate=data['fromDate'],
                deadline=data['thruDate'],
                status_enum_id_id=Enumeration.objects.get(enum_id="tskStaOpen").id,
            )
            newTask.save()
            operators = Person.objects.filter(post_id_id="operator")
            for operator in operators:
                newTaskResponsible = TaskResponsible(
                    task_id_id=newTask.task_id,
                    fromDate=data['fromDate'],
                    asset_id_id=operator.asset_id_id,
                    tillDate=data['thruDate'],
                )
                newTaskResponsible.save()
        else:
            newTask = Task(
                category_enum_id_id=Enumeration.objects.get(enum_id="tskCatCargoHandling").id,
                title=Enumeration.objects.get(enum_id='moveCargoTypeId').description,
                description=data['description'],
                priority_enum_id_id=Enumeration.objects.get(enum_id="priorityHigh").id,
                orderDate=data['fromDate'],
            )
            newTask.save()
            operators = Person.objects.filter(post_id_id="operator")
            for operator in operators:
                newTaskResponsible = TaskResponsible(
                    task_id_id=newTask.task_id,
                    fromDate=data['fromDate'],
                    asset_id_id=operator.asset_id_id,
                )
                newTaskResponsible.save()
        for item in data['cargoList']:
            newInv = Inventory(
                count=1,
                fromDate=data['fromDate'],
                # tillDate = None,
                # location_id_id = None,
                # TODO : Turn On The StockId
                # stock_id_id = None,
                volume=item['count'],
            )
            newInv.save()

            if "thruDate" in data.keys():
                newSubTask = Task(
                    category_enum_id_id=Enumeration.objects.get(enum_id="tskCatCargoHandling").id,
                    title=Enumeration.objects.get(enum_id='moveCargoTypeId').description,
                    description=data['description'],
                    priority_enum_id_id=Enumeration.objects.get(enum_id="priorityHigh").id,
                    orderDate=data['fromDate'],
                    deadline=data['thruDate'],
                    status_enum_id_id=Enumeration.objects.get(enum_id="tskStaWaitingForLoading").id,
                    parent_enum_id_id=newTask.task_id,
                    data={
                        "correspondingInventory": newInv.inventory_id
                    },
                )
                newSubTask.save()
            else:
                newSubTask = Task(
                    category_enum_id_id=Enumeration.objects.get(enum_id="tskCatCargoHandling").id,
                    title=Enumeration.objects.get(enum_id='moveCargoTypeId').description,
                    description=data['description'],
                    priority_enum_id_id=Enumeration.objects.get(enum_id="priorityHigh").id,
                    orderDate=data['fromDate'],
                    status_enum_id_id=Enumeration.objects.get(enum_id="tskStaWaitingForLoading").id,
                    parent_enum_id_id=newTask.task_id,
                    data={
                        "correspondingInventory": newInv.inventory_id
                    },
                )
                newSubTask.save()
        return JsonResponse({"mission": True})
    else:
        return JsonResponse({"mission": False})


def cargoHistory(request):
    data = {}
    travels = Travel.objects.all()
    for travel in travels:
        if travel.asset_id_id in data.keys():
            data[travel.asset_id_id] += 1
        else:
            data[travel.asset_id_id] = 1
    return JsonResponse(data=data)


def cargoHistoryCustom(request):
    if request.method == "POST":
        returnData = {}
        data = request.POST
        assetId = data['id']
        travels = Travel.objects.filter(asset_id_id=assetId)
        if 'id' in data.keys():
            if 'timestamp' in data.keys():
                returnData = {'count': 0}
                for travel in travels:
                    if travel.startTimestamp <= data[
                        'timestamp'] <= travel.endTimestamp and travel.asset_id_id == assetId:
                        returnData['cargoCount'] += 1
            elif 'fromTimestamp' in data.keys():
                returnData = {'count': 0}
                for travel in travels:
                    if data['fromTimestamp'] >= travel.startTimestamp and data[
                        'tillTimestamp'] <= travel.endTimestamp and travel.asset_id_id == assetId:
                        returnData['cargoCount'] += 1
        else:
            if 'timestamp' in data.keys():
                returnData = {}
                for travel in travels:
                    if travel.startTimestamp <= data['timestamp'] <= travel.endTimestamp:
                        if travel.asset_id_id in returnData.keys():
                            returnData[travel.asset_id_id] += 1
                        else:
                            returnData[travel.asset_id_id] = 1
            elif 'fromTimestamp' in data.keys():
                returnData = {}
                for travel in travels:
                    if data['fromTimestamp'] >= travel.startTimestamp and data['tillTimestamp'] <= travel.endTimestamp:
                        if travel.asset_id_id in returnData.keys():
                            returnData[travel.asset_id_id] += 1
                        else:
                            returnData[travel.asset_id_id] = 1

        return JsonResponse(returnData)


def avgLoadTime(request):
    travels = Travel.objects.all()
    underLoadTimes = {}
    for travel in travels:
        underLoadTime = travel.endTimestamp - travel.startTimestamp
        if travel.asset_id_id in underLoadTimes.keys():
            underLoadTimes[travel.asset_id_id][0] += underLoadTime
            underLoadTimes[travel.asset_id_id][1] += 1
            pass
        else:
            underLoadTimes[travel.asset_id_id] = [underLoadTime, 1]
    avgUnderLoads = {}
    for assetId in underLoadTimes.keys():
        avgUnderLoads[assetId] = underLoadTimes[assetId][0] / underLoadTimes[assetId][1]

    return JsonResponse(avgUnderLoads)


def avgLoadTimeCustom(request):
    if request.method == 'POST':
        returnData = {}
        data = request.POST
        id = data['id']
        travels = Travel.objects.filter(asset_id_id=id)
        underLoadTime = 0
        for travel in travels:
            underLoadTime += travel.endTimestamp - travel.startTimestamp
        avg = underLoadTime/len(travels)
        returnData['avgUnderLoadTime'] = avg

        return JsonResponse(returnData)


def truckStatus(request):
    trucks = Vehicle.objects.filter(type_enum_id=Enumeration.objects.get(enum_id='vhcTypeTruck'))
    returnData = {}
    for truck in trucks:
        returnData[truck.id] = {
            'id': truck.id,
            'name': truck.name,
            'brand': truck.brand,
            'color': truck.color,
            'assetId': truck.asset_id_id,
            'status': Enumeration.objects.get(id=truck.status_enum_id_id).description,
            'type': Enumeration.objects.get(id=truck.type_enum_id_id).description,
        }

    return JsonResponse(returnData)


def temp(request):
    vars = Module.objects.all()
    return HttpResponse(vars)


def index(request):
    # return JsonResponse({} ,safe=False)
    return HttpResponse("Hello, Done")


def socketCheck(request):
    pass
