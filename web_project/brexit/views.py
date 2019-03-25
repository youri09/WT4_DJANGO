import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    
    atm = datetime.today()
    brex = datetime(2019,5,29,11,0,0,0)
    now = brex - atm
    
    return HttpResponse("Hello, brexitters! Time to the end: " + str(now))