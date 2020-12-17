from django.urls import path
from .userViews import (
    RegisterNurseryUser, 
    RegisterNormalUser, 
    LoginNurseryUser, 
    LoginNormalUser, 
    HelloWorldNursery, 
    HelloWorldNormal
)

from .plantViews import (
    AddPlant,
    GetPlant
)

from .orderViews import (
    OrderPlant,
    ViewOrders
)

urlpatterns = [
    path('nursery-register/', RegisterNurseryUser.as_view()),
    path('normal-register/', RegisterNormalUser.as_view()),
    path('nursery-login/', LoginNurseryUser.as_view()),
    path('normal-login/', LoginNormalUser.as_view()),
    path('hello-world-nursery/', HelloWorldNursery.as_view()),
    path('hello-world-normal/', HelloWorldNormal.as_view()),
    path('add-plant/', AddPlant.as_view()),
    path('get-plant/', GetPlant.as_view()),
    path('get-plant/<str:name>', GetPlant.as_view()),
    path('order-plant/', OrderPlant.as_view()),
    path('view-orders/', ViewOrders.as_view())
]