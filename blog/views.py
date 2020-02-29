from django.shortcuts import render,HttpResponse
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response


'''
@api_view()
def say_hellow(request: Request):
    return Response(
        {
            'message':'Hellow world'
        }
    )

 '''
@api_view(['GET','POST'])
def index(request: Request):
    message3= ""
    if request.POST.get('name'):
        message3='Hellow ,' + request.POST.get('name')

    print(request.POST.get('name'))

    return Response(
        {'message':message3}

    )



# def index(request):
#     return HttpResponse(
#         {"m:Hellow django"})


