from django.shortcuts import render
from mytools.models import Device,DeviceConfiguration,Operator
from django.http import HttpResponse
import json
import asyncio
import time
import random
from netmiko import ConnectHandler
# import os
# import django
import threading
# from asgiref.sync import sync_to_async
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()



# Create your views here.
def load_file(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        data = request.body
        print(data)

    response1 = ""
    config_list = Device.objects.all().values()
    for var in config_list:
        response1 += (str(var) + "</br>")
    response = response1
    return HttpResponse(response)

def load_device_info(request):
    devices_info = list() #所有设备配置list
    task_list = list()
    response = str()
    config_list = Device.objects.all().values()
    devices_info = list() #所有设备配置list
    par_list = list()
    threading_list = list()
    for var in config_list:
        devices_info.append(eval(str(var)))
    for each_divice_info in devices_info:
        par = {"device_type" : each_divice_info["device_type"],
               "host" : each_divice_info["device_ip"],
               "username" : each_divice_info["device_username"],
               "password" : each_divice_info["device_password"],
               "secret" : each_divice_info["device_secret"],
               "port" : each_divice_info["device_port"],
               "device_id" : each_divice_info["device_id"],
               "device_location_city" : each_divice_info["device_location_city"],
               "device_location_specific" : each_divice_info["device_location_specific"]}
        par_list.append(par)

    for each_par in par_list:
        threading_list.append(threading.Thread(target=get_config,args=(each_par,)))
    for each_th in threading_list:
        each_th.start()
    return HttpResponse("ok")


def get_config(par):
    device_id = par.pop("device_id")
    device_location_city = par.pop("device_location_city")
    device_location_specific = par.pop("device_location_specific")
    try :
        with ConnectHandler(**par) as net_connect:
            net_connect.enable()
            response = net_connect.send_command("show running-config")
            DeviceConfiguration.objects.create(device_id =device_id,
            create_person_id = random.randint(0,10),
            device_config = response,
            create_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    except Exception as e:
        print(e)
    #return HttpResponse(output)

