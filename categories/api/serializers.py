from rest_framework import serializers
from categories.models import Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fiels = ['title','slug','published']

    