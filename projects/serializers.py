#Este archivo llamaremos un modulo especial de DRF

from rest_framework import serializers
from .models import Project

class ProjectSerialiazer(serializers.ModelSerializer): #Esto convierte un modelo en datos que van a ser consultados
    class Meta:
        model = Project
        fields = ("id","title", "description", "technology", "created_at")
        read_only_fields = ("created_at",)



