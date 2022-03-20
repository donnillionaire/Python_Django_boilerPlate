# in the file we are going to create model serializer because response serializer cannot natively handle complex data types such as django model 
# instances so we will first need to serialize this data before we can actualy start to render it out

# so we will create serializers for our item model and all this will do is convert instances of our items from objects to datatypes the reponse object can understand

from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item # model 
        fields='__all__' # fields that we want to serialize