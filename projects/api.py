from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerialiazer

class ProjectViewSet(viewsets.ModelViewSet): #El ViewSet establece quien puede consultar estos datos y que peticiones realizara 
    queryset = Project.objects.all() #punto de datos
    permission_classes = [permissions.AllowAny] #AllowAny cualquier aplicacion cliente puede solicitar datos al servidor
    serializer_class = ProjectSerialiazer
