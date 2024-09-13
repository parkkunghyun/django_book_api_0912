from rest_framework import serializers
from .models import Category, Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField -> 다른 모델의 기본키 ID를 직렬화하는데 사용
    # queryset=Author.objects.all -> 유효한 Author인스턴스를 정의, 
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    class Meta:
        model = Book
        fields = "__all__"