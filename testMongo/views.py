from django.http import HttpResponse
from testMongo.models import TestMongo

# Create your views here.
def index(request):
    return HttpResponse('Test!')

def saveData(request, key_id, value_id):
    entry = TestMongo(test_key = key_id, test_value = value_id)
    entry.save()
    return HttpResponse('Data saved successfully!')

def readData(request, key_id):
    for entry in TestMongo.objects.all():
        print entry['test_key'], key_id
        if entry['test_key'] == int(key_id):
            return HttpResponse(entry['test_value'])
    return HttpResponse('Data not found!')