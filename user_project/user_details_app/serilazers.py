from rest_framework import serializers
from .models import *

class UserDetailsSerilazer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails 
        fields = '__all__'
   