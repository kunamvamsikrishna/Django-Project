
from django.urls import path
from .views import *
urlpatterns =[
    path('post_user_details/',post_user_details,name='post_user_details'),
    path('get_user_details/',get_user_details,name='get_user_details'),
    path('delete_user_details/<int:id>/',delete_user_details,name='delete_user_details'),
    path('update_user/<int:id>/,',update_user_details,name="update_user_details")
]
