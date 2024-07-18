from rest_framework import serializers

from .models import Book , Category_subcategory , Subcategory

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_subcategory
        fields = '__all__'


class SubcategorySerialize(serializers.ModelSerializer):
      cateory= Category_subcategory()

      class Meta:
        model = Subcategory
        fields =  '__all__'














