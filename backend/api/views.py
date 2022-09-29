from itertools import product
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import JsonResponse
# import json for getting the frontend json format to dictionary and dict to json
# this data is comming from the client.py file
import json

# api end point view
def home(request,*args,**kwargs):
    data = request.body # json data comming through the body of the reqeusts
    # this requests is the instace of the HttpRequest
    print(request.body)
    # output
    # b'{"data": "this data from frontend json"}' ===> note the output that is in the format of binary string
    dict_format = {} #this line of code is used for suppose if we have no json data from font end

    try:
        dict_format = json.loads(data)
        print(dict_format)
    except:
        pass

    # headers, content_type
    # dict_format['headers'] = request.headers
    # got an error on HttpHeaders is not Json serilizable
    # this error because fo already the headersin json format again passing it to the JsonRespons

    print(request.headers)
    # {'Content-Length': '40', 
    # 'Content-Type': 'application/json', 
    # 'Host': '127.0.0.1:8000', 'User-Agent': 'python-requests/2.28.1',
    #  'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    #  HEADERS AND CONTENT TYPE
    dict_format['headers'] = dict(request.headers)
    dict_format['content_type'] = request.content_type
    
    #GETTING THE QUERY PARAMETERS
    dict_format['query_params'] = dict(request.GET)

    print(request.GET)
    # <QueryDict: {'category': ['mobile']}>
    return JsonResponse(dict_format)


# _____________________________________________________________________________________________
from products.models import Products
# model_to_dict
from django.forms.models import model_to_dict

def models_data_get(request):
    # for taking the random values from the database
    product = Products.objects.all().order_by('?').first()
    print(product)
    data = {}
    # this method we need to do manually 
    # converting the data to dictionary format
    # this may take too much time
 
    if product:
        'instead of this method we can use model_to_dict method'
        # data['title'] = product.title
        # data['content'] = product.content
        # data['price'] = product.price

        # also we can difine the feilds iside of the model_to_dict method
        # fields = ['id','price' ]
        data = model_to_dict(product)
        ''' we can define the fields inside of the model_to_dict function 
        data = model_to_dict(product, fields=['id' , 'title' ])'''

    return JsonResponse(data)

    # USING DJANGO REST FRAME WORK
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def rest_view(reqeust,*args,**kwargs):
    product = Products.objects.all().order_by('?').first()

    data = {}
    try:
        data = model_to_dict(product)
        ''' '''
    except:
        pass
    return Response(data)

