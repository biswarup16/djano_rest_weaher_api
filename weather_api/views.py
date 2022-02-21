from django.shortcuts import render
from . serailizers import *
from rest_framework import viewsets
from . models import *


class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
