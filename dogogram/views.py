import json
from django.http import HttpResponse

def sort_list(request):
    numbers_list = request.GET["numbers"].split(",")
    numbers_list.sort(key= lambda i: int(i))
    return HttpResponse(json.dumps({ "number": numbers_list }))

def hi(request, name, age):
    if age < 12:
        message = f"Sorry, {name}. You're not allowed here"
    else:
        message = f"Hi, {name}. You're wellcome to Dogogram!"
    return HttpResponse(f"<h1>{message}</h1>")