# this turn data into json

from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from base.models import Rooms

class RoomSerializer(ModelSerializer):
    class Meta:
        model= Rooms
        fields = '__all__'