from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializers

class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()