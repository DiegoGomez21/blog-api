from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializers
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
     
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    
    #Esto define por que parametro se puede buscar y editar una categoria en este caso
    #Sustituimos la clave unica
    
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title'] # <--- Este filtro lo podemos usar en postman agregando como parametro ?published=false
    
    #Ahora implementemos filtros :)
    
    #Devolvemos la categorias publicadas (comentar el queryset de arriba)
    queryset=Category.objects.filter(published=True)