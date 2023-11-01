from django.urls import path
from django.contrib import admin
from .views import *


app_name = 'design_studio'


urlpatterns = [
   path('superadmin/', admin.site.urls),
   path('', index, name='index'),
   path('register/', RegistrateUser.as_view(), name='registration'),
   path('login/', BBLoginView.as_view(), name='login'),
   path('logout/', BBLogoutView.as_view(), name='logout'),
   path('request/create', CreateRequest.as_view(), name='request_create'),
   path('request/', ViewRequests.as_view(), name='request')
]

