import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    
    atm = datetime.today()
    brex = datetime(2019,5,29,11,0,0,0)
    now = brex - atm
    
    return HttpResponse("Hello, brexitters! Time to the end: " + str(now))

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)