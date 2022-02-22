# Django
from email import message
from django.http import HttpResponse,  JsonResponse


def sort_items(request):
    items = sorted(map(int, request.GET["items"].split(",")), reverse=True)
    data = {
        "status" : "ok",
        "numbers" : items,
        "message" : "Integers sorted successfully"
    }
    return JsonResponse(data)


def say_hi(request, name, age):
    if age < 12:
        message = f"Sorry, {name} you are not allowed here"
    else:
        message = f"Welcome to Instagram, {name} !!!"
    
    return HttpResponse	(message)

