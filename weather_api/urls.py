from django.urls import path,include
from . views import *


urlpatterns = [
    path('',DescriptionViewSet.as_view({'get':'list'}))
]
