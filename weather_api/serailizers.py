from rest_framework import serializers
from . models import *


class DescriptionSerializer(serializers.Serializer):
    class Meta:
        model = Description
        fields = ['id','description','temperature','created_on']