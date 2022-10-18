from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'completed')

#specifies the model to work with and the fields to be converted to JSON - because react is in javascript uses JSON