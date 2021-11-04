from django.shortcuts import render
from mytools.models import Device,DeviceConfiguration,Operator
from django.http import HttpResponse

# Create your views here.
def load_file(request):
    # if request.method == "GET":
    #     return render(request, 'index.html')
    # if request.method == "POST":
    #     data = request.POST['router']
    #     print(data)
    response1 = ""
    config_list = DeviceConfiguration.objects.all().values()
    for var in config_list:
        response1 += (str(var) + "</br>")
    response = response1
    return HttpResponse(response)

def get_config():
    response = str()
    config_list = DeviceConfiguration.objects.all().values()
    for var in config_list:
        response += (str(var) + "</br>")
    return HttpResponse(response)