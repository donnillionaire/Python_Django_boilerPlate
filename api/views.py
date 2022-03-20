from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])      #api_view decorator and pass in GET method to the list of allowed methods
def getData(request):
    #person={'name': 'Dennis', 'age': 28} # a dictionary with key value pairs and pass it to the response object
    items= Item.objects.all()
    #after querying we will need to serialize them before we can return them
    serializer= ItemSerializer(items, many=True) #many= True means we want to serialize many items

    return Response(serializer.data)   #for the return object lets just use the Response object that we have just imported
                             # as soon as dictionary is passed to the response, it will be returned as output data




@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data) #data sent in from the front end being serialized
    #check if the data coming in is valid data
    if serializer.is_valid():
        serializer.save() #save the newly created data to the database
    return Response(serializer.data)

